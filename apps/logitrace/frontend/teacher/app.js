const API_BASE = window.location.origin;
const WS_URL = `${window.location.protocol === "https:" ? "wss:" : "ws:"}//${window.location.host}/api/teacher/ws/ambient`;

const KC_META = [
  { id: "WLAN_STANDARDS",         code: "01", short: "Standar",   name: "Standar 802.11 b/g/n/ac/ax" },
  { id: "WLAN_TOPOLOGY_BSS",      code: "02", short: "Topologi",  name: "Topologi Ad-Hoc vs Infrastructure" },
  { id: "IP_PEER_CONFIG",         code: "03", short: "IP",        name: "Pengalamatan IPv4 & Subnetting" },
  { id: "WLAN_FREQ_CHANNEL",      code: "04", short: "Kanal",     name: "Alokasi Kanal Non-Overlapping" },
  { id: "WLAN_SECURITY_AUTH",     code: "05", short: "Keamanan",  name: "Keamanan WPA2-PSK / WPA3-SAE" },
  { id: "WLAN_HOST_HARDENING",    code: "06", short: "Hardening", name: "MAC Filter & Firewall" },
  { id: "WLAN_SIGNAL_PROP",       code: "07", short: "Sinyal",    name: "Redaman Sinyal & RSSI" },
  { id: "WLAN_ROAMING_PROB",      code: "08", short: "Roaming",   name: "Roaming & Hysteresis" },
  { id: "WLAN_CHANNEL_COLLISION", code: "09", short: "Kolisi",    name: "Collision & Kepadatan Kanal" },
  { id: "ICMP_CONNECTIVITY",      code: "10", short: "Ping",      name: "Uji Konektivitas Ping & RTT" },
  { id: "ICMP_TROUBLE_DHU",       code: "11", short: "DHU",       name: "Destination Host Unreachable" },
  { id: "ICMP_TROUBLE_RTO",       code: "12", short: "RTO",       name: "Request Timed Out" }
];
const KC_KEYS = KC_META.map(k => k.id);
const KC_BY_ID = Object.fromEntries(KC_META.map(k => [k.id, k]));

let ws = null;
let fallbackPollTimer = null;
let pingTimer = null;
let currentSessionId = null;
let sessionsList = [];
let activeConfirmCallback = null;

// Station Rotation 35-minute Timer Logic
let timerSeconds = 35 * 60;
let timerInterval = null;
let isTimerRunning = false;

function toggleRotationTimer() {
  const btn = document.getElementById("btn-timer-toggle");
  if (isTimerRunning) {
    clearInterval(timerInterval);
    isTimerRunning = false;
    btn.innerHTML = "&#9654;";
  } else {
    isTimerRunning = true;
    btn.innerHTML = "&#10074;&#10074;";
    timerInterval = setInterval(() => {
      if (timerSeconds > 0) {
        timerSeconds--;
        updateTimerDisplay();
      } else {
        clearInterval(timerInterval);
        isTimerRunning = false;
        btn.innerHTML = "&#9654;";
        showToast("Waktu 35 Menit Selesai! Saatnya pergantian zona Station Rotation.", "success");
      }
    }, 1000);
  }
}

function resetRotationTimer() {
  clearInterval(timerInterval);
  isTimerRunning = false;
  timerSeconds = 35 * 60;
  updateTimerDisplay();
  document.getElementById("btn-timer-toggle").innerHTML = "&#9654;";
}

function updateTimerDisplay() {
  const m = Math.floor(timerSeconds / 60);
  const s = timerSeconds % 60;
  document.getElementById("rotation-timer").textContent =
    `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
}

function escapeHtml(str) {
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function showToast(message, type = "info") {
  const container = document.getElementById("toast-container");
  const toast = document.createElement("div");

  let styleClass = "bg-eel text-white border-black/20";
  if (type === "success") styleClass = "bg-feather text-white border-feather-shade";
  if (type === "error") styleClass = "bg-cardinal text-white border-cardinal-shade";

  toast.className = `${styleClass} px-4 py-3 rounded-2xl border-2 border-b-4 flex items-center gap-2.5 text-xs font-sans font-extrabold pointer-events-auto transform transition-all duration-300`;
  toast.textContent = String(message || "");
  container.appendChild(toast);

  setTimeout(() => {
    toast.classList.add("opacity-0", "translate-y-2");
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

// Custom Confirm Modal & Global Escape Dismiss
function openConfirmModal({ title, body, okLabel, onConfirm }) {
  document.getElementById("confirm-title").textContent = title;
  document.getElementById("confirm-body").textContent = body;
  document.getElementById("confirm-ok-btn").textContent = okLabel || "Ya, Lanjutkan";
  activeConfirmCallback = onConfirm;
  document.getElementById("modal-confirm").classList.remove("hidden");
}

function closeConfirmModal() {
  document.getElementById("modal-confirm").classList.add("hidden");
  activeConfirmCallback = null;
}

document.getElementById("confirm-cancel-btn").onclick = closeConfirmModal;
document.getElementById("confirm-ok-btn").onclick = async () => {
  const cb = activeConfirmCallback;
  closeConfirmModal();
  if (typeof cb === "function") await cb();
};
document.getElementById("modal-confirm").onclick = (e) => {
  if (e.target.id === "modal-confirm") closeConfirmModal();
};

document.addEventListener("keydown", (e) => {
  if (e.key !== "Escape") return;
  if (!document.getElementById("modal-confirm").classList.contains("hidden")) {
    closeConfirmModal();
    return;
  }
  if (!document.getElementById("modal-summary").classList.contains("hidden") && typeof closeSummaryModal === "function") {
    closeSummaryModal();
    return;
  }
  if (!document.getElementById("modal-manage").classList.contains("hidden") && typeof closeManageModal === "function") {
    closeManageModal();
  }
});

// Session Management Helpers
async function loadSessions() {
  try {
    const res = await fetch(`${API_BASE}/api/sessions?class_rombel=XI%20TKJ%201`);
    if (!res.ok) throw new Error("Gagal mengambil data sesi");
    sessionsList = await res.json();

    if (typeof loadClassCode === "function") loadClassCode();
    if (sessionsList.length === 0) return;

    if (!currentSessionId) {
      const active = sessionsList.find(s => s.is_active);
      currentSessionId = active ? active.id : sessionsList[0].id;
    }
    updateBannerTag();

    if (typeof renderSessionCardsInModal === "function") {
      renderSessionCardsInModal();
    }
  } catch (err) {
    console.error("Error loading sessions:", err);
  }
}

function updateBannerTag() {
  const tag = document.getElementById("banner-active-tag");
  if (!tag) return;
  const s = sessionsList.find(x => x.id === currentSessionId);
  const isActive = !s || s.is_active;
  tag.textContent = isActive ? "Sesi aktif" : "Tidak aktif · hanya dilihat";
  tag.className = isActive
    ? "px-2.5 py-0.5 rounded-full text-[11px] font-num font-bold uppercase bg-feather-soft text-feather-shade border border-feather/30"
    : "px-2.5 py-0.5 rounded-full text-[11px] font-num font-bold uppercase bg-snow text-wolf border border-swan";
}

function onSessionDropdownChange(sessionId) {
  if (!sessionId) return;
  currentSessionId = sessionId;
  refreshAmbientState();
}

function promptResetAllCurrentSession() {
  if (!currentSessionId) {
    showToast("Silakan pilih sesi terlebih dahulu.", "error");
    return;
  }
  openConfirmModal({
    title: "Ulangi seluruh kelas?",
    body:
      `Sesi: ${typeof currentSessionLabel === "function" ? currentSessionLabel() : ""}\n\n` +
      "• Semua siswa mulai lagi dari Soal 1.\n" +
      "• Progres dan penguasaan di dasbor kembali kosong.\n" +
      "• Riwayat jawaban lama tetap tersimpan untuk audit.",
    okLabel: "Ya, ulangi kelas",
    onConfirm: async () => {
      try {
        const res = await fetch(`${API_BASE}/api/sessions/${currentSessionId}/reset-all`, { method: "POST" });
        if (!res.ok) throw new Error("Gagal me-reset sesi");
        const data = await res.json();
        showToast(data.message || "Seluruh kelas berhasil di-reset ke Soal 1!", "success");
        if (typeof closeManageModal === "function") closeManageModal();
        await loadSessions();
        await refreshAmbientState();
      } catch (err) {
        showToast("Gagal me-reset sesi: " + err.message, "error");
      }
    }
  });
}

function quickResetStudent(studentCode) {
  if (!currentSessionId) return;
  openConfirmModal({
    title: `Ulangi pengerjaan ${studentCode}?`,
    body: `${studentCode} akan mulai lagi dari Soal 1 pada sesi ini. Riwayat jawaban lama tetap tersimpan untuk audit.`,
    okLabel: "Ya, ulangi",
    onConfirm: async () => {
      try {
        const res = await fetch(`${API_BASE}/api/sessions/${currentSessionId}/reset-student/${studentCode}`, { method: "POST" });
        if (!res.ok) throw new Error("Gagal me-reset siswa");
        showToast(`Siswa ${studentCode} berhasil di-reset ke Soal 1!`, "success");
        await loadSessions();
        await refreshAmbientState();
      } catch (err) {
        showToast("Gagal: " + err.message, "error");
      }
    }
  });
}

// Mastery level vocabulary: teachers read words, not 0.25 decimals
const LEVELS = [
  { max: 0.35, label: "Belum paham", cell: "bg-cardinal text-white", text: "text-cardinal-shade", bar: "bg-cardinal" },
  { max: 0.55, label: "Berkembang",  cell: "bg-bee text-eel",        text: "text-fox",            bar: "bg-bee" },
  { max: 0.75, label: "Cakap",       cell: "bg-mask text-[#224100]", text: "text-feather-shade",  bar: "bg-mask" },
  { max: 1.01, label: "Mahir",       cell: "bg-feather text-white",  text: "text-feather-shade",  bar: "bg-feather" }
];

function masteryLevel(m) {
  return LEVELS.find(l => m < l.max) || LEVELS[LEVELS.length - 1];
}

function pct(m) {
  return `${Math.round(m * 100)}%`;
}

function connectWebSocket() {
  try {
    ws = new WebSocket(WS_URL);

    ws.onopen = () => {
      setConnectionStatus(true, "Tersambung");
      if (fallbackPollTimer) {
        clearInterval(fallbackPollTimer);
        fallbackPollTimer = null;
      }
      if (pingTimer) clearInterval(pingTimer);
      pingTimer = setInterval(() => {
        if (ws && ws.readyState === WebSocket.OPEN) {
          ws.send("ping");
        }
      }, 20000);
    };

    ws.onmessage = (event) => {
      if (event.data === "pong") return;
      try {
        const data = JSON.parse(event.data);
        if (!currentSessionId || !data.session_id || data.session_id === currentSessionId) {
          renderAmbientState(data);
        }
      } catch (e) {
        console.error("Error parsing WebSocket JSON:", e);
      }
    };

    ws.onclose = () => {
      if (pingTimer) {
        clearInterval(pingTimer);
        pingTimer = null;
      }
      if (typeof teacherAuthed !== "undefined" && !teacherAuthed) return; // logged out: stay quiet
      setConnectionStatus(false, "Mode Polling");
      startPollingFallback();
      setTimeout(connectWebSocket, 3000);
    };

    ws.onerror = (err) => {
      if (pingTimer) {
        clearInterval(pingTimer);
        pingTimer = null;
      }
      console.error("[LogiTrace Ambient] WebSocket error:", err);
      ws.close();
    };
  } catch (err) {
    console.error("Failed to initiate WebSocket:", err);
    startPollingFallback();
  }
}

function setConnectionStatus(connected, text) {
  const ind = document.getElementById("ws-indicator");
  const label = document.getElementById("ws-status-text");
  if (connected) {
    ind.className = "w-2.5 h-2.5 rounded-full bg-feather";
    label.textContent = text;
  } else {
    ind.className = "w-2.5 h-2.5 rounded-full bg-bee";
    label.textContent = text;
  }
}

function startPollingFallback() {
  if (!fallbackPollTimer) {
    refreshAmbientState();
    fallbackPollTimer = setInterval(refreshAmbientState, 5000);
  }
}

async function refreshAmbientState() {
  try {
    const url = currentSessionId
      ? `${API_BASE}/api/teacher/ambient?session_id=${encodeURIComponent(currentSessionId)}`
      : `${API_BASE}/api/teacher/ambient`;
    const resp = await fetch(url);
    if (!resp.ok) throw new Error("Gagal mengambil status ambient");
    const data = await resp.json();
    renderAmbientState(data);
  } catch (err) {
    console.error("Error refreshing ambient state:", err);
  }
}

let lastState = null;
let showAllKc = false;

function renderAmbientState(state) {
  lastState = state;

  if (state.session_title) {
    document.getElementById("banner-session-title").textContent = state.session_title;
    document.getElementById("banner-session-code").textContent = `Sesi ${state.session_number || 1}`;
  }
  updateBannerTag();

  const totalStudents = state.active_students_count || 0;
  const comp = state.completed_count || 0;
  const inProg = state.in_progress_count || 0;
  const notStart = state.not_started_count !== undefined && state.not_started_count !== null
    ? state.not_started_count
    : Math.max(0, totalStudents - comp - inProg);
  const total = comp + inProg + notStart || 1;

  document.getElementById("class-subtitle").textContent = `${state.class_rombel || "XI TKJ 1"} · ${totalStudents} siswa`;
  document.getElementById("badge-completed").textContent = comp;
  document.getElementById("badge-in-progress").textContent = inProg;
  document.getElementById("badge-not-started").textContent = notStart;

  const pComp = (comp / total) * 100;
  const pInProg = (inProg / total) * 100;
  document.getElementById("progbar-completed").style.width = `${pComp}%`;
  document.getElementById("progbar-in-progress").style.width = `${pInProg}%`;
  document.getElementById("progbar-not-started").style.width = `${Math.max(0, 100 - pComp - pInProg)}%`;

  const stuck = state.top_stuck_students || [];
  const cells = state.heatmap || [];
  const tested = cells.filter(c => c.confidence !== "low");

  // KPI: perlu dibantu
  const stuckEl = document.getElementById("stat-stuck-count");
  stuckEl.textContent = stuck.length;
  stuckEl.className = `kpi-value ${stuck.length > 0 ? "text-cardinal-shade" : "text-eel"}`;

  // KPI: penguasaan kelas, only from answered (high-confidence) cells
  const avgEl = document.getElementById("stat-avg-mastery");
  const avgSub = document.getElementById("stat-avg-mastery-sub");
  if (tested.length === 0) {
    avgEl.textContent = "—";
    avgEl.className = "kpi-value text-wolf";
    avgSub.textContent = "belum ada jawaban";
  } else {
    const avg = tested.reduce((a, c) => a + c.mastery, 0) / tested.length;
    const lvl = masteryLevel(avg);
    avgEl.textContent = pct(avg);
    avgEl.className = `kpi-value ${lvl.text}`;
    avgSub.textContent = lvl.label;
  }

  document.getElementById("status-headline").textContent =
    buildHeadline({ totalStudents, comp, inProg, notStart, stuckCount: stuck.length });

  renderTopStuck(stuck);
  renderKcSummary(cells);
  renderHeatmap(cells);
}

function buildHeadline({ totalStudents, comp, inProg, notStart, stuckCount }) {
  if (comp + inProg === 0) {
    return `Belum ada siswa yang mulai. Data muncul otomatis saat ${totalStudents} siswa mulai menjawab.`;
  }
  const parts = [];
  if (inProg > 0) parts.push(`${inProg} siswa sedang mengerjakan`);
  if (comp > 0) parts.push(`${comp} sudah selesai`);
  if (notStart > 0) parts.push(`${notStart} belum mulai`);
  let line = parts.join(", ") + ".";
  line += stuckCount > 0
    ? ` ${stuckCount} siswa perlu Anda datangi sekarang.`
    : " Belum ada yang tersendat.";
  return line.charAt(0).toUpperCase() + line.slice(1);
}

function renderTopStuck(stuckStudents) {
  const container = document.getElementById("top-stuck-container");
  container.innerHTML = "";

  if (stuckStudents.length === 0) {
    container.innerHTML = `
      <div class="col-span-full flex items-center gap-3 bg-polar border-2 border-swan rounded-2xl px-4 py-3">
        <span class="w-7 h-7 rounded-full bg-feather-soft flex items-center justify-center flex-shrink-0">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 13l4 4L19 7" stroke="#46A302" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
        <p class="text-sm font-bold text-eel">Tidak ada siswa yang tersendat. <span class="text-wolf">Anda bebas berkeliling atau fokus ke zona lain.</span></p>
      </div>`;
    return;
  }

  stuckStudents.forEach((s, idx) => {
    const kc = KC_BY_ID[s.stuck_kc_id];
    const topic = kc ? kc.name : s.stuck_kc_name;
    const card = document.createElement("article");
    card.className = "bg-polar rounded-3xl p-5 border-2 border-cardinal/40 border-b-[5px] flex flex-col gap-3";
    card.innerHTML = `
      <div class="flex items-center justify-between">
        <span class="font-display text-2xl font-extrabold text-eel leading-none">${escapeHtml(s.student_code)}</span>
        <span class="px-2.5 py-0.5 rounded-full text-xs font-num font-bold bg-cardinal-soft text-cardinal-shade">#${idx + 1}</span>
      </div>
      <p class="text-sm font-bold text-wolf leading-snug">
        Salah <strong class="text-cardinal-shade">${s.consecutive_errors}× berturut</strong> di topik
        <strong class="text-eel">${escapeHtml(topic)}</strong>
      </p>
      <div class="p-3 bg-macaw-soft/60 rounded-2xl text-sm text-eel">
        <p class="font-extrabold text-[11px] text-macaw-shade uppercase mb-0.5">Yang bisa Anda lakukan</p>
        <p class="font-bold leading-relaxed">${escapeHtml(s.recommended_action)}</p>
      </div>
      <div class="flex items-center justify-between text-xs mt-auto pt-1">
        <span class="font-bold text-wolf">Penguasaan topik: ${pct(s.current_mastery)}</span>
        <button type="button" class="btn-quick-reset font-extrabold text-wolf hover:text-cardinal-shade transition" title="Reset siswa ini ke Soal 1">&#8634; Reset</button>
      </div>
    `;
    card.querySelector(".btn-quick-reset").onclick = () => quickResetStudent(s.student_code);
    container.appendChild(card);
  });
}

function renderKcSummary(cells) {
  const list = document.getElementById("kc-summary-list");
  const toggle = document.getElementById("kc-toggle-btn");

  const agg = KC_META.map(k => ({ ...k, n: 0, sum: 0, weak: 0 }));
  const byId = Object.fromEntries(agg.map(a => [a.id, a]));
  cells.forEach(c => {
    if (c.confidence === "low") return;
    const a = byId[c.kc_id];
    if (!a) return;
    a.n++;
    a.sum += c.mastery;
    if (c.mastery < 0.35) a.weak++;
  });

  const answered = agg.filter(a => a.n > 0).map(a => ({ ...a, avg: a.sum / a.n }));
  if (answered.length === 0) {
    list.innerHTML = `<p class="text-sm font-bold text-wolf">Belum ada jawaban masuk. Daftar topik terisi otomatis setelah siswa mulai menjawab.</p>`;
    toggle.classList.add("hidden");
    return;
  }

  answered.sort((x, y) => x.avg - y.avg);
  const LIMIT = 5;
  const shown = showAllKc ? answered : answered.slice(0, LIMIT);

  list.innerHTML = shown.map(a => {
    const lvl = masteryLevel(a.avg);
    return `
      <div class="grid grid-cols-[1fr_auto] sm:grid-cols-[minmax(0,260px)_1fr_auto] items-center gap-x-4 gap-y-1">
        <div class="min-w-0">
          <p class="text-sm font-extrabold text-eel truncate" title="${escapeHtml(a.name)}">${escapeHtml(a.name)}</p>
          <p class="text-[11px] font-bold text-wolf">${a.weak > 0 ? `${a.weak} dari ${a.n} siswa belum paham` : `${a.n} siswa sudah menjawab`}</p>
        </div>
        <div class="hidden sm:block h-3 bg-swan rounded-full overflow-hidden">
          <div class="${lvl.bar} h-full spring-bar" style="width:${Math.max(4, a.avg * 100)}%"></div>
        </div>
        <div class="text-right min-w-[84px]">
          <span class="font-num font-bold text-sm tabular-nums ${lvl.text}">${pct(a.avg)}</span>
          <span class="block text-[11px] font-bold text-wolf">${lvl.label}</span>
        </div>
      </div>`;
  }).join("");

  if (answered.length > LIMIT) {
    toggle.classList.remove("hidden");
    toggle.textContent = showAllKc ? "Tampilkan 5 terlemah saja" : `Tampilkan semua ${answered.length} topik`;
  } else {
    toggle.classList.add("hidden");
  }
  const untouched = KC_META.length - answered.length;
  if (untouched > 0) {
    list.insertAdjacentHTML("beforeend",
      `<p class="text-[11px] font-bold text-wolf pt-1">${untouched} topik lain belum dijawab siswa.</p>`);
  }
}

function toggleAllKc() {
  showAllKc = !showAllKc;
  if (lastState) renderKcSummary(lastState.heatmap || []);
}

function rerenderHeatmap() {
  if (lastState) renderHeatmap(lastState.heatmap || []);
}

function renderHeatmap(heatmapCells) {
  const thead = document.getElementById("heatmap-head");
  const tbody = document.getElementById("heatmap-body");
  const showNum = document.getElementById("heatmap-show-num").checked;
  const sortMode = document.getElementById("heatmap-sort").value;

  thead.innerHTML = `
    <tr class="border-b-2 border-swan text-[11px] font-bold text-wolf bg-snow">
      <th class="w-24 p-2.5 text-left sticky left-0 bg-snow z-10 border-r-2 border-swan text-eel font-extrabold">Siswa</th>
      ${KC_META.map(k => `
        <th class="px-1 py-2 font-sans" title="${escapeHtml(k.name)}">
          <span class="block font-num text-[10px] text-hare">${k.code}</span>
          <span class="block text-eel truncate">${k.short}</span>
        </th>`).join("")}
      <th class="w-20 p-2.5 border-l-2 border-swan text-eel font-extrabold">Rerata</th>
      <th class="w-12 p-2.5 border-l-2 border-swan"><span class="sr-only">Aksi</span></th>
    </tr>`;

  const studentMap = {};
  heatmapCells.forEach(cell => {
    (studentMap[cell.student_code] ||= {})[cell.kc_id] = cell;
  });

  const rows = Object.keys(studentMap).map(code => {
    const tested = KC_KEYS.map(k => studentMap[code][k]).filter(c => c && c.confidence !== "low");
    const avg = tested.length ? tested.reduce((a, c) => a + c.mastery, 0) / tested.length : null;
    return { code, avg };
  });

  if (sortMode === "need") {
    // Answered students with lowest mastery first; students with no answers last
    rows.sort((a, b) => {
      if (a.avg === null && b.avg === null) return a.code.localeCompare(b.code);
      if (a.avg === null) return 1;
      if (b.avg === null) return -1;
      return a.avg - b.avg;
    });
  } else {
    rows.sort((a, b) => a.code.localeCompare(b.code));
  }

  document.getElementById("heatmap-subtitle").textContent =
    `${rows.length} siswa × ${KC_META.length} topik. Buka bila perlu menelusuri siswa tertentu.`;

  tbody.innerHTML = "";
  rows.forEach(({ code, avg }) => {
    const safeCode = escapeHtml(code);
    const tr = document.createElement("tr");
    tr.className = "hover:bg-snow/70 transition";

    let html = `<td class="p-2.5 text-left font-bold text-eel text-xs font-num sticky left-0 bg-polar border-r-2 border-swan z-10">${safeCode}</td>`;

    KC_META.forEach(k => {
      const cell = studentMap[code][k.id];
      if (!cell || cell.confidence === "low") {
        html += `<td class="p-1"><div class="h-7 rounded-lg cell-untested" title="${safeCode} · ${escapeHtml(k.name)}: belum dijawab"></div></td>`;
        return;
      }
      const lvl = masteryLevel(cell.mastery);
      html += `
        <td class="p-1">
          <div class="h-7 rounded-lg flex items-center justify-center text-[11px] font-num font-extrabold ${lvl.cell}"
               title="${safeCode} · ${escapeHtml(k.name)}: ${lvl.label} (${pct(cell.mastery)})">${showNum ? pct(cell.mastery) : ""}</div>
        </td>`;
    });

    const avgHtml = avg === null
      ? `<span class="text-hare">—</span>`
      : `<span class="${masteryLevel(avg).text}">${pct(avg)}</span>`;
    html += `
      <td class="p-2.5 font-num font-bold tabular-nums text-xs border-l-2 border-swan">${avgHtml}</td>
      <td class="p-1 border-l-2 border-swan">
        <button type="button" class="btn-quick-reset p-1.5 text-hare hover:text-cardinal transition font-extrabold" title="Reset siswa ${safeCode} ke Soal 1" aria-label="Reset siswa ${safeCode}">&#8634;</button>
      </td>`;

    tr.innerHTML = html;
    tr.querySelector(".btn-quick-reset").onclick = () => quickResetStudent(code);
    tbody.appendChild(tr);
  });
}

// Initialization after DOM + modals.js are loaded
// Startup lives in auth.js (bootTeacher): the dashboard loads only after the teacher logs in.
