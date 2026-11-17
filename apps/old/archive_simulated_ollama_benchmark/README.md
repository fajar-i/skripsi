# ⚠️ SIMULATED BENCHMARK OUTPUT — INVALID

`benchmark_concurrency_ollama.py` silently switched to a random-number simulation
(`simulate_cpu_concurrency_latency`) when Ollama was not reachable. The run saved here
was produced in that mode (the report says `Mode Eksekusi: Validated CPU Queuing Benchmark`).

The latency, CPU and RAM numbers in these files do **not** come from a language model.
They were used for Tables 4–5 of the 12 Nov draft article and must be removed from it.

LogiTrace no longer has an Ollama mode. The replacement benchmark is
`logitrace/evals/benchmark_concurrency_9router.py` (path dari folder `apps/`), which fails if 9router is unreachable
instead of simulating.
