// Teacher login, class code and student login cards.
// Loaded before app.js: wraps fetch so any 401 from the API brings back the login screen.

let teacherAuthed = false;
let dashboardStarted = false;
let classCodeState = { code: null, url: null };

const _rawFetch = window.fetch.bind(window);
window.fetch = async (input, init) => {
  const res = await _rawFetch(input, init);
  const url = typeof input === "string" ? input : input.url;
  if (res.status === 401 && url.includes("/api/") && !url.includes("/api/auth/teacher/login")) {
    showTeacherLogin();
  }
  return res;
};

function showTeacherLogin(message) {
  teacherAuthed = false;
  if (typeof ws !== "undefined" && ws) { ws.onclose = null; ws.close(); }
  if (typeof fallbackPollTimer !== "undefined" && fallbackPollTimer) {
    clearInterval(fallbackPollTimer);
    fallbackPollTimer = null;
  }
  document.getElementById("teacher-login").classList.remove("hidden");
  const err = document.getElementById("teacher-login-error");
  err.textContent = message || "";
  err.classList.toggle("hidden", !message);
  setTimeout(() => document.getElementById("teacher-password").focus(), 50);
}

async function submitTeacherLogin(e) {
  e.preventDefault();
  const input = document.getElementById("teacher-password");
  const btn = document.getElementById("btn-teacher-login");
  btn.disabled = true;
  try {
    const res = await _rawFetch(`${window.location.origin}/api/auth/teacher/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ password: input.value })
    });
    if (!res.ok) {
      const data = await res.json().catch(() => ({}));
      showTeacherLogin(data.detail || "Gagal masuk.");
      return;
    }
    input.value = "";
    document.getElementById("teacher-login").classList.add("hidden");
    startDashboard();
  } finally {
    btn.disabled = false;
  }
}

async function teacherLogout() {
  await _rawFetch(`${window.location.origin}/api/auth/teacher/logout`, { method: "POST" });
  dashboardStarted = false;
  showTeacherLogin();
}

function startDashboard() {
  teacherAuthed = true;
  loadSessions();
  refreshAmbientState();
  if (!dashboardStarted) {
    dashboardStarted = true;
    connectWebSocket();
  } else if (!ws || ws.readyState > 1) {
    connectWebSocket();
  }
}

async function bootTeacher() {
  const res = await _rawFetch(`${window.location.origin}/api/auth/teacher/me`);
  if (res.ok) startDashboard();
  else showTeacherLogin();
}

document.addEventListener("DOMContentLoaded", bootTeacher);

// ---------------------------------------------------------------- class code ----

async function loadClassCode() {
  try {
    const res = await fetch(`${API_BASE}/api/auth/class-code`);
    if (!res.ok) return;
    const data = await res.json();
    classCodeState.code = data.class_code;
    const chip = document.getElementById("class-code-chip");
    chip.classList.toggle("hidden", !data.class_code);
    document.getElementById("class-code-value").textContent = data.class_code || "----";
    document.getElementById("class-code-big").textContent = data.class_code || "----";
  } catch (e) {
    console.error("class code:", e);
  }
}

async function studentUrls() {
  try {
    const res = await fetch(`${API_BASE}/api/auth/server-info`);
    if (res.ok) return await res.json();
  } catch (e) { /* fall through */ }
  return { student_urls: [`${window.location.origin}/student/`], opened_via_localhost: false };
}

async function openClassCodeView() {
  await loadClassCode();
  const info = await studentUrls();
  document.getElementById("class-code-url").textContent = info.student_urls[0] || `${window.location.origin}/student/`;
  document.getElementById("class-code-view").classList.remove("hidden");
}

function closeClassCodeView() {
  document.getElementById("class-code-view").classList.add("hidden");
}

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") closeClassCodeView();
});

// --------------------------------------------------------------- login cards ----

function formatShortTime(iso) {
  if (!iso) return "";
  const d = new Date(/[zZ]|[+-]\d\d:\d\d$/.test(iso) ? iso : iso + "Z");
  return isNaN(d) ? "" : d.toLocaleString("id-ID", { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" });
}

async function loadCardsTab() {
  const rows = document.getElementById("cards-student-rows");
  const summary = document.getElementById("cards-summary");
  rows.innerHTML = `<tr><td colspan="4" class="p-3 text-wolf">Memuat...</td></tr>`;
  try {
    const res = await fetch(`${API_BASE}/api/auth/students`);
    if (!res.ok) throw new Error("Gagal memuat daftar siswa");
    const list = await res.json();
    const withPin = list.filter(s => s.has_pin).length;
    const online = list.filter(s => s.device_active).length;
    summary.textContent = `${withPin}/${list.length} siswa punya kartu · ${online} perangkat sedang masuk`;

    rows.innerHTML = "";
    list.forEach(s => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td class="p-2.5 font-num">${escapeHtml(s.student_code)}</td>
        <td class="p-2.5">${s.has_pin
          ? `<span class="text-feather-shade">Ada</span> <span class="text-wolf font-semibold">· ${escapeHtml(formatShortTime(s.pin_set_at))}</span>`
          : `<span class="text-fox">Belum dibuat</span>`}</td>
        <td class="p-2.5">${s.device_active
          ? `<span class="text-macaw-shade">Masuk</span> <span class="text-wolf font-semibold">· ${escapeHtml(formatShortTime(s.last_login_at))}</span>`
          : `<span class="text-wolf">—</span>`}</td>
        <td class="p-2 text-right whitespace-nowrap">
          <button type="button" data-act="pin" class="px-2 py-1 rounded-lg text-[11px] font-extrabold text-macaw-shade hover:bg-macaw-soft">PIN baru</button>
          ${s.device_active ? `<button type="button" data-act="out" class="px-2 py-1 rounded-lg text-[11px] font-extrabold text-wolf hover:text-cardinal-shade hover:bg-cardinal-soft">Keluarkan</button>` : ""}
        </td>`;
      tr.querySelector('[data-act="pin"]').onclick = () => promptPrintOneCard(s.student_code, s.has_pin);
      const out = tr.querySelector('[data-act="out"]');
      if (out) out.onclick = () => promptLogoutDevice(s.student_code);
      rows.appendChild(tr);
    });
  } catch (err) {
    rows.innerHTML = `<tr><td colspan="4" class="p-3 text-cardinal-shade">${escapeHtml(err.message)}</td></tr>`;
  }
}

// The card page issues the PINs itself after a click there, so no popup hand-off or confirm is needed here.
function promptPrintAllCards() {
  openCardsPage("all");
}

function promptPrintOneCard(code) {
  openCardsPage(code);
}

function openCardsPage(codes) {
  const url = `/teacher/cards.html?codes=${encodeURIComponent(codes)}`;
  const win = window.open(url, "_blank");
  if (!win) window.location.href = url;
}

function promptLogoutDevice(code) {
  openConfirmModal({
    title: `Keluarkan perangkat ${code}?`,
    body: `${code} harus masuk lagi dengan PIN dan kode kelas.`,
    okLabel: "Ya, keluarkan",
    onConfirm: async () => {
      const res = await fetch(`${API_BASE}/api/auth/students/${encodeURIComponent(code)}/logout-device`, { method: "POST" });
      showToast(res.ok ? `Perangkat ${code} dikeluarkan.` : "Gagal mengeluarkan perangkat.", res.ok ? "success" : "error");
      loadCardsTab();
    }
  });
}
