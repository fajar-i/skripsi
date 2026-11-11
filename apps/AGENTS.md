# AGENTS.md — LogiTrace (RAG-KT) Project Directives & ECC Guidelines

> **Project:** LogiTrace — Web Evaluasi Formatif Adaptif Berbasis Knowledge Tracing & RAG dalam Pembelajaran Station Rotation untuk SMK TKJ  
> **Reference Specs:** `PRD-LogiTrace-RAG-KT.md` & `desain-final-rag-kt-logitrace.md`  
> **Target Environment:** Python 3.13 / FastAPI, PostgreSQL (pgvector) / SQLite dev fallback, Ollama Local CPU (`Qwen2.5-3B-Instruct-Q4_K_M`), Modern Web UI.

---

## 1. Core Operating Principles

1. **Deterministic Cognitive Engine (L3 Runtime < 1 ms):**
   - The cognitive state update ($m$) and probability estimation ($\hat{p}$) MUST be strictly deterministic and rule-based.
   - NEVER use LLM to predict student mastery or select items directly. The math engine handles all cognitive calculations.
   - Formulas:
     $$\hat{p}(q) = \sigma\big(\mathrm{logit}(m_{s, k_q}) + \theta_{d_q}\big), \quad \theta_1=+0.9, \ \theta_2=0.0, \ \theta_3=-0.9$$
     $$m \leftarrow \begin{cases} m + \alpha_d (1 - m) h, & \text{if } r = 1 \\ m - \gamma_d m, & \text{if } r = 0 \end{cases}$$
     Where $m \in [0.02, 0.98]$ (strictly clipped), $h=1.0$ (no hint) or $h=0.5$ (hint used).

2. **Zero Answer Leakage & Graceful Fallback:**
   - **T2 Socratic Hints** must adhere to *Guiding, Not Solving* (max 60 words).
   - Regex-based Leakage Guard is mandatory. Any hint containing direct answer tokens or leakage phrasing must be dropped immediately.
   - If LLM response exceeds 3.0 seconds, instant fallback (< 50 ms) to curated static hint bank is required.

3. **Strict Audit Trail (Append-Only):**
   - The `interactions` table is append-only. SQL `UPDATE` and `DELETE` queries are strictly prohibited on interaction logs.
   - Cold-start calibration items 1–6 must have `is_calibration = TRUE` and be excluded from E3 predictive accuracy calculations.

4. **Test-Driven Development (TDD):**
   - Write tests first for all cognitive formulas, ZPD item selection, and guardrail verification before writing production code.
   - Maintain $\ge 85\%$ test coverage for core business logic.

---

## 2. Agent Roles & Delegation

| Agent | Scope in LogiTrace |
|:---|:---|
| `rag-pipeline-reviewer` | Review vector embeddings, retrieval pipeline, and RAGAS / leakage guard verification. |
| `fastapi-reviewer` | Review FastAPI router endpoints, async dependency injection, Pydantic schemas, and WebSocket management. |
| `database-reviewer` | Review PostgreSQL / pgvector schemas, append-only integrity, index performance, and migration scripts. |
| `tdd-guide` | Ensure all math engine and guardrail components follow rigorous Red-Green-Refactor cycles. |
| `security-reviewer` | Audit API input sanitization, token validation, rate-limiting, and error message masking. |
| `eval-harness` | Execute and verify empirical evaluation scripts E1 through E6 against KPI targets. |

---

## 3. Directory & Component Conventions

```text
logitrace/
├── data/              # L1 Knowledge Base (12 KCs, DAG, 5 TOLT) & L2 Seed Items
├── backend/app/       # FastAPI app, L3 deterministic engine, RAG triggers, DB models
├── frontend/          # Student mobile-first quiz & Teacher ambient dashboard
├── evals/             # Verification pipelines E1 - E6
└── tests/             # Pytest suite for deterministic logic and guardrails
```
