let currentSummaryData = null;

// Modal Visibility & Tab Control
function openManageModal() {
  document.getElementById("modal-manage").classList.remove("hidden");
  populateStudentOptions();
  loadSessions();
}

function closeManageModal() {
  document.getElementById("modal-manage").classList.add("hidden");
}

function switchModalTab(tab) {
  const tabs = {
    reset: { content: "tab-content-reset", btn: "tab-btn-reset" },
    create: { content: "tab-content-create", btn: "tab-btn-create" },
    list: { content: "tab-content-list", btn: "tab-btn-list" },
    labeler: { content: "tab-content-labeler", btn: "tab-btn-labeler" }
  };

  Object.values(tabs).forEach(t => {
    const contentEl = document.getElementById(t.content);
    const btnEl = document.getElementById(t.btn);
    if (contentEl) contentEl.classList.add("hidden");
    if (btnEl) btnEl.className = "py-2.5 px-4 border-b-4 border-transparent hover:text-eel transition";
  });

  const active = tabs[tab];
  if (!active) return;
  document.getElementById(active.content).classList.remove("hidden");
  document.getElementById(active.btn).className = "py-2.5 px-4 border-b-4 border-feather text-feather-shade transition";

  if (tab === "list") renderSessionCardsInModal();
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

function renderSessionSummary(data) {
  document.getElementById("summary-loading").classList.add("hidden");
  document.getElementById("summary-content").classList.remove("hidden");

  const pill = document.getElementById("summary-source-pill");
  if (data.source === "llm_9router") {
    pill.className = "px-2.5 py-0.5 rounded-full text-[11px] font-num font-bold bg-macaw-soft text-macaw-shade border border-macaw/30";
    pill.textContent = "Ringkasan AI";
  } else {
    pill.className = "px-2.5 py-0.5 rounded-full text-[11px] font-num font-bold bg-feather-soft text-feather-shade border border-feather/30";
    pill.textContent = "Ringkasan Otomatis";
  }

  document.getElementById("sum-latency-pill").textContent = `Latensi: ${data.latency_ms} ms`;
  document.getElementById("sum-avg-mastery").textContent = data.class_avg_mastery.toFixed(3);
  document.getElementById("sum-accuracy").textContent = `${(data.accuracy_rate * 100).toFixed(1)}%`;
  document.getElementById("sum-completion").textContent = `${data.completed_students} / ${data.total_students}`;
  document.getElementById("sum-total-resp").textContent = `${data.total_responses} butir`;

  const narrativeBox = document.getElementById("sum-narrative-text");
  narrativeBox.innerHTML = "";
  const paragraphs = data.narrative_summary.split(/\n\n+/);
  paragraphs.forEach(p => {
    if (p.trim()) {
      const pEl = document.createElement("p");
      pEl.className = "leading-relaxed text-eel";
      pEl.textContent = p.trim();
      narrativeBox.appendChild(pEl);
    }
  });

  const strBox = document.getElementById("sum-strengths-list");
  strBox.innerHTML = "";
  if (data.strengths && data.strengths.length > 0) {
    data.strengths.forEach(s => {
      const item = document.createElement("div");
      item.className = "p-3 rounded-2xl bg-polar border-2 border-feather/30 flex items-center justify-between gap-2";
      item.innerHTML = `
        <div>
          <p class="font-extrabold text-xs text-eel">${escapeHtml(s.kc_name)}</p>
          <p class="text-[11px] font-num font-semibold text-feather-shade">${escapeHtml(s.kc_id)}</p>
        </div>
        <div class="text-right flex-shrink-0">
          <span class="px-2.5 py-0.5 rounded-full text-xs font-num font-bold tabular-nums bg-feather-soft text-feather-shade">
            m = ${s.avg_mastery.toFixed(2)}
          </span>
          <span class="block text-[11px] font-num font-semibold text-wolf mt-0.5">${s.mastered_count} mahir</span>
        </div>
      `;
      strBox.appendChild(item);
    });
  } else {
    strBox.innerHTML = `<p class="text-xs text-wolf font-sans font-bold">Belum ada data penguasaan tercatat.</p>`;
  }

  const btnBox = document.getElementById("sum-bottlenecks-list");
  btnBox.innerHTML = "";
  if (data.bottlenecks && data.bottlenecks.length > 0) {
    data.bottlenecks.forEach(b => {
      const item = document.createElement("div");
      item.className = "p-3 rounded-2xl bg-polar border-2 border-cardinal/30 flex items-center justify-between gap-2";
      item.innerHTML = `
        <div>
          <p class="font-extrabold text-xs text-eel">${escapeHtml(b.kc_name)}</p>
          <p class="text-[11px] font-num font-semibold text-cardinal-shade">${escapeHtml(b.kc_id)}</p>
        </div>
        <div class="text-right flex-shrink-0">
          <span class="px-2.5 py-0.5 rounded-full text-xs font-num font-bold tabular-nums bg-cardinal-soft text-cardinal-shade">
            m = ${b.avg_mastery.toFixed(2)}
          </span>
          <span class="block text-[11px] font-num font-semibold text-fox mt-0.5">${b.struggling_count} butuh bimbingan</span>
        </div>
      `;
      btnBox.appendChild(item);
    });
  } else {
    btnBox.innerHTML = `<p class="text-xs text-wolf font-sans font-bold">Tidak ada topik kritis teridentifikasi.</p>`;
  }

  const peerBox = document.getElementById("sum-peer-tutoring-cards");
  peerBox.innerHTML = "";
  if (data.peer_tutoring_recommendations && data.peer_tutoring_recommendations.length > 0) {
    data.peer_tutoring_recommendations.forEach(pt => {
      const card = document.createElement("div");
      card.className = "p-4 bg-polar rounded-2xl border-2 border-swan border-b-4 space-y-3";
      const menteeBadges = pt.mentee_student_codes.map(c =>
        `<span class="px-2 py-0.5 rounded-lg bg-bee-soft text-eel border border-bee-shade/40 font-num text-[11px] font-bold">${escapeHtml(c)}</span>`
      ).join(" ");

      card.innerHTML = `
        <div class="flex items-center justify-between gap-2">
          <span class="text-sm font-extrabold text-eel">${escapeHtml(pt.kc_name)}</span>
          <span class="text-[11px] font-num font-bold text-feather-shade">${escapeHtml(pt.kc_id)}</span>
        </div>

        <div class="grid grid-cols-2 gap-2 text-xs font-num bg-snow p-2.5 rounded-xl border border-swan">
          <div>
            <span class="text-[10px] font-sans font-bold text-wolf block">Tutor Sebaya:</span>
            <span class="font-bold text-feather-shade">${escapeHtml(pt.tutor_student_code)} (m=${pt.tutor_mastery.toFixed(2)})</span>
          </div>
          <div>
            <span class="text-[10px] font-sans font-bold text-wolf block">Rekan Belajar:</span>
            <div class="flex flex-wrap gap-1 mt-0.5">${menteeBadges}</div>
          </div>
        </div>

        <div class="text-xs text-eel bg-macaw-soft/50 p-2.5 rounded-xl border border-macaw/25">
          <span class="font-sans font-extrabold text-[10px] uppercase text-macaw-shade block mb-0.5">Fokus Intervensi:</span>
          <p class="font-bold leading-relaxed">${escapeHtml(pt.action_guidance)}</p>
        </div>
      `;
      peerBox.appendChild(card);
    });
  } else {
    peerBox.innerHTML = `
      <div class="col-span-2 p-4 bg-snow rounded-2xl border-2 border-swan text-center text-xs font-sans font-bold text-wolf">
        Belum ada rekomendasi kelompok tutor sebaya yang diperlukan pada sesi ini.
      </div>
    `;
  }
}

function buildSummaryExportText(includeTimestamp) {
  const tsLine = includeTimestamp ? `Waktu Ekspor: ${new Date().toLocaleString("id-ID")}\n` : "";
  return (
    `=== LOGITRACE — RINGKASAN SESI EVALUASI (AGEN T3) ===\n` +
    `Sesi: ${currentSummaryData.session_title} (${currentSummaryData.class_rombel})\n` +
    tsLine +
    `Rata-rata Penguasaan (m): ${currentSummaryData.class_avg_mastery.toFixed(3)}\n` +
    `Akurasi Respons: ${(currentSummaryData.accuracy_rate * 100).toFixed(1)}%\n` +
    `Selesai: ${currentSummaryData.completed_students} dari ${currentSummaryData.total_students} siswa\n\n` +
    `--- REFLEKSI DINAMIKA KELAS ---\n` +
    `${currentSummaryData.narrative_summary}\n\n` +
    `--- REKOMENDASI PEER-TUTORING ROTASI BERIKUTNYA ---\n` +
    currentSummaryData.peer_tutoring_recommendations.map(pt =>
      `• Topik: ${pt.kc_name} (${pt.kc_id})\n  Tutor: ${pt.tutor_student_code} (m=${pt.tutor_mastery.toFixed(2)})\n  Rekan: ${pt.mentee_student_codes.join(", ")}\n  Panduan: ${pt.action_guidance}`
    ).join("\n\n")
  );
}

function copySummaryText() {
  if (!currentSummaryData) return;
  const summaryText = buildSummaryExportText(false);
  if (navigator.clipboard && typeof navigator.clipboard.writeText === "function") {
    navigator.clipboard.writeText(summaryText).then(() => {
      showToast("Catatan refleksi berhasil disalin ke clipboard!", "success");
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
      showToast("Catatan refleksi berhasil disalin ke clipboard!", "success");
    } else {
      showToast("Clipboard tidak tersedia di HTTP. Gunakan tombol 'Unduh (.txt)'.", "info");
    }
  } catch (err) {
    showToast("Clipboard tidak tersedia di HTTP. Gunakan tombol 'Unduh (.txt)'.", "info");
  }
}

function downloadSummaryFile() {
  if (!currentSummaryData) return;
  const blob = new Blob([buildSummaryExportText(true)], { type: "text/plain;charset=utf-8" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = `LogiTrace_Refleksi_${currentSummaryData.session_id}.txt`;
  a.click();
  URL.revokeObjectURL(a.href);
  showToast("Laporan refleksi berhasil diunduh!", "success");
}

// Agent T1 Semantic Labeling Handlers
async function handleTestItemLabel(e) {
  e.preventDefault();
  const promptText = document.getElementById("label-test-prompt").value.trim();
  const optA = document.getElementById("label-opt-a").value.trim();
  const optB = document.getElementById("label-opt-b").value.trim();
  const optC = document.getElementById("label-opt-c").value.trim();
  const optD = document.getElementById("label-opt-d").value.trim();

  if (!promptText) return;

  const btn = document.getElementById("btn-submit-label");
  btn.disabled = true;
  btn.textContent = "Menganalisis...";

  try {
    const payload = {
      prompt_text: promptText,
      options: { A: optA, B: optB, C: optC, D: optD }
    };
    const res = await fetch(`${API_BASE}/api/teacher/items/label`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error("Gagal mengklasifikasikan butir soal");
    const data = await res.json();
    renderLabelResult(data);
  } catch (err) {
    showToast("Gagal analisis label: " + err.message, "error");
  } finally {
    btn.disabled = false;
    btn.textContent = "Klasifikasikan Soal";
  }
}

function renderLabelResult(data) {
  const card = document.getElementById("label-result-card");
  card.classList.remove("hidden");

  const isHighConf = data.confidence >= 0.60;
  const confBadge = isHighConf
    ? `<span class="px-2.5 py-0.5 rounded-full text-[11px] font-extrabold bg-feather-soft text-feather-shade">Keyakinan Tinggi: ${(data.confidence * 100).toFixed(0)}%</span>`
    : `<span class="px-2.5 py-0.5 rounded-full text-[11px] font-extrabold bg-bee-soft text-fox">Butuh Review: ${(data.confidence * 100).toFixed(0)}%</span>`;

  card.innerHTML = `
    <div class="flex items-center justify-between border-b-2 border-swan pb-2">
      <span class="font-extrabold text-eel">Hasil Klasifikasi Topik</span>
      ${confBadge}
    </div>

    <div class="grid grid-cols-2 gap-3 text-xs">
      <div>
        <span class="text-wolf text-[10px] font-bold block">Primary KC:</span>
        <span class="font-extrabold text-feather-shade">${escapeHtml(data.primary_kc_name)}</span>
        <span class="text-[10px] text-wolf block font-num font-semibold">${escapeHtml(data.primary_kc_id)}</span>
      </div>
      <div>
        <span class="text-wolf text-[10px] font-bold block">Saran Level Kognitif (Bloom):</span>
        <span class="font-extrabold text-macaw-shade">${escapeHtml(data.bloom_level)}</span>
        <span class="text-[10px] text-wolf block font-num">Kesulitan Nominal: Level ${data.nominal_difficulty}</span>
      </div>
    </div>

    <div class="p-3 rounded-xl bg-polar border-2 border-swan text-[11px] text-eel leading-relaxed">
      <p><strong class="text-eel">Rasional:</strong> ${escapeHtml(data.rationale)}</p>
      <p class="text-[10px] text-wolf mt-1 font-num font-semibold">Sumber: ${escapeHtml(data.source)} &bull; Latensi: ${data.latency_ms} ms</p>
    </div>
  `;
}

async function loadReviewQueue() {
  const container = document.getElementById("review-queue-container");
  container.innerHTML = `<p class="text-xs font-sans font-bold text-wolf">Memuat antrean bank soal...</p>`;

  try {
    const res = await fetch(`${API_BASE}/api/teacher/items/review-queue`);
    if (!res.ok) throw new Error("Gagal mengambil antrean");
    const queue = await res.json();
    container.innerHTML = "";

    if (queue.length === 0) {
      container.innerHTML = `<p class="text-xs font-sans font-bold text-wolf">Semua butir soal telah terverifikasi penuh.</p>`;
      return;
    }

    queue.forEach(item => {
      const div = document.createElement("div");
      div.className = "p-3 rounded-2xl bg-snow border-2 border-swan flex items-center justify-between gap-2 text-xs font-sans";

      const textDiv = document.createElement("div");
      textDiv.className = "flex-1 min-w-0";
      textDiv.innerHTML = `
        <span class="font-extrabold text-eel block truncate">${escapeHtml(item.prompt_text)}</span>
        <span class="text-[10px] font-num font-semibold text-wolf">${escapeHtml(item.item_id)} &bull; ${escapeHtml(item.current_primary_kc_id)} &bull; ${escapeHtml(item.current_bloom_level || '-')} &bull; ${escapeHtml(item.current_indikator_id || '-')} &bull; Diff: ${item.current_difficulty}</span>
      `;

      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "duo-btn duo-btn-green px-3 py-1.5 text-[11px] whitespace-nowrap";
      btn.textContent = "Verifikasi";
      btn.onclick = () => approveReviewItem(item.item_id, item.current_primary_kc_id, item.current_bloom_level || 'C2', item.current_difficulty);

      div.appendChild(textDiv);
      div.appendChild(btn);
      container.appendChild(div);
    });
  } catch (err) {
    container.innerHTML = `<p class="text-xs font-sans font-bold text-cardinal-shade">Gagal memuat antrean: ${escapeHtml(err.message)}</p>`;
  }
}

async function approveReviewItem(itemId, kcId, bloom, diff) {
  try {
    const payload = {
      primary_kc_id: kcId,
      bloom_level: bloom,
      difficulty_nominal: diff,
      teacher_notes: "Disetujui melalui Antrean Tinjauan Guru"
    };
    const res = await fetch(`${API_BASE}/api/teacher/items/${itemId}/approve-label`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error("Gagal memverifikasi label");
    showToast(`Butir soal ${itemId} berhasil diverifikasi!`, "success");
    loadReviewQueue();
  } catch (err) {
    showToast("Gagal: " + err.message, "error");
  }
}

function populateStudentOptions() {
  const sel = document.getElementById("modal-select-student");
  if (sel.options.length > 1) return;
  for (let i = 1; i <= 34; i++) {
    const code = `std_${String(i).padStart(2, "0")}`;
    const opt = document.createElement("option");
    opt.value = code;
    opt.textContent = `Siswa ${code} (No. Urut ${i})`;
    sel.appendChild(opt);
  }
}

function renderSessionCardsInModal() {
  const container = document.getElementById("modal-session-cards");
  if (!container) return;
  container.innerHTML = "";

  if (sessionsList.length === 0) {
    container.innerHTML = `<p class="text-xs text-wolf font-sans font-bold">Tidak ada sesi ditemukan.</p>`;
    return;
  }

  sessionsList.forEach(s => {
    const card = document.createElement("div");
    const isCurrent = s.id === currentSessionId;
    const safeTitle = escapeHtml(s.title);
    card.className = `p-4 rounded-2xl border-2 transition flex flex-wrap items-center justify-between gap-3 ${
      s.is_active ? "bg-feather-soft/50 border-feather/50" : "bg-snow border-swan"
    }`;

    card.innerHTML = `
      <div class="flex-1 min-w-[200px]">
        <div class="flex flex-wrap items-center gap-2">
          <span class="text-sm font-extrabold text-eel">${safeTitle}</span>
          ${s.is_active ? '<span class="px-2 py-0.5 rounded-full text-[10px] font-num font-bold bg-feather text-white">AKTIF</span>' : ""}
          ${isCurrent && !s.is_active ? '<span class="px-2 py-0.5 rounded-full text-[10px] font-num font-bold bg-swan text-eel">DIPILIH</span>' : ""}
        </div>
        <div class="flex flex-wrap items-center gap-2.5 text-[11px] font-num font-semibold text-wolf mt-1">
          <span>Maks: <strong class="text-eel">${s.max_items} Soal</strong></span>
          <span>&bull;</span>
          <span class="text-feather-shade">${s.completed_count} Selesai</span>
          <span>&bull;</span>
          <span class="text-fox">${s.in_progress_count} Mengerjakan</span>
          <span>&bull;</span>
          <span>${s.not_started_count} Belum</span>
        </div>
      </div>
      <div class="flex items-center gap-2">
        ${!s.is_active ? `
          <button type="button" data-action="activate" class="duo-btn duo-btn-green px-3 py-1.5 text-[11px]" title="Jadikan tugas utama kelas">
            Aktifkan
          </button>
        ` : ""}
        <button type="button" data-action="open" class="duo-btn duo-btn-ghost px-3 py-1.5 text-[11px]">
          Buka di Dasbor
        </button>
      </div>
    `;
    const actBtn = card.querySelector('[data-action="activate"]');
    if (actBtn) actBtn.onclick = () => activateSession(s.id);
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

async function activateSession(sessionId) {
  try {
    const res = await fetch(`${API_BASE}/api/sessions/${sessionId}/activate`, { method: "POST" });
    if (!res.ok) throw new Error("Gagal mengaktifkan sesi");
    const data = await res.json();
    showToast(data.message || "Tugas berhasil diaktifkan untuk kelas!", "success");
    currentSessionId = sessionId;
    await loadSessions();
    await refreshAmbientState();
  } catch (err) {
    showToast("Gagal mengaktifkan sesi: " + err.message, "error");
  }
}

async function handleCreateSession(e) {
  e.preventDefault();
  const title = document.getElementById("create-title").value.trim();
  const session_number = parseInt(document.getElementById("create-session-num").value, 10) || 2;
  const max_items = parseInt(document.getElementById("create-max-items").value, 10) || 20;

  if (!title) return;

  try {
    const payload = {
      title: title,
      session_number: session_number,
      max_items: max_items,
      class_rombel: "XI TKJ 1"
    };
    const res = await fetch(`${API_BASE}/api/sessions`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error("Gagal membuat tugas baru");
    const data = await res.json();
    showToast("Tugas baru berhasil dibuat dan didistribusikan ke 34 siswa!", "success");
    currentSessionId = data.session_id;
    document.getElementById("create-title").value = "";
    await loadSessions();
    await refreshAmbientState();
    switchModalTab("reset");
  } catch (err) {
    showToast("Gagal membuat tugas: " + err.message, "error");
  }
}

async function resetSelectedStudent() {
  const studentCode = document.getElementById("modal-select-student").value;
  if (!studentCode) {
    showToast("Pilih kode siswa terlebih dahulu.", "error");
    return;
  }
  if (!currentSessionId) {
    showToast("Pilih sesi terlebih dahulu.", "error");
    return;
  }

  try {
    const res = await fetch(`${API_BASE}/api/sessions/${currentSessionId}/reset-student/${studentCode}`, { method: "POST" });
    if (!res.ok) throw new Error("Gagal me-reset siswa");
    const data = await res.json();
    showToast(data.message || `Siswa ${studentCode} berhasil di-reset ke Soal 1!`, "success");
    await loadSessions();
    await refreshAmbientState();
  } catch (err) {
    showToast("Gagal me-reset siswa: " + err.message, "error");
  }
}

// Modal Backdrop Dismiss
document.getElementById("modal-manage").onclick = (e) => {
  if (e.target.id === "modal-manage") closeManageModal();
};
document.getElementById("modal-summary").onclick = (e) => {
  if (e.target.id === "modal-summary") closeSummaryModal();
};
