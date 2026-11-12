const API_BASE = window.location.origin;
const WS_URL = `${window.location.protocol === "https:" ? "wss:" : "ws:"}//${window.location.host}/api/teacher/ws/ambient`;

const KC_KEYS = [
  "WLAN_STANDARDS",
  "WLAN_TOPOLOGY_BSS",
  "IP_PEER_CONFIG",
  "WLAN_FREQ_CHANNEL",
  "WLAN_SECURITY_AUTH",
  "WLAN_HOST_HARDENING",
  "WLAN_SIGNAL_PROP",
  "WLAN_ROAMING_PROB",
  "WLAN_CHANNEL_COLLISION",
  "ICMP_CONNECTIVITY",
  "ICMP_TROUBLE_DHU",
  "ICMP_TROUBLE_RTO"
];

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

    const select = document.getElementById("teacher-session-select");
    select.innerHTML = "";

    if (sessionsList.length === 0) {
      select.innerHTML = `<option value="">Belum ada tugas</option>`;
      return;
    }

    if (!currentSessionId) {
      const active = sessionsList.find(s => s.is_active);
      currentSessionId = active ? active.id : sessionsList[0].id;
    }

    sessionsList.forEach(s => {
      const opt = document.createElement("option");
      opt.value = s.id;
      opt.className = "bg-polar text-eel";
      opt.textContent = `${s.title} ${s.is_active ? "★ (Aktif)" : ""}`;
      if (s.id === currentSessionId) opt.selected = true;
      select.appendChild(opt);
    });

    if (typeof renderSessionCardsInModal === "function") {
      renderSessionCardsInModal();
    }
  } catch (err) {
    console.error("Error loading sessions:", err);
  }
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
    title: "Reset Seluruh Kelas (34 Siswa)?",
    body:
      "• Seluruh siswa pada sesi ini akan dimulai kembali dari Soal 1.\n" +
      "• Estimasi penguasaan dikembalikan ke baseline awal (0.25).\n" +
      "• Log interaksi sebelumnya tetap tersimpan aman di tabel audit append-only.",
    okLabel: "Ya, Reset Kelas",
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
    title: `Reset Siswa ${studentCode}?`,
    body: `Kembalikan pengerjaan siswa ${studentCode} pada sesi ini ke Soal 1?`,
    okLabel: "Ya, Reset Siswa",
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

// Light Tactile Heatmap Color Scale
function getMasteryColor(m) {
  if (m < 0.35) {
    return "bg-cardinal text-white font-extrabold";
  } else if (m < 0.55) {
    return "bg-bee text-eel font-extrabold";
  } else if (m < 0.75) {
    return "bg-mask text-[#224100] font-extrabold";
  } else {
    return "bg-feather text-white font-extrabold";
  }
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

function renderAmbientState(state) {
  if (state.session_title) {
    document.getElementById("banner-session-title").textContent = state.session_title;
    document.getElementById("banner-session-code").textContent = `Sesi ${state.session_number || 1}`;
  }

  const comp = state.completed_count || 0;
  const inProg = state.in_progress_count || 0;
  const notStart = state.not_started_count !== undefined ? state.not_started_count : 34;
  const total = comp + inProg + notStart || 34;

  document.getElementById("badge-completed").textContent = comp;
  document.getElementById("badge-in-progress").textContent = inProg;
  document.getElementById("badge-not-started").textContent = notStart;

  const pComp = Math.round((comp / total) * 100);
  const pInProg = Math.round((inProg / total) * 100);
  const pNotStart = Math.max(0, 100 - pComp - pInProg);

  document.getElementById("progbar-completed").style.width = `${pComp}%`;
  document.getElementById("progbar-in-progress").style.width = `${pInProg}%`;
  document.getElementById("progbar-not-started").style.width = `${pNotStart}%`;

  document.getElementById("stat-active-students").textContent = state.active_students_count || 34;
  document.getElementById("stat-avg-mastery").textContent = (state.class_average_mastery || 0.25).toFixed(3);

  const stuckCount = state.top_stuck_students ? state.top_stuck_students.length : 0;
  document.getElementById("stat-stuck-count").textContent = stuckCount;

  renderTopStuck(state.top_stuck_students || []);
  renderHeatmap(state.heatmap || []);
}

function renderTopStuck(stuckStudents) {
  const container = document.getElementById("top-stuck-container");
  container.innerHTML = "";

  if (stuckStudents.length === 0) {
    container.innerHTML = `
      <div class="col-span-3 bg-feather-soft border-2 border-feather/40 rounded-3xl p-6 text-center space-y-1">
        <div class="w-10 h-10 rounded-full bg-feather text-white flex items-center justify-center mx-auto mb-2">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M5 13l4 4L19 7" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <h4 class="font-display font-extrabold text-lg text-feather-shade">Semua Siswa Lancar</h4>
        <p class="text-xs font-sans font-bold text-eel">Belum ada siswa yang mengalami kesulitan berulang pada sesi ini.</p>
      </div>
    `;
    return;
  }

  stuckStudents.forEach((s, idx) => {
    const safeCode = escapeHtml(s.student_code);
    const card = document.createElement("div");
    card.className = "bg-polar rounded-3xl p-5 border-2 border-cardinal/40 border-b-[5px] flex flex-col justify-between gap-3";
    card.innerHTML = `
      <div>
        <div class="flex items-center justify-between mb-2.5">
          <span class="px-2.5 py-0.5 rounded-full text-xs font-num font-bold bg-cardinal-soft text-cardinal-shade">
            Prioritas #${idx + 1}
          </span>
          <span class="text-xs font-num font-bold px-2.5 py-0.5 rounded-xl bg-snow text-eel border-2 border-swan">
            ${safeCode}
          </span>
        </div>

        <h4 class="font-display font-extrabold text-base text-eel leading-snug">
          ${escapeHtml(s.stuck_kc_name)}
        </h4>
        <p class="text-[11px] font-num font-semibold text-macaw-shade mb-3">${escapeHtml(s.stuck_kc_id)}</p>

        <div class="grid grid-cols-2 gap-2 text-xs font-num mb-3 bg-snow p-2.5 rounded-2xl border border-swan">
          <div>
            <span class="text-wolf font-sans block text-[10px] font-bold">Penguasaan:</span>
            <span class="font-bold text-cardinal-shade tabular-nums">${s.current_mastery.toFixed(2)}</span>
          </div>
          <div>
            <span class="text-wolf font-sans block text-[10px] font-bold">Salah Beruntun:</span>
            <span class="font-bold text-fox tabular-nums">${s.consecutive_errors}x</span>
          </div>
        </div>

        <div class="p-3 bg-macaw-soft/50 border border-macaw/30 rounded-2xl text-xs text-eel space-y-1">
          <p class="font-sans font-extrabold text-[10px] text-macaw-shade uppercase">Saran Bantuan:</p>
          <p class="text-xs font-bold leading-relaxed">${escapeHtml(s.recommended_action)}</p>
        </div>
      </div>

      <div class="pt-2.5 border-t-2 border-swan flex items-center justify-end">
        <button type="button" class="btn-quick-reset text-xs font-sans text-cardinal-shade hover:underline font-extrabold transition" title="Reset siswa ini ke Soal 1">
          &#8634; Reset Siswa
        </button>
      </div>
    `;
    const resetBtn = card.querySelector(".btn-quick-reset");
    if (resetBtn) {
      resetBtn.onclick = () => quickResetStudent(s.student_code);
    }
    container.appendChild(card);
  });
}

function renderHeatmap(heatmapCells) {
  const tbody = document.getElementById("heatmap-body");
  tbody.innerHTML = "";

  const studentMap = {};
  heatmapCells.forEach(cell => {
    if (!studentMap[cell.student_code]) {
      studentMap[cell.student_code] = {};
    }
    studentMap[cell.student_code][cell.kc_id] = cell;
  });

  const studentCodes = Object.keys(studentMap).sort();

  studentCodes.forEach(stdCode => {
    const safeCode = escapeHtml(stdCode);
    const tr = document.createElement("tr");
    tr.className = "hover:bg-snow/70 transition";

    let rowHtml = `
      <td class="p-2.5 text-left font-bold text-eel text-xs font-num sticky left-0 bg-polar border-r-2 border-swan z-10">
        ${safeCode}
      </td>
    `;

    let studentSum = 0;
    let count = 0;

    KC_KEYS.forEach(kc => {
      const cell = studentMap[stdCode] ? studentMap[stdCode][kc] : null;
      const m = cell ? cell.mastery : 0.25;
      const conf = cell ? cell.confidence : "low";
      studentSum += m;
      count++;

      const colorClass = getMasteryColor(m);
      const lowConfClass = conf === "low" ? "striped-low-conf" : "";

      rowHtml += `
        <td class="p-1">
          <div class="h-7 w-full rounded-lg flex items-center justify-center text-[11px] font-num tabular-nums ${colorClass} ${lowConfClass} cursor-pointer hover:ring-2 hover:ring-macaw transition"
               title="${safeCode} • ${kc}: m = ${m.toFixed(2)} (${conf === "low" ? "Estimasi Prasyarat" : "Terkonfirmasi"})">
            ${m.toFixed(2)}
          </div>
        </td>
      `;
    });

    const stdAvg = count > 0 ? (studentSum / count).toFixed(2) : "0.25";
    rowHtml += `
      <td class="p-2.5 font-num font-bold tabular-nums text-xs border-l-2 border-swan bg-polar text-eel">${stdAvg}</td>
      <td class="p-1 border-l-2 border-swan bg-snow">
        <button type="button" class="btn-quick-reset p-1.5 text-wolf hover:text-cardinal transition font-extrabold" title="Reset siswa ${safeCode} ke Soal 1" aria-label="Reset siswa ${safeCode}">
          &#8634;
        </button>
      </td>
    `;

    tr.innerHTML = rowHtml;
    const resetBtn = tr.querySelector(".btn-quick-reset");
    if (resetBtn) {
      resetBtn.onclick = () => quickResetStudent(stdCode);
    }
    tbody.appendChild(tr);
  });
}

// Initialization after DOM + modals.js are loaded
document.addEventListener("DOMContentLoaded", () => {
  loadSessions();
  connectWebSocket();
  refreshAmbientState();
});
