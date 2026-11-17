let currentSummaryData = null;

// Kelola modal: visibility & tabs. "Sesi" is the default tab; destructive actions never open first.
function openManageModal() {
  document.getElementById("modal-manage").classList.remove("hidden");
  toggleCreateForm(false);
  switchModalTab("list");
  loadSessions();
  loadReviewQueue(); // also refreshes the "Cek soal" badge
}

function closeManageModal() {
  document.getElementById("modal-manage").classList.add("hidden");
}

function switchModalTab(tab) {
  const tabs = {
    list: { content: "tab-content-list", btn: "tab-btn-list" },
    reset: { content: "tab-content-reset", btn: "tab-btn-reset" },
    labeler: { content: "tab-content-labeler", btn: "tab-btn-labeler" }
  };
  if (tab === "create") { tab = "list"; toggleCreateForm(true); }
  const active = tabs[tab];
  if (!active) return;

  Object.entries(tabs).forEach(([key, t]) => {
    document.getElementById(t.content).classList.toggle("hidden", key !== tab);
    document.getElementById(t.btn).setAttribute("aria-selected", key === tab ? "true" : "false");
  });

  if (tab === "list") renderSessionCardsInModal();
  if (tab === "reset") prepareResetTab();
  if (tab === "labeler") loadReviewQueue();
}

// Agent T3 Summary Modal Handlers
async function openSummaryModal() {
  const modal = document.getElementById("modal-summary");
  modal.classList.remove("hidden");
  document.getElementById("summary-loading").classList.remove("hidden");
  document.getElementById("summary-loading").innerHTML = `
    <div class="w-9 h-9 border-4 border-swan border-t-feather rounded-full animate-spin"></div>
    <p class="text-xs font-sans font-bold text-wolf">Menyusun ringkasan kelas...</p>
  `;
  document.getElementById("summary-content").classList.add("hidden");

  try {
    const url = currentSessionId
      ? `${API_BASE}/api/teacher/session-summary?session_id=${encodeURIComponent(currentSessionId)}`
      : `${API_BASE}/api/teacher/session-summary`;
    const res = await fetch(url);
    if (!res.ok) throw new Error("Gagal mengambil ringkasan sesi");
    currentSummaryData = await res.json();
    renderSessionSummary(currentSummaryData);
  } catch (err) {
    showToast("Gagal memuat ringkasan sesi: " + err.message, "error");
    document.getElementById("summary-loading").innerHTML = `
      <div class="text-center text-cardinal-shade p-4 space-y-1">
        <p class="font-display text-lg font-extrabold">Gagal menghasilkan ringkasan sesi</p>
        <p class="text-xs text-wolf font-sans font-bold">${escapeHtml(err.message)}</p>
      </div>
    `;
  }
}

function closeSummaryModal() {
  document.getElementById("modal-summary").classList.add("hidden");
}

const WEAK_TOPIC_MAX = 0.55;   // below this a topic is worth re-teaching
const STRONG_TOPIC_MIN = 0.75; // at/above this a topic counts as mastered by the class

function isTeacherGroup(pt) {
  return String(pt.tutor_student_code || "").startsWith("Guru");
}

// Backend narrative uses research notation; translate it for teachers
function humanizeNarrative(text) {
  return String(text || "")
    .replace(/m\s*=\s*(0?\.\d+|1(?:\.0+)?)/g, (_, v) => pct(parseFloat(v)))
    .replace(/\bKC\b/g, "topik")
    .replace(/peserta didik/g, "siswa");
}

function renderSessionSummary(data) {
  document.getElementById("summary-loading").classList.add("hidden");
  document.getElementById("summary-content").classList.remove("hidden");

  const pill = document.getElementById("summary-source-pill");
  if (pill) {
    pill.textContent = data.source === "llm_9router" ? "Disusun AI" : "Otomatis";
    pill.title = `Disusun dalam ${data.latency_ms} ms`;
  }

  document.getElementById("sum-session-line").textContent = `${data.session_title} · ${data.class_rombel}`;

  // A. Kondisi kelas
  const total = data.total_students || 0;
  const done = data.completed_students || 0;
  const started = done + (data.in_progress_students || 0);
  document.getElementById("sum-completion").textContent = `${done}/${total}`;
  document.getElementById("sum-completion-sub").textContent = data.in_progress_students
    ? `${data.in_progress_students} masih mengerjakan` : "siswa";
  document.getElementById("sum-accuracy").textContent = pct(data.accuracy_rate || 0);
  document.getElementById("sum-total-resp").textContent = `dari ${data.total_responses} soal dijawab`;

  const avgEl = document.getElementById("sum-avg-mastery");
  const avgLvl = document.getElementById("sum-avg-level");
  if (data.total_responses > 0) {
    const lvl = masteryLevel(data.class_avg_mastery);
    avgEl.textContent = pct(data.class_avg_mastery);
    avgEl.className = `kpi-value ${lvl.text}`;
    avgLvl.textContent = lvl.label;
  } else {
    avgEl.textContent = "—";
    avgEl.className = "kpi-value text-wolf";
    avgLvl.textContent = "belum ada jawaban";
  }

  const warn = document.getElementById("sum-coverage-warning");
  if (total > 0 && started / total < 0.5) {
    warn.classList.remove("hidden");
    warn.innerHTML = `<span aria-hidden="true">&#9888;</span><span>Baru <b>${started} dari ${total} siswa</b> yang mengerjakan. Ringkasan ini belum mewakili seluruh kelas; buka lagi setelah lebih banyak siswa selesai.</span>`;
  } else {
    warn.classList.add("hidden");
  }

  // B. Topik
  const weak = (data.bottlenecks || []).filter(b => b.avg_mastery < WEAK_TOPIC_MAX);
  const btnBox = document.getElementById("sum-bottlenecks-list");
  if (weak.length === 0) {
    btnBox.innerHTML = `<p class="text-sm font-bold text-wolf px-1">Tidak ada topik yang lemah. Lanjutkan ke materi berikutnya.</p>`;
  } else {
    btnBox.innerHTML = weak.map(b => {
      const lvl = masteryLevel(b.avg_mastery);
      return `
        <div class="flex items-center justify-between gap-3 p-3 rounded-2xl border-2 border-cardinal/30 bg-cardinal-soft/40">
          <div class="min-w-0">
            <p class="text-sm font-extrabold text-eel">${escapeHtml(b.kc_name)}</p>
            <p class="text-[11px] font-bold text-wolf">${b.struggling_count} dari ${b.student_count} siswa belum paham</p>
          </div>
          <div class="text-right flex-shrink-0">
            <span class="font-num font-bold text-base ${lvl.text}">${pct(b.avg_mastery)}</span>
            <span class="block text-[11px] font-bold text-wolf">${lvl.label}</span>
          </div>
        </div>`;
    }).join("");
  }

  const strong = (data.strengths || []).filter(s => s.avg_mastery >= STRONG_TOPIC_MIN);
  document.getElementById("sum-strengths-list").innerHTML = strong.length
    ? strong.map(s => `<span class="px-3 py-1 rounded-full bg-feather-soft text-feather-shade text-xs font-extrabold border border-feather/30" title="${s.mastered_count} dari ${s.student_count} siswa mahir">&#10003; ${escapeHtml(s.kc_name)} · ${pct(s.avg_mastery)}</span>`).join("")
    : `<span class="text-xs font-bold text-wolf">Belum ada topik yang dikuasai kelas.</span>`;

  // C. Kelompok belajar
  const peerBox = document.getElementById("sum-peer-tutoring-cards");
  const groups = data.peer_tutoring_recommendations || [];
  if (groups.length === 0) {
    peerBox.innerHTML = `<p class="p-4 rounded-2xl bg-snow border-2 border-swan text-sm font-bold text-wolf">Tidak perlu kelompok belajar: belum ada siswa yang tertinggal pada topik terlemah.</p>`;
  } else {
    const chip = (code, cls) => `<span class="px-2.5 py-1 rounded-xl font-num text-sm font-bold ${cls}">${escapeHtml(code)}</span>`;
    peerBox.innerHTML = groups.map((pt, i) => {
      const mentees = pt.mentee_student_codes.map(c => chip(c, "bg-bee-soft text-eel border-2 border-bee/60")).join("");
      const teacher = isTeacherGroup(pt);
      const leader = teacher
        ? `<div class="flex flex-col items-start gap-1">
             <span class="text-[11px] font-extrabold uppercase text-cardinal-shade">Dibimbing oleh</span>
             <span class="px-2.5 py-1 rounded-xl text-sm font-extrabold bg-cardinal-soft text-cardinal-shade border-2 border-cardinal/30">Anda (guru)</span>
           </div>`
        : `<div class="flex flex-col items-start gap-1">
             <span class="text-[11px] font-extrabold uppercase text-feather-shade">Teman pengajar</span>
             <span class="flex items-center gap-1.5">${chip(pt.tutor_student_code, "bg-feather-soft text-feather-shade border-2 border-feather/40")}<span class="text-[11px] font-bold text-wolf">${pct(pt.tutor_mastery)}</span></span>
           </div>`;
      const note = teacher
        ? `Belum ada siswa yang menguasai topik ini, jadi kelompok ini perlu Anda dampingi langsung.`
        : `Minta ${escapeHtml(pt.tutor_student_code)} menjelaskan ulang konsep inti, lalu temannya mencoba soal serupa.`;
      return `
        <article class="p-4 rounded-2xl border-2 ${teacher ? "border-cardinal/30" : "border-swan"} border-b-4 space-y-3">
          <div class="flex items-center justify-between gap-2">
            <p class="text-sm font-extrabold text-eel"><span class="text-wolf">Kelompok ${i + 1} ·</span> ${escapeHtml(pt.kc_name)}</p>
          </div>
          <div class="flex flex-wrap items-end gap-3">
            ${leader}
            <span class="text-hare text-xl font-extrabold pb-1" aria-hidden="true">&rarr;</span>
            <div class="flex flex-col items-start gap-1">
              <span class="text-[11px] font-extrabold uppercase text-fox">Yang dibantu</span>
              <span class="flex flex-wrap items-center gap-1.5">${mentees}<span class="text-[11px] font-bold text-wolf">rata-rata ${pct(pt.mentee_avg_mastery)}</span></span>
            </div>
          </div>
          <p class="text-xs font-bold text-wolf leading-relaxed">${note}</p>
        </article>`;
    }).join("");
  }

  // D. Catatan lengkap
  const narrativeBox = document.getElementById("sum-narrative-text");
  narrativeBox.innerHTML = "";
  humanizeNarrative(data.narrative_summary).split(/\n\n+/).forEach(p => {
    if (!p.trim()) return;
    const pEl = document.createElement("p");
    pEl.textContent = p.trim();
    narrativeBox.appendChild(pEl);
  });
}

function buildSummaryExportText(includeTimestamp) {
  const d = currentSummaryData;
  const tsLine = includeTimestamp ? `Waktu ekspor: ${new Date().toLocaleString("id-ID")}\n` : "";
  const weak = (d.bottlenecks || []).filter(b => b.avg_mastery < WEAK_TOPIC_MAX);
  const groups = (d.peer_tutoring_recommendations || []).map((pt, i) => {
    const leader = isTeacherGroup(pt) ? "Guru (bimbingan langsung)" : `${pt.tutor_student_code} (${pct(pt.tutor_mastery)})`;
    return `Kelompok ${i + 1} - ${pt.kc_name}\n  Pengajar : ${leader}\n  Dibantu  : ${pt.mentee_student_codes.join(", ")}`;
  });
  return (
    `RINGKASAN KELAS - LOGITRACE\n` +
    `Sesi: ${d.session_title} (${d.class_rombel})\n` +
    tsLine +
    `Selesai: ${d.completed_students} dari ${d.total_students} siswa\n` +
    `Jawaban benar: ${pct(d.accuracy_rate)} dari ${d.total_responses} soal\n` +
    `Penguasaan rata-rata: ${pct(d.class_avg_mastery)} (${masteryLevel(d.class_avg_mastery).label})\n\n` +
    `TOPIK PERLU DIULANG\n` +
    (weak.length ? weak.map(b => `- ${b.kc_name}: ${pct(b.avg_mastery)}, ${b.struggling_count} dari ${b.student_count} siswa belum paham`).join("\n") : "- Tidak ada") +
    `\n\nKELOMPOK BELAJAR PERTEMUAN BERIKUTNYA\n` +
    (groups.length ? groups.join("\n\n") : "- Tidak diperlukan") +
    `\n\nCATATAN\n${humanizeNarrative(d.narrative_summary)}\n`
  );
}

function copySummaryText() {
  if (!currentSummaryData) return;
  const summaryText = buildSummaryExportText(false);
  if (navigator.clipboard && typeof navigator.clipboard.writeText === "function") {
    navigator.clipboard.writeText(summaryText).then(() => {
      showToast("Ringkasan berhasil disalin!", "success");
    }).catch(() => {
      showToast("Gagal menyalin teks ke clipboard.", "error");
    });
    return;
  }

  // Fallback for non-HTTPS LAN origins where navigator.clipboard is unavailable
  try {
    const tempArea = document.createElement("textarea");
    tempArea.value = summaryText;
    tempArea.setAttribute("readonly", "");
    tempArea.style.position = "fixed";
    tempArea.style.left = "-9999px";
    document.body.appendChild(tempArea);
    tempArea.select();
    const copied = document.execCommand("copy");
    document.body.removeChild(tempArea);
    if (copied) {
      showToast("Ringkasan berhasil disalin!", "success");
    } else {
      showToast("Clipboard tidak tersedia di HTTP. Gunakan tombol 'Unduh .txt'.", "info");
    }
  } catch (err) {
    showToast("Clipboard tidak tersedia di HTTP. Gunakan tombol 'Unduh .txt'.", "info");
  }
}

function downloadSummaryFile() {
  if (!currentSummaryData) return;
  const blob = new Blob([buildSummaryExportText(true)], { type: "text/plain;charset=utf-8" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = `LogiTrace_Ringkasan_${currentSummaryData.session_id}.txt`;
  a.click();
  URL.revokeObjectURL(a.href);
  showToast("Ringkasan berhasil diunduh!", "success");
}

// ---------- Shared helpers for Kelola ----------
const BLOOM_LABELS = {
  C1: "Mengingat", C2: "Memahami", C3: "Menerapkan",
  C4: "Menganalisis", C5: "Mengevaluasi", C6: "Mencipta"
};
const DIFFICULTY_LABELS = { 1: "Mudah", 2: "Sedang", 3: "Sulit" };

function bloomText(code) {
  return code ? `${code} · ${BLOOM_LABELS[code] || ""}`.trim() : "—";
}

function kcName(kcId, fallback) {
  const kc = typeof KC_BY_ID !== "undefined" ? KC_BY_ID[kcId] : null;
  return kc ? kc.name : (fallback || kcId);
}

function formatSessionDate(iso) {
  if (!iso) return "";
  const d = new Date(/[zZ]|[+-]\d\d:\d\d$/.test(iso) ? iso : iso + "Z");
  if (isNaN(d)) return "";
  return d.toLocaleString("id-ID", { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" });
}

function currentSessionLabel() {
  const s = sessionsList.find(x => x.id === currentSessionId);
  if (!s) return "—";
  const dup = sessionsList.filter(x => x.title === s.title).length > 1;
  return dup ? `${s.title} (${formatSessionDate(s.created_at)})` : s.title;
}

// ---------- Tab: Sesi ----------
function toggleCreateForm(show) {
  const form = document.getElementById("form-create-session");
  const btn = document.getElementById("btn-show-create");
  if (!form || !btn) return;
  form.classList.toggle("hidden", !show);
  btn.classList.toggle("hidden", show);
  if (show) {
    const nextNum = sessionsList.reduce((mx, s) => Math.max(mx, s.session_number || 0), 0) + 1;
    document.getElementById("create-session-num").value = Math.min(10, nextNum || 1);
    document.getElementById("create-title").focus();
  }
}

function renderSessionCardsInModal() {
  const container = document.getElementById("modal-session-cards");
  if (!container) return;

  if (sessionsList.length === 0) {
    container.innerHTML = `<p class="text-sm font-bold text-wolf">Belum ada sesi. Buat sesi pertama di bawah.</p>`;
    return;
  }

  const sorted = [...sessionsList].sort((a, b) =>
    (b.is_active - a.is_active) || String(b.created_at).localeCompare(String(a.created_at)));
  const titleCount = {};
  sessionsList.forEach(s => { titleCount[s.title] = (titleCount[s.title] || 0) + 1; });

  container.innerHTML = "";
  sorted.forEach(s => {
    const isViewed = s.id === currentSessionId;
    const total = s.total_students || (s.completed_count + s.in_progress_count + s.not_started_count) || 1;
    const pDone = (s.completed_count / total) * 100;
    const pProg = (s.in_progress_count / total) * 100;

    const chips = [
      s.is_active ? `<span class="px-2 py-0.5 rounded-full text-[11px] font-extrabold bg-feather text-white">Aktif · dikerjakan siswa</span>` : "",
      isViewed ? `<span class="px-2 py-0.5 rounded-full text-[11px] font-extrabold bg-macaw-soft text-macaw-shade">Ditampilkan di dasbor</span>` : ""
    ].join("");

    const card = document.createElement("article");
    card.className = `p-4 rounded-2xl border-2 ${s.is_active ? "border-feather/60 bg-feather-soft/30" : "border-swan bg-polar"} space-y-2.5`;
    card.innerHTML = `
      <div class="flex flex-wrap items-start justify-between gap-2">
        <div class="min-w-0">
          <p class="text-sm font-extrabold text-eel">${escapeHtml(s.title)}</p>
          <p class="text-[11px] font-bold text-wolf mt-0.5">
            Pertemuan ${s.session_number} · ${s.max_items} soal · dibuat ${escapeHtml(formatSessionDate(s.created_at))}
            ${titleCount[s.title] > 1 ? `<span class="text-fox">· judul sama dengan sesi lain</span>` : ""}
          </p>
        </div>
        <div class="flex flex-wrap gap-1.5">${chips}</div>
      </div>
      <div>
        <div class="w-full h-2 bg-swan rounded-full overflow-hidden flex">
          <div class="bg-feather h-full" style="width:${pDone}%"></div>
          <div class="bg-bee h-full" style="width:${pProg}%"></div>
        </div>
        <p class="text-[11px] font-bold text-wolf mt-1">${s.completed_count} selesai · ${s.in_progress_count} mengerjakan · ${s.not_started_count} belum mulai</p>
      </div>
      <div class="flex flex-wrap gap-2 justify-end">
        ${!isViewed ? `<button type="button" data-action="open" class="duo-btn duo-btn-ghost px-3 py-1.5 text-[11px]">Lihat di dasbor</button>` : ""}
        ${!s.is_active ? `<button type="button" data-action="activate" class="duo-btn duo-btn-green px-3 py-1.5 text-[11px]">Jadikan aktif</button>` : ""}
      </div>
    `;
    const actBtn = card.querySelector('[data-action="activate"]');
    if (actBtn) actBtn.onclick = () => confirmActivateSession(s);
    const openBtn = card.querySelector('[data-action="open"]');
    if (openBtn) openBtn.onclick = () => selectAndCloseSession(s.id);
    container.appendChild(card);
  });
}

function selectAndCloseSession(sessionId) {
  currentSessionId = sessionId;
  const select = document.getElementById("teacher-session-select");
  if (select) select.value = sessionId;
  closeManageModal();
  refreshAmbientState();
}

function confirmActivateSession(s) {
  const current = sessionsList.find(x => x.is_active);
  openConfirmModal({
    title: "Ganti sesi aktif?",
    body:
      `Siswa akan mengerjakan "${s.title}".` +
      (current ? `\n\nSesi "${current.title}" berhenti menjadi sesi aktif. Jawaban yang sudah masuk tetap tersimpan.` : ""),
    okLabel: "Ya, jadikan aktif",
    onConfirm: () => activateSession(s.id)
  });
}

async function activateSession(sessionId) {
  try {
    const res = await fetch(`${API_BASE}/api/sessions/${sessionId}/activate`, { method: "POST" });
    if (!res.ok) throw new Error("Gagal mengaktifkan sesi");
    showToast("Sesi aktif diganti. Siswa sekarang mengerjakan sesi ini.", "success");
    currentSessionId = sessionId;
    await loadSessions();
    await refreshAmbientState();
    renderSessionCardsInModal();
  } catch (err) {
    showToast("Gagal mengaktifkan sesi: " + err.message, "error");
  }
}

async function handleCreateSession(e) {
  e.preventDefault();
  const title = document.getElementById("create-title").value.trim();
  const session_number = parseInt(document.getElementById("create-session-num").value, 10) || 1;
  const max_items = parseInt(document.getElementById("create-max-items").value, 10) || 20;
  if (!title) return;

  try {
    const res = await fetch(`${API_BASE}/api/sessions`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, session_number, max_items, class_rombel: "XI TKJ 1" })
    });
    if (!res.ok) throw new Error("Gagal membuat sesi baru");
    const data = await res.json();
    showToast("Sesi baru dibuat dan sudah aktif untuk siswa.", "success");
    currentSessionId = data.session_id;
    document.getElementById("create-title").value = "";
    toggleCreateForm(false);
    await loadSessions();
    await refreshAmbientState();
    renderSessionCardsInModal();
  } catch (err) {
    showToast("Gagal membuat sesi: " + err.message, "error");
  }
}

// ---------- Tab: Ulangi pengerjaan ----------
function prepareResetTab() {
  document.getElementById("reset-session-name").textContent = currentSessionLabel();

  const sel = document.getElementById("modal-select-student");
  const prev = sel.value;
  let codes = [];
  if (typeof lastState !== "undefined" && lastState && Array.isArray(lastState.heatmap)) {
    codes = [...new Set(lastState.heatmap.map(c => c.student_code))].sort();
  }
  if (codes.length === 0) {
    const n = (lastState && lastState.active_students_count) || 34;
    codes = Array.from({ length: n }, (_, i) => `std_${String(i + 1).padStart(2, "0")}`);
  }
  sel.innerHTML = `<option value="">Pilih siswa...</option>` +
    codes.map(c => `<option value="${escapeHtml(c)}">${escapeHtml(c)}</option>`).join("");
  if (codes.includes(prev)) sel.value = prev;
}

function resetSelectedStudent() {
  const studentCode = document.getElementById("modal-select-student").value;
  if (!studentCode) {
    showToast("Pilih siswa terlebih dahulu.", "error");
    return;
  }
  quickResetStudent(studentCode); // confirms first, then resets and refreshes
}

// ---------- Tab: Cek soal ----------
async function handleTestItemLabel(e) {
  e.preventDefault();
  const promptText = document.getElementById("label-test-prompt").value.trim();
  if (!promptText) return;
  const opt = id => document.getElementById(id).value.trim();

  const btn = document.getElementById("btn-submit-label");
  btn.disabled = true;
  btn.textContent = "Mendeteksi...";
  try {
    const res = await fetch(`${API_BASE}/api/teacher/items/label`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        prompt_text: promptText,
        options: { A: opt("label-opt-a"), B: opt("label-opt-b"), C: opt("label-opt-c"), D: opt("label-opt-d") }
      })
    });
    if (!res.ok) throw new Error("Gagal mendeteksi topik soal");
    renderLabelResult(await res.json());
  } catch (err) {
    showToast(err.message, "error");
  } finally {
    btn.disabled = false;
    btn.textContent = "Deteksi topik";
  }
}

function renderLabelResult(data) {
  const card = document.getElementById("label-result-card");
  card.classList.remove("hidden");
  const sure = data.confidence >= 0.60;
  const row = (label, value) => `
    <div class="flex justify-between gap-3 py-1.5 border-b border-swan last:border-0">
      <span class="text-xs font-bold text-wolf">${label}</span>
      <span class="text-sm font-extrabold text-eel text-right">${value}</span>
    </div>`;

  card.innerHTML = `
    <div class="flex items-center justify-between gap-2">
      <span class="text-sm font-extrabold text-eel">Hasil deteksi</span>
      <span class="px-2.5 py-0.5 rounded-full text-[11px] font-extrabold ${sure ? "bg-feather-soft text-feather-shade" : "bg-bee-soft text-fox"}"
            title="Sumber: ${escapeHtml(data.source)} · ${data.latency_ms} ms">
        ${sure ? "Cukup yakin" : "Kurang yakin, mohon dicek"} · ${pct(data.confidence)}
      </span>
    </div>
    <div>
      ${row("Topik", escapeHtml(kcName(data.primary_kc_id, data.primary_kc_name)))}
      ${row("Tingkat berpikir", escapeHtml(bloomText(data.bloom_level)))}
      ${row("Kesulitan", escapeHtml(DIFFICULTY_LABELS[data.nominal_difficulty] || "—"))}
    </div>
    <p class="text-xs font-bold text-wolf leading-relaxed"><b class="text-eel">Alasan:</b> ${escapeHtml(data.rationale)}</p>
  `;
}

async function loadReviewQueue() {
  const container = document.getElementById("review-queue-container");
  const badge = document.getElementById("review-count-badge");
  container.innerHTML = `<p class="text-xs font-bold text-wolf">Memuat...</p>`;

  try {
    const res = await fetch(`${API_BASE}/api/teacher/items/review-queue`);
    if (!res.ok) throw new Error("Gagal mengambil daftar soal");
    const queue = await res.json();

    badge.textContent = queue.length;
    badge.classList.toggle("hidden", queue.length === 0);

    if (queue.length === 0) {
      container.innerHTML = `<p class="p-3 rounded-2xl bg-feather-soft/50 text-sm font-bold text-feather-shade">Semua soal sudah diperiksa.</p>`;
      return;
    }

    container.innerHTML = "";
    const kcOptions = (selectedId) => KC_META.map(k =>
      `<option value="${k.id}" ${k.id === selectedId ? "selected" : ""}>${escapeHtml(k.name)}</option>`).join("");

    queue.forEach(item => {
      const el = document.createElement("article");
      el.className = "p-3.5 rounded-2xl border-2 border-swan space-y-2.5";
      const opts = Object.entries(item.options || {})
        .map(([k, v]) => `<li><b class="text-wolf">${escapeHtml(k)}.</b> ${escapeHtml(v)}</li>`).join("");
      el.innerHTML = `
        <p class="text-sm font-bold text-eel leading-snug">${escapeHtml(item.prompt_text)}</p>
        <details class="text-xs">
          <summary class="cursor-pointer font-extrabold text-macaw-shade">Lihat pilihan jawaban</summary>
          <ul class="mt-1.5 space-y-0.5 font-bold text-eel">${opts}</ul>
        </details>
        <div class="flex flex-wrap gap-1.5 text-[11px] font-extrabold">
          <span class="px-2 py-0.5 rounded-full bg-snow border border-swan text-wolf">${escapeHtml(bloomText(item.current_bloom_level))}</span>
          <span class="px-2 py-0.5 rounded-full bg-snow border border-swan text-wolf">${escapeHtml(DIFFICULTY_LABELS[item.current_difficulty] || "—")}</span>
          <span class="px-2 py-0.5 rounded-full bg-bee-soft text-fox" title="Seberapa yakin sistem pada topik soal ini">Keyakinan sistem ${pct(item.confidence)}</span>
        </div>
        <div class="flex flex-col sm:flex-row gap-2">
          <label class="sr-only" for="kc-${escapeHtml(item.item_id)}">Topik soal</label>
          <select id="kc-${escapeHtml(item.item_id)}" class="flex-1 min-w-0 bg-polar border-2 border-swan rounded-xl px-2.5 py-2 text-xs font-extrabold text-eel focus:border-macaw focus:outline-none">
            ${kcOptions(item.current_primary_kc_id)}
          </select>
          <button type="button" class="duo-btn duo-btn-green px-4 py-2 text-[11px] whitespace-nowrap">Setujui topik</button>
        </div>
      `;
      const select = el.querySelector("select");
      el.querySelector("button").onclick = () => approveReviewItem(
        item.item_id, select.value, item.current_bloom_level || "C2", item.current_difficulty);
      container.appendChild(el);
    });
  } catch (err) {
    container.innerHTML = `<p class="text-xs font-bold text-cardinal-shade">Gagal memuat: ${escapeHtml(err.message)}</p>`;
  }
}

async function approveReviewItem(itemId, kcId, bloom, diff) {
  try {
    const res = await fetch(`${API_BASE}/api/teacher/items/${itemId}/approve-label`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        primary_kc_id: kcId,
        bloom_level: bloom,
        difficulty_nominal: diff,
        teacher_notes: "Disetujui melalui Antrean Tinjauan Guru"
      })
    });
    if (!res.ok) throw new Error("Gagal menyimpan persetujuan");
    showToast("Topik soal disetujui.", "success");
    loadReviewQueue();
  } catch (err) {
    showToast("Gagal: " + err.message, "error");
  }
}

// Modal Backdrop Dismiss
document.getElementById("modal-manage").onclick = (e) => {
  if (e.target.id === "modal-manage") closeManageModal();
};
document.getElementById("modal-summary").onclick = (e) => {
  if (e.target.id === "modal-summary") closeSummaryModal();
};
