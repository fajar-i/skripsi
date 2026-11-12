const API_BASE = window.location.origin;

const PRAISE_TITLES = [
  "Mantap!",
  "Tepat sekali!",
  "Keren, lanjut terus!",
  "Luar biasa!"
];

const RETRY_TITLES = [
  "Hampir! Yuk cek jawabannya",
  "Belum tepat — simpan konsepnya",
  "Oke, perhatikan polanya ya"
];

const CHECK_SVG = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M5 13l4 4L19 7" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>';
const CROSS_SVG = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M6 6l12 12M18 6L6 18" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/></svg>';
const SOUND_ON_SVG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M11 5L6 9H2v6h4l5 4V5Z" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07M19.07 4.93a10 10 0 0 1 0 14.14" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
const SOUND_OFF_SVG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M11 5L6 9H2v6h4l5 4V5Z" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M23 9l-6 6M17 9l6 6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';

function createFeedbackAudio(src) {
  if (typeof Audio === "undefined") return null;
  const audio = new Audio(src);
  audio.preload = "auto";
  audio.volume = 0.85;
  return audio;
}

const FEEDBACK_AUDIO = {
  correct: createFeedbackAudio(`${API_BASE}/assets/audio/correct_answer.mp3`),
  wrong: createFeedbackAudio(`${API_BASE}/assets/audio/wrong_answer.mp3`),
};

function readSoundMutedPref() {
  try {
    return localStorage.getItem("logitrace_sound_muted") === "1";
  } catch (e) {
    return false;
  }
}

function writeSoundMutedPref(muted) {
  try {
    localStorage.setItem("logitrace_sound_muted", muted ? "1" : "0");
  } catch (e) {}
}

let isSoundMuted = readSoundMutedPref();
let isAudioPrimed = false;

function primeFeedbackAudio() {
  if (isAudioPrimed) return;
  isAudioPrimed = true;
  Object.values(FEEDBACK_AUDIO).forEach(audio => {
    if (!audio) return;
    try {
      if (audio.readyState === 0) audio.load();
    } catch (e) {}
  });
}

window.addEventListener("pointerdown", primeFeedbackAudio, { once: true, passive: true });
window.addEventListener("keydown", primeFeedbackAudio, { once: true, passive: true });

function stopAllFeedbackAudio() {
  Object.values(FEEDBACK_AUDIO).forEach(audio => {
    if (!audio) return;
    try {
      audio.pause();
      audio.currentTime = 0;
    } catch (e) {}
  });
}

function playFeedbackSound(isCorrect) {
  if (isSoundMuted) return;
  const audio = isCorrect ? FEEDBACK_AUDIO.correct : FEEDBACK_AUDIO.wrong;
  if (!audio) return;
  stopAllFeedbackAudio();
  try {
    audio.currentTime = 0;
    const playPromise = audio.play();
    if (playPromise && typeof playPromise.catch === "function") {
      playPromise.catch(() => {});
    }
  } catch (e) {}
}

function updateSoundToggleButton() {
  const btn = document.getElementById("btn-toggle-sound");
  if (!btn) return;
  btn.innerHTML = isSoundMuted ? SOUND_OFF_SVG : SOUND_ON_SVG;
  btn.setAttribute("aria-pressed", isSoundMuted ? "true" : "false");
  btn.setAttribute("aria-label", "Bisukan efek suara");
  btn.title = isSoundMuted ? "Efek suara dibisukan — klik untuk aktifkan" : "Efek suara aktif — klik untuk bisukan";
  btn.className = isSoundMuted
    ? "w-11 h-11 rounded-xl border-2 border-swan bg-snow hover:bg-swan/50 text-wolf flex items-center justify-center flex-shrink-0 transition"
    : "w-11 h-11 rounded-xl border-2 border-swan bg-polar hover:bg-snow text-macaw-shade flex items-center justify-center flex-shrink-0 transition";
}

function toggleSound() {
  isSoundMuted = !isSoundMuted;
  writeSoundMutedPref(isSoundMuted);
  if (isSoundMuted) stopAllFeedbackAudio();
  updateSoundToggleButton();
}

let currentStudentCode = localStorage.getItem("logitrace_student_code") || "";
let activeSessionId = localStorage.getItem("logitrace_active_session_id") || "session_01";
let currentItem = null;
let selectedChoice = null;
let isAnswerLocked = false;
let hintUsed = false;
let hintLevel = 0;
let questionStartTime = null;
let totalHintsUsed = 0;
let lastReportedMastery = null;
let lastSubmitResult = null;
let consecutiveKcErrors = {};
let sessionStatusCache = {};
let activeConfirmCallback = null;

function escapeHtml(text) {
  if (!text) return "";
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function getHintStorageKey(studentCode, sessionId) {
  return `logitrace_hints_${studentCode}_${sessionId}`;
}

function getMasteryStorageKey(studentCode, sessionId) {
  return `logitrace_mastery_${studentCode}_${sessionId}`;
}

function loadPersistedSessionStats() {
  if (!currentStudentCode || !activeSessionId) return;
  const savedHints = localStorage.getItem(getHintStorageKey(currentStudentCode, activeSessionId));
  totalHintsUsed = savedHints !== null ? (parseInt(savedHints, 10) || 0) : 0;

  const savedMastery = localStorage.getItem(getMasteryStorageKey(currentStudentCode, activeSessionId));
  if (savedMastery !== null && !Number.isNaN(parseFloat(savedMastery))) {
    lastReportedMastery = parseFloat(savedMastery);
  }
}

function savePersistedSessionStats() {
  if (!currentStudentCode || !activeSessionId) return;
  localStorage.setItem(getHintStorageKey(currentStudentCode, activeSessionId), String(totalHintsUsed));
  if (lastReportedMastery !== null) {
    localStorage.setItem(getMasteryStorageKey(currentStudentCode, activeSessionId), String(lastReportedMastery));
  }
}

function initStudentDropdown() {
  const select = document.getElementById("student-select");
  select.innerHTML = '<option value="">-- Pilih Kode (std_01–34) --</option>';
  for (let i = 1; i <= 34; i++) {
    const code = `std_${i.toString().padStart(2, "0")}`;
    const opt = document.createElement("option");
    opt.value = code;
    opt.textContent = `${code} (XI TKJ 1)`;
    if (code === currentStudentCode) opt.selected = true;
    select.appendChild(opt);
  }
}

function showScreen(screenId) {
  ["screen-login", "screen-classroom", "screen-quiz", "screen-summary"].forEach(id => {
    document.getElementById(id).classList.add("hidden");
  });
  document.getElementById("quiz-dock").classList.add("hidden");
  document.getElementById("feedback-banner").classList.add("hidden");
  document.getElementById("quiz-error-banner").classList.add("hidden");

  const showChrome = (screenId === "screen-login" || screenId === "screen-classroom");
  document.getElementById("app-topbar").classList.toggle("hidden", !showChrome);
  document.getElementById("app-footer").classList.toggle("hidden", !showChrome);

  document.getElementById(screenId).classList.remove("hidden");

  if (screenId === "screen-quiz") {
    document.getElementById("quiz-dock").classList.remove("hidden");
  }
}

function updateStudentBadge() {
  const container = document.getElementById("student-badge-container");
  if (!currentStudentCode) {
    container.innerHTML = "";
    return;
  }
  container.innerHTML = `
    <span class="px-3 py-1 rounded-xl bg-snow border-2 border-swan text-xs font-num font-bold text-eel">
      ${escapeHtml(currentStudentCode)}
    </span>
    <button type="button" onclick="logoutStudent()" class="text-xs font-extrabold text-wolf hover:text-eel px-3 py-1.5 rounded-xl border-2 border-swan bg-polar hover:bg-snow transition" title="Ganti Siswa">
      Ganti
    </button>
  `;
}

function loginStudent() {
  const val = document.getElementById("student-select").value;
  const errBox = document.getElementById("login-error");
  if (!val) {
    errBox.classList.remove("hidden");
    return;
  }
  errBox.classList.add("hidden");
  currentStudentCode = val;
  localStorage.setItem("logitrace_student_code", currentStudentCode);
  updateStudentBadge();
  loadClassroomSessions();
}

function logoutStudent() {
  stopAllFeedbackAudio();
  currentStudentCode = "";
  localStorage.removeItem("logitrace_student_code");
  updateStudentBadge();
  showScreen("screen-login");
}

function returnToClassroom() {
  stopAllFeedbackAudio();
  loadClassroomSessions();
}

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
  if (e.key === "Escape" && !document.getElementById("modal-confirm").classList.contains("hidden")) {
    closeConfirmModal();
  }
});

async function loadClassroomSessions() {
  showScreen("screen-classroom");
  const container = document.getElementById("classroom-sessions-list");
  container.innerHTML = `<div class="p-6 text-center text-sm font-bold text-wolf bg-snow rounded-3xl border-2 border-swan">Memuat daftar sesi...</div>`;

  try {
    const resp = await fetch(`${API_BASE}/api/sessions?class_rombel=XI%20TKJ%201`);
    if (!resp.ok) throw new Error("Gagal mengambil sesi");
    const sessions = await resp.json();

    container.innerHTML = "";
    if (!sessions.length) {
      container.innerHTML = `<div class="p-6 text-center text-sm font-bold text-wolf bg-snow rounded-3xl border-2 border-swan">Belum ada sesi latihan aktif untuk XI TKJ 1.</div>`;
      return;
    }

    for (const sess of sessions) {
      let statusData = { status: "NOT_STARTED", current_sequence: 0, max_items: sess.max_items, final_mastery: null };
      try {
        const stResp = await fetch(`${API_BASE}/api/sessions/${sess.id}/student/${currentStudentCode}/status`);
        if (stResp.ok) statusData = await stResp.json();
      } catch (e) {}

      sessionStatusCache[sess.id] = statusData;

      const card = document.createElement("div");
      card.className = "bg-polar rounded-3xl p-5 border-2 border-swan border-b-[5px] space-y-4";

      let statusBadge = "";
      let actionBtn = "";
      const maxItems = statusData.max_items || sess.max_items || 20;

      if (statusData.status === "COMPLETED") {
        const masteryLabel = statusData.final_mastery !== null && statusData.final_mastery !== undefined
          ? `Selesai &bull; m=${Number(statusData.final_mastery).toFixed(2)}`
          : "Selesai";
        statusBadge = `<span class="px-3 py-1 rounded-full text-[11px] font-num font-bold bg-feather-soft text-feather-shade border border-feather/30">${masteryLabel}</span>`;
        actionBtn = `
          <div class="grid grid-cols-2 gap-2.5">
            <button type="button" data-action="start" class="duo-btn duo-btn-blue text-xs py-3 px-3">
              Lihat Hasil
            </button>
            <button type="button" data-action="reset" class="duo-btn duo-btn-ghost text-xs py-3 px-3">
              Ulangi
            </button>
          </div>
        `;
      } else if (statusData.status === "IN_PROGRESS") {
        const pct = Math.min(100, Math.round(((statusData.current_sequence || 0) / maxItems) * 100));
        statusBadge = `<span class="px-3 py-1 rounded-full text-[11px] font-num font-bold tabular-nums bg-macaw-soft text-macaw-shade border border-macaw/30">Soal ${statusData.current_sequence}/${maxItems}</span>`;
        actionBtn = `
          <div class="space-y-3">
            <div class="w-full h-3 rounded-full bg-swan overflow-hidden">
              <div class="h-full bg-macaw rounded-full spring-bar" style="width: ${pct}%"></div>
            </div>
            <div class="flex gap-2.5">
              <button type="button" data-action="start" class="flex-1 duo-btn duo-btn-green text-xs py-3 px-4">
                Lanjutkan
              </button>
              <button type="button" data-action="reset" class="duo-btn duo-btn-ghost text-xs py-3 px-4" title="Ulangi dari Soal 1">
                Ulangi
              </button>
            </div>
          </div>
        `;
      } else {
        statusBadge = `<span class="px-3 py-1 rounded-full text-[11px] font-num font-semibold bg-snow text-wolf border-2 border-swan">Belum Mulai</span>`;
        actionBtn = `
          <button type="button" data-action="start" class="w-full duo-btn duo-btn-green text-xs py-3.5 px-4">
            <span>Mulai Latihan (${maxItems} Soal)</span>
            <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
        `;
      }

      card.innerHTML = `
        <div class="flex justify-between items-start gap-3">
          <div>
            <span class="text-[11px] font-num font-bold text-wolf uppercase tracking-wider">Sesi ${sess.session_number}</span>
            <h4 class="font-display font-extrabold text-lg text-eel leading-snug mt-0.5">${escapeHtml(sess.title)}</h4>
          </div>
          <div class="flex-shrink-0">${statusBadge}</div>
        </div>
        ${actionBtn}
      `;
      card.querySelectorAll('[data-action="start"]').forEach(btn => {
        btn.onclick = () => startSessionQuiz(sess.id);
      });
      card.querySelectorAll('[data-action="reset"]').forEach(btn => {
        btn.onclick = () => resetAndStartSession(sess.id);
      });
      container.appendChild(card);
    }
  } catch (err) {
    console.error(err);
    container.innerHTML = `<div class="p-5 text-center text-sm font-extrabold text-cardinal-shade bg-cardinal-soft rounded-3xl border-2 border-cardinal/40">Gagal memuat daftar sesi. Periksa koneksi ke server LogiTrace.</div>`;
  }
}

async function startSessionQuiz(sessionId) {
  activeSessionId = sessionId;
  localStorage.setItem("logitrace_active_session_id", sessionId);
  lastSubmitResult = null;
  consecutiveKcErrors = {};
  loadPersistedSessionStats();
  await fetchNextQuestion();
}

function resetAndStartSession(sessionId) {
  openConfirmModal({
    title: "Ulangi dari Soal 1?",
    body: "Progres pengerjaanmu pada sesi ini akan dimulai kembali dari Soal 1.",
    okLabel: "Ya, Mulai Ulang",
    onConfirm: async () => {
      try {
        const resp = await fetch(`${API_BASE}/api/sessions/${sessionId}/reset-student/${currentStudentCode}`, { method: "POST" });
        if (!resp.ok) throw new Error("Gagal mereset sesi siswa");
        activeSessionId = sessionId;
        localStorage.setItem("logitrace_active_session_id", sessionId);
        totalHintsUsed = 0;
        lastReportedMastery = null;
        lastSubmitResult = null;
        consecutiveKcErrors = {};
        localStorage.removeItem(getHintStorageKey(currentStudentCode, sessionId));
        localStorage.removeItem(getMasteryStorageKey(currentStudentCode, sessionId));
        await fetchNextQuestion();
      } catch (e) {
        showQuizError("Gagal mereset sesi. Silakan coba lagi.");
      }
    }
  });
}

function restartActiveAttempt() {
  resetAndStartSession(activeSessionId);
}

function showQuizError(msg) {
  const errEl = document.getElementById("quiz-error-banner");
  const textEl = document.getElementById("quiz-error-text");
  if (!errEl || !textEl) return;
  textEl.textContent = msg;
  errEl.classList.remove("hidden");
}

async function fetchNextQuestion() {
  showScreen("screen-quiz");
  selectedChoice = null;
  isAnswerLocked = false;
  hintUsed = false;
  hintLevel = 0;

  const submitBtn = document.getElementById("btn-submit");
  submitBtn.disabled = true;
  submitBtn.innerHTML = `<span>Cek Jawaban</span>`;

  document.getElementById("hint-panel").classList.add("hidden");
  document.getElementById("hint-status-pill").classList.add("hidden");
  document.getElementById("hint-body").textContent = "Pilih Level 1 untuk arahan ringan, atau Level 2–3 untuk langkah berpikir yang lebih rinci tanpa membocorkan kunci jawaban.";
  resetHintLevelButtons();

  try {
    const url = `${API_BASE}/api/quiz/${currentStudentCode}/next?session_id=${encodeURIComponent(activeSessionId)}`;
    const resp = await fetch(url);
    if (!resp.ok) {
      if (resp.status === 404) {
        logoutStudent();
        return;
      }
      throw new Error("Gagal mengambil soal berikutnya");
    }
    const data = await resp.json();

    if (data.is_completed) {
      currentItem = data;
      await showSummary();
      return;
    }

    currentItem = data;
    renderQuestion(data);
    if ((consecutiveKcErrors[data.primary_kc] || 0) >= 2) {
      document.getElementById("hint-panel").classList.remove("hidden");
      loadHint(1);
    }
    questionStartTime = Date.now();
  } catch (err) {
    console.error(err);
    showQuizError("Gangguan koneksi ke server LogiTrace. Coba muat ulang atau periksa jaringan lab.");
  }
}

function renderQuestion(item) {
  const seq = item.sequence_number;
  const maxSeq = item.max_items || 20;

  if (seq > maxSeq || item.is_completed) {
    showSummary();
    return;
  }

  document.getElementById("label-sequence").textContent = `${seq}/${maxSeq}`;
  const progressPercent = Math.min(100, Math.max(5, Math.round(((seq - 1) / maxSeq) * 100)));
  document.getElementById("progress-bar").style.width = `${progressPercent}%`;

  const badgeStage = document.getElementById("badge-stage");
  if (item.is_calibration) {
    badgeStage.textContent = "Pemetaan Awal";
    badgeStage.className = "hidden sm:inline-block px-2.5 py-1 rounded-xl text-[11px] font-extrabold bg-macaw-soft text-macaw-shade";
  } else {
    badgeStage.textContent = "Adaptif ZPD";
    badgeStage.className = "hidden sm:inline-block px-2.5 py-1 rounded-xl text-[11px] font-extrabold bg-feather-soft text-feather-shade";
  }

  document.getElementById("text-kc-name").textContent = item.kc_name || item.primary_kc;

  const diffBadge = document.getElementById("badge-diff");
  if (item.difficulty === 1) {
    diffBadge.textContent = "Mudah";
    diffBadge.className = "px-3 py-1 rounded-xl text-xs font-extrabold bg-feather-soft text-feather-shade";
  } else if (item.difficulty === 2) {
    diffBadge.textContent = "Sedang";
    diffBadge.className = "px-3 py-1 rounded-xl text-xs font-extrabold bg-macaw-soft text-macaw-shade";
  } else {
    diffBadge.textContent = "Sulit";
    diffBadge.className = "px-3 py-1 rounded-xl text-xs font-extrabold bg-fox-soft text-fox";
  }

  document.getElementById("question-prompt").textContent = item.prompt_text;

  const optContainer = document.getElementById("options-container");
  optContainer.innerHTML = "";

  const keys = ["A", "B", "C", "D"];
  keys.forEach(k => {
    if (!item.options[k]) return;
    const optCard = document.createElement("button");
    optCard.type = "button";
    optCard.dataset.choice = k;
    optCard.setAttribute("aria-pressed", "false");
    optCard.className = "mc-opt";
    optCard.onclick = () => selectOption(k, optCard);

    optCard.innerHTML = `
      <span class="opt-key">${k}</span>
      <span class="text-sm sm:text-base font-bold text-eel leading-snug">${escapeHtml(item.options[k])}</span>
    `;
    optContainer.appendChild(optCard);
  });
}

function selectOption(key, element) {
  if (isAnswerLocked) return;
  selectedChoice = key;

  document.querySelectorAll("#options-container .mc-opt").forEach(el => {
    el.classList.remove("is-selected");
    el.setAttribute("aria-pressed", "false");
  });
  element.classList.add("is-selected");
  element.setAttribute("aria-pressed", "true");
  document.getElementById("btn-submit").disabled = false;
}

function resetHintLevelButtons() {
  document.querySelectorAll(".btn-hint-lvl").forEach(btn => {
    btn.className = "btn-hint-lvl px-3 py-1.5 rounded-xl text-xs font-extrabold bg-polar hover:bg-macaw-soft text-eel border-2 border-swan transition";
  });
}

async function loadHint(level) {
  if (!currentItem || isAnswerLocked) return;
  const hintBody = document.getElementById("hint-body");
  hintBody.textContent = `Menyiapkan petunjuk Level ${level}...`;

  resetHintLevelButtons();
  const activeBtn = document.querySelector(`.btn-hint-lvl[data-level="${level}"]`);
  if (activeBtn) {
    activeBtn.className = "btn-hint-lvl px-3 py-1.5 rounded-xl text-xs font-extrabold bg-macaw text-white border-2 border-macaw-shade transition";
  }

  try {
    const resp = await fetch(`${API_BASE}/api/quiz/hint`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        student_code: currentStudentCode,
        item_id: currentItem.item_id,
        requested_level: level
      })
    });

    if (!resp.ok) throw new Error("Gagal mengambil petunjuk");
    const data = await resp.json();

    hintBody.innerHTML = `<span class="text-macaw-shade font-extrabold">Level ${data.hint_level}:</span> ${escapeHtml(data.hint_text)}`;
    if (!hintUsed) {
      totalHintsUsed++;
      savePersistedSessionStats();
    }
    hintUsed = true;
    hintLevel = level;
    document.getElementById("hint-status-pill").classList.remove("hidden");
  } catch (err) {
    console.error(err);
    hintBody.textContent = "Petunjuk sedang tidak bisa dimuat. Coba klik sekali lagi ya.";
  }
}

document.getElementById("btn-toggle-hint").onclick = () => {
  document.getElementById("hint-panel").classList.toggle("hidden");
};

document.getElementById("btn-submit").onclick = async () => {
  if (!selectedChoice || !currentItem || isAnswerLocked) return;

  primeFeedbackAudio();
  const responseTimeMs = Date.now() - (questionStartTime || Date.now());
  const btn = document.getElementById("btn-submit");
  btn.disabled = true;
  btn.textContent = "Memeriksa...";
  document.getElementById("quiz-error-banner").classList.add("hidden");

  try {
    const payload = {
      student_code: currentStudentCode,
      item_id: currentItem.item_id,
      choice: selectedChoice,
      session_id: activeSessionId,
      response_time_ms: responseTimeMs,
      used_hint: hintUsed,
      hint_level: hintLevel
    };

    const resp = await fetch(`${API_BASE}/api/quiz/submit`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!resp.ok) throw new Error("Gagal mengirim jawaban");
    const result = await resp.json();
    isAnswerLocked = true;
    lastSubmitResult = result;
    showFeedback(result);
  } catch (err) {
    console.error(err);
    showQuizError("Gagal memproses jawaban. Coba tekan Cek Jawaban sekali lagi.");
    btn.disabled = false;
    btn.innerHTML = `<span>Cek Jawaban</span>`;
  }
};

function showFeedback(result) {
  const banner = document.getElementById("feedback-banner");
  const iconBox = document.getElementById("fb-icon-container");
  const title = document.getElementById("fb-title");
  const subtitle = document.getElementById("fb-subtitle");
  const nextBtn = document.getElementById("btn-next-question");
  const deltaElem = document.getElementById("fb-delta-m");

  // Highlight option cards
  document.querySelectorAll("#options-container .mc-opt").forEach(el => {
    const c = el.dataset.choice;
    el.disabled = true;
    el.classList.remove("is-selected");
    if (c === result.correct_choice) {
      el.classList.add("is-correct");
    } else if (c === selectedChoice && !result.is_correct) {
      el.classList.add("is-wrong");
    }
  });

  // Update top progress bar smoothly upon submission
  const maxSeq = currentItem ? (currentItem.max_items || 20) : 20;
  const completedSeq = result.sequence_number || (currentItem ? currentItem.sequence_number : 1);
  document.getElementById("progress-bar").style.width = `${Math.min(100, Math.round((completedSeq / maxSeq) * 100))}%`;

  playFeedbackSound(Boolean(result.is_correct));

  if (result.is_correct) {
    if (currentItem && currentItem.primary_kc) {
      consecutiveKcErrors[currentItem.primary_kc] = 0;
    }
    const praiseIdx = (completedSeq - 1) % PRAISE_TITLES.length;
    banner.className = "fixed inset-x-0 bottom-0 z-50 border-t-2 border-feather bg-feather-soft px-4 py-5 banner-slide";
    iconBox.className = "w-11 h-11 rounded-full bg-feather flex items-center justify-center flex-shrink-0 text-white mt-0.5";
    iconBox.innerHTML = CHECK_SVG;
    title.className = "font-display text-2xl font-extrabold leading-tight text-feather-shade";
    title.textContent = PRAISE_TITLES[praiseIdx];
    subtitle.className = "text-sm font-bold text-eel mt-0.5";
    subtitle.textContent = hintUsed ? "Bagus — terselesaikan dengan bantuan petunjuk!" : "Dijawab mandiri tanpa petunjuk!";
    nextBtn.className = "w-full duo-btn duo-btn-green py-3.5 px-6 tap-target";
    nextBtn.innerHTML = `<span>${result.is_completed ? "Lihat Perayaan" : "Lanjut"}</span>`;
  } else {
    if (currentItem && currentItem.primary_kc) {
      consecutiveKcErrors[currentItem.primary_kc] = (consecutiveKcErrors[currentItem.primary_kc] || 0) + 1;
    }
    const retryIdx = (completedSeq - 1) % RETRY_TITLES.length;
    banner.className = "fixed inset-x-0 bottom-0 z-50 border-t-2 border-cardinal bg-cardinal-soft px-4 py-5 banner-slide";
    iconBox.className = "w-11 h-11 rounded-full bg-cardinal flex items-center justify-center flex-shrink-0 text-white mt-0.5";
    iconBox.innerHTML = CROSS_SVG;
    title.className = "font-display text-2xl font-extrabold leading-tight text-cardinal-shade";
    title.textContent = RETRY_TITLES[retryIdx];
    subtitle.className = "text-sm font-extrabold text-cardinal-shade mt-0.5";
    subtitle.textContent = `Jawaban yang benar: Pilihan ${result.correct_choice}`;
    nextBtn.className = "w-full duo-btn duo-btn-red py-3.5 px-6 tap-target";
    nextBtn.innerHTML = `<span>${result.is_completed ? "Lihat Hasil" : "Paham, Lanjut"}</span>`;
  }

  lastReportedMastery = result.mastery_after;
  savePersistedSessionStats();

  document.getElementById("fb-p-hat").textContent = `${(result.predicted_p * 100).toFixed(0)}%`;
  document.getElementById("fb-mastery-shift").textContent = `${result.mastery_before.toFixed(2)} → ${result.mastery_after.toFixed(2)}`;

  if (result.mastery_delta >= 0) {
    deltaElem.textContent = `+${result.mastery_delta.toFixed(3)}`;
    deltaElem.className = "font-num text-xs font-bold tabular-nums px-2.5 py-1 rounded-full bg-polar text-feather-shade border border-feather/30";
  } else {
    deltaElem.textContent = `${result.mastery_delta.toFixed(3)}`;
    deltaElem.className = "font-num text-xs font-bold tabular-nums px-2.5 py-1 rounded-full bg-polar text-cardinal-shade border border-cardinal/30";
  }

  document.getElementById("fb-explanation").textContent = result.explanation || "Teruskan latihanmu untuk memperkuat konsep ini!";

  document.getElementById("quiz-dock").classList.add("hidden");
  banner.classList.remove("hidden");
}

document.getElementById("btn-next-question").onclick = () => {
  stopAllFeedbackAudio();
  document.getElementById("feedback-banner").classList.add("hidden");
  const btn = document.getElementById("btn-submit");
  btn.innerHTML = `<span>Cek Jawaban</span>`;

  const maxSeq = currentItem ? (currentItem.max_items || 20) : 20;
  const doneByResult = lastSubmitResult && lastSubmitResult.is_completed;
  const doneBySeq = currentItem && (currentItem.sequence_number >= maxSeq || currentItem.is_completed);

  if (doneByResult || doneBySeq) {
    showSummary();
  } else {
    fetchNextQuestion();
  }
};

function spawnConfetti() {
  const layer = document.getElementById("confetti-layer");
  layer.innerHTML = "";
  if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    return;
  }
  const colors = ["#FFC800", "#1CB0F6", "#FF9600", "#FF4B4B", "#CE82FF", "#89E219", "#FFFFFF"];
  for (let i = 0; i < 65; i++) {
    const piece = document.createElement("div");
    piece.className = "confetti-piece";
    piece.style.left = `${Math.random() * 100}vw`;
    piece.style.background = colors[i % colors.length];
    piece.style.animationDuration = `${2.0 + Math.random() * 1.8}s`;
    piece.style.animationDelay = `${Math.random() * 0.9}s`;
    layer.appendChild(piece);
    setTimeout(() => piece.remove(), 4800);
  }
}

async function showSummary() {
  showScreen("screen-summary");
  spawnConfetti();

  const cached = sessionStatusCache[activeSessionId] || {};
  let maxItems = (currentItem && currentItem.max_items) || cached.max_items || 20;
  let finalMastery = lastReportedMastery !== null ? lastReportedMastery : cached.final_mastery;

  // Fetch fresh status if mastery isn't loaded yet (e.g. clicking "Lihat Hasil" directly)
  if ((finalMastery === null || finalMastery === undefined) && currentStudentCode && activeSessionId) {
    try {
      const resp = await fetch(`${API_BASE}/api/sessions/${activeSessionId}/student/${currentStudentCode}/status`);
      if (resp.ok) {
        const st = await resp.json();
        sessionStatusCache[activeSessionId] = st;
        if (st.final_mastery !== null && st.final_mastery !== undefined) {
          finalMastery = st.final_mastery;
        }
        if (st.max_items) maxItems = st.max_items;
      }
    } catch (e) {}
  }

  document.getElementById("sum-student").textContent = `${currentStudentCode} (XI TKJ 1)`;
  document.getElementById("sum-total-items").textContent = `${maxItems} Soal`;
  document.getElementById("sum-hints").textContent = `${totalHintsUsed} kali`;
  document.getElementById("sum-avg-mastery").textContent = (finalMastery !== null && finalMastery !== undefined)
    ? Number(finalMastery).toFixed(2)
    : "Tuntas";
}

document.getElementById("btn-login").onclick = loginStudent;
updateSoundToggleButton();
initStudentDropdown();
if (currentStudentCode) {
  updateStudentBadge();
  loadClassroomSessions();
} else {
  showScreen("screen-login");
}
