"""
LogiTrace: Reproducible micro-benchmark for the deterministic L3 engine and the static fallback.

Measures (per operation, in milliseconds):
  1. math      : p_hat + mastery update + on-read decay for one response
  2. zpd_select: ZPD selection with DAG gating over the full 180-item bank
  3. fallback  : static hint lookup including the answer-leakage guard

Usage:
    python evals/benchmark_l3_engine.py [--iterations 10000] [--seed 42]

Writes evals/results/l3_engine_<timestamp>.json with raw summary statistics and host metadata.
No network calls.
"""

import argparse
import json
import os
import platform
import random
import statistics
import sys
import time
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, ROOT)

from backend.app.engine.cognitive import (  # noqa: E402
    apply_temporal_decay,
    calculate_predicted_p,
    update_mastery,
)
from backend.app.engine.zpd_selector import ItemCandidate, ZPDSelector  # noqa: E402
from backend.app.rag.hint_service import HintService  # noqa: E402

DATA = os.path.join(ROOT, "data")


def summarize(samples_ms):
    s = sorted(samples_ms)
    n = len(s)

    def pct(p):
        return s[min(n - 1, int(round(p / 100.0 * (n - 1))))]

    return {
        "n": n,
        "mean_ms": round(statistics.fmean(s), 5),
        "sd_ms": round(statistics.stdev(s), 5) if n > 1 else 0.0,
        "p50_ms": round(pct(50), 5),
        "p95_ms": round(pct(95), 5),
        "p99_ms": round(pct(99), 5),
        "max_ms": round(s[-1], 5),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--iterations", type=int, default=10000)
    ap.add_argument("--warmup", type=int, default=200)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    rng = random.Random(args.seed)

    with open(os.path.join(DATA, "l1_knowledge_base", "dag_prerequisites.json"), encoding="utf-8") as f:
        dag = json.load(f)
    with open(os.path.join(DATA, "l2_item_bank", "items_adaptive_180.json"), encoding="utf-8") as f:
        items = json.load(f)

    kc_ids = list(dag["in_degrees"].keys())
    selector = ZPDSelector(dag["edges"])
    candidates = [
        ItemCandidate(id=it["id"], primary_kc=it["primary_kc"], difficulty=it["difficulty"],
                      is_calibration=it["is_calibration"])
        for it in items
    ]
    hint_service = HintService()

    def one_math():
        m = rng.uniform(0.02, 0.98)
        d = rng.choice((1, 2, 3))
        t0 = time.perf_counter()
        m_read = apply_temporal_decay(m, rng.uniform(0, 30))
        calculate_predicted_p(m_read, d)
        update_mastery(m_read, rng.choice((0, 1)), d, used_hint=rng.random() < 0.3)
        return (time.perf_counter() - t0) * 1000.0

    def one_select():
        mastery = {k: rng.uniform(0.02, 0.98) for k in kc_ids}
        answered = {c.id for c in rng.sample(candidates, rng.randint(6, 20))}
        last_kc = rng.choice(kc_ids)
        t0 = time.perf_counter()
        selector.select_next_item(candidates, mastery, answered, last_kc_id=last_kc)
        return (time.perf_counter() - t0) * 1000.0

    def one_fallback():
        it = rng.choice(items)
        lvl = rng.choice((1, 2, 3))
        ans = it["options"][it["correct_answer"]]
        t0 = time.perf_counter()
        hint_service.get_static_fallback_hint(it["primary_kc"], lvl, ans, it["options"])
        return (time.perf_counter() - t0) * 1000.0

    results = {}
    for name, fn in (("math", one_math), ("zpd_select", one_select), ("fallback", one_fallback)):
        for _ in range(args.warmup):
            fn()
        results[name] = summarize([fn() for _ in range(args.iterations)])

    out = {
        "benchmark": "l3_engine",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "iterations": args.iterations,
        "warmup": args.warmup,
        "seed": args.seed,
        "item_bank_size": len(items),
        "host": {
            "platform": platform.platform(),
            "processor": platform.processor(),
            "python": platform.python_version(),
            "cpu_count_logical": os.cpu_count(),
        },
        "results": results,
    }

    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(HERE, "results", f"l3_engine_{stamp}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    for name, r in results.items():
        print(f"{name:11s} mean={r['mean_ms']:.4f} ms  p95={r['p95_ms']:.4f} ms  p99={r['p99_ms']:.4f} ms  (n={r['n']})")
    print(f"Saved: {path}")


if __name__ == "__main__":
    main()
