"""
LogiTrace: Concurrency benchmark for Socratic hints (T2) through 9router.

Exercises the PRODUCTION code path (HintService.generate_socratic_hint): PII scrub ->
9router call with a hard 3.0 s deadline -> leakage guard -> static fallback.
Latency is the total time the student waits, including any failed LLM attempt.

There is NO simulation mode. The script aborts if 9router is unreachable or the key is missing.

Each batch fires k requests at the same instant (burst), using real items from the bank.

Usage:
    python evals/benchmark_concurrency_9router.py --levels 1 2 4 8 17 --requests 100 --repeats 3

Outputs (evals/results/):
    concurrency_9router_<stamp>.jsonl   one line per request (raw data)
    concurrency_9router_<stamp>.json    summary per k and per repeat, with Wilson 95% CIs
"""

import argparse
import asyncio
import json
import math
import os
import platform
import random
import statistics
import sys
import time
from collections import Counter
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, ROOT)

import httpx  # noqa: E402

from backend.app.rag.hint_service import HintService  # noqa: E402

DATA = os.path.join(ROOT, "data")
SLA_SECONDS = 3.0


def wilson_ci(successes: int, n: int, z: float = 1.96):
    if n == 0:
        return (None, None)
    p = successes / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (round(max(0.0, centre - half), 4), round(min(1.0, centre + half), 4))


def percentile(sorted_vals, p):
    if not sorted_vals:
        return None
    idx = min(len(sorted_vals) - 1, int(round(p / 100.0 * (len(sorted_vals) - 1))))
    return sorted_vals[idx]


async def preflight(service: HintService):
    client = service.client
    if not client.api_key:
        raise SystemExit("ABORT: NINEROUTER_API_KEY is not set. No simulation fallback exists.")
    base = client.endpoint_url.rsplit("/chat/completions", 1)[0]
    try:
        async with httpx.AsyncClient(timeout=5.0) as http:
            r = await http.get(f"{base}/models", headers={"Authorization": f"Bearer {client.api_key}"})
    except Exception as e:
        raise SystemExit(f"ABORT: 9router unreachable at {base} ({e}).")
    if r.status_code != 200:
        raise SystemExit(f"ABORT: 9router /models returned HTTP {r.status_code}.")
    text, _, err = await client.call_chat("Jawab singkat.", "Sebutkan satu standar Wi-Fi.", max_tokens=20,
                                          timeout_seconds=15.0)
    if err or not text:
        raise SystemExit(f"ABORT: test completion failed: {err or 'empty response'}")


async def one_request(service, item, level, kc_names, kc_desc, meta):
    ans = item["options"][item["correct_answer"]]
    t0 = time.perf_counter()
    hint, source, svc_ms, reason = await service.generate_socratic_hint(
        kc_id=item["primary_kc"],
        kc_name=kc_names.get(item["primary_kc"], item["primary_kc"]),
        level=level,
        prompt_text=item["prompt_text"],
        correct_answer_text=ans,
        options=item["options"],
        timeout_seconds=SLA_SECONDS,
        kc_description=kc_desc.get(item["primary_kc"]),
    )
    wall_ms = (time.perf_counter() - t0) * 1000.0
    return {
        **meta,
        "item_id": item["id"],
        "hint_level": level,
        "source": source,
        "fallback_reason": reason,
        "wall_ms": round(wall_ms, 2),
        "service_ms": svc_ms,
        "hint_words": len(hint.split()),
        "hint_text": hint,
        "ts_utc": datetime.now(timezone.utc).isoformat(),
    }


def summarize(rows):
    n = len(rows)
    lat = sorted(r["wall_ms"] / 1000.0 for r in rows)
    llm_ok = sum(1 for r in rows if r["source"] == "llm_9router")
    within_sla = sum(1 for r in rows if r["wall_ms"] / 1000.0 <= SLA_SECONDS + 0.05)
    reasons = Counter((r["fallback_reason"] or "").split(" (")[0] for r in rows if r["source"] != "llm_9router")
    return {
        "n": n,
        "latency_s": {
            "mean": round(statistics.fmean(lat), 3),
            "sd": round(statistics.stdev(lat), 3) if n > 1 else 0.0,
            "p50": round(percentile(lat, 50), 3),
            "p95": round(percentile(lat, 95), 3),
            "max": round(lat[-1], 3),
        },
        "llm_served": llm_ok,
        "llm_served_rate": round(llm_ok / n, 4),
        "llm_served_rate_ci95": wilson_ci(llm_ok, n),
        "fallback_rate": round((n - llm_ok) / n, 4),
        "fallback_rate_ci95": wilson_ci(n - llm_ok, n),
        "wait_within_3_05s": within_sla,
        "wait_within_3_05s_rate": round(within_sla / n, 4),
        "fallback_reasons": dict(reasons),
    }


async def main_async(args):
    rng = random.Random(args.seed)
    with open(os.path.join(DATA, "l2_item_bank", "items_adaptive_180.json"), encoding="utf-8") as f:
        items = json.load(f)
    with open(os.path.join(DATA, "l1_knowledge_base", "kcs.json"), encoding="utf-8") as f:
        kcs = json.load(f)
    kc_names = {k["id"]: k["name"] for k in kcs}
    kc_desc = {k["id"]: k.get("description") for k in kcs}

    service = HintService()
    await preflight(service)

    for _ in range(args.warmup):
        it = rng.choice(items)
        await one_request(service, it, 1, kc_names, kc_desc, {"phase": "warmup"})

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    raw_path = os.path.join(HERE, "results", f"concurrency_9router_{stamp}.jsonl")
    all_rows = []

    with open(raw_path, "w", encoding="utf-8") as raw:
        for rep in range(1, args.repeats + 1):
            for k in args.levels:
                batches = math.ceil(args.requests / k)
                for b in range(batches):
                    batch_items = [rng.choice(items) for _ in range(k)]
                    levels = [rng.choice((1, 2, 3)) for _ in range(k)]
                    meta = {"phase": "measure", "repeat": rep, "k": k, "batch": b + 1}
                    rows = await asyncio.gather(*[
                        one_request(service, it, lv, kc_names, kc_desc, {**meta, "slot": i + 1})
                        for i, (it, lv) in enumerate(zip(batch_items, levels))
                    ])
                    for r in rows:
                        raw.write(json.dumps(r, ensure_ascii=False) + "\n")
                    all_rows.extend(rows)
                    await asyncio.sleep(args.pause)
                print(f"repeat {rep} k={k}: {batches * k} requests done")

    summary = {
        "benchmark": "concurrency_9router",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "endpoint": service.client.endpoint_url,
        "model": service.client.model_name,
        "sla_seconds": SLA_SECONDS,
        "arrival_pattern": "burst: k simultaneous requests per batch",
        "params": vars(args),
        "host": {"platform": platform.platform(), "python": platform.python_version()},
        "raw_file": os.path.basename(raw_path),
        "per_k": {},
        "per_k_per_repeat": {},
    }
    for k in args.levels:
        rows_k = [r for r in all_rows if r["k"] == k]
        summary["per_k"][str(k)] = summarize(rows_k)
        summary["per_k_per_repeat"][str(k)] = {
            str(rep): summarize([r for r in rows_k if r["repeat"] == rep]) for rep in range(1, args.repeats + 1)
        }

    sum_path = raw_path.replace(".jsonl", ".json")
    with open(sum_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print()
    print(f"{'k':>3} {'n':>5} {'mean s':>7} {'p95 s':>7} {'LLM %':>7} {'95% CI':>17}")
    for k, s in summary["per_k"].items():
        lo, hi = s["llm_served_rate_ci95"]
        print(f"{k:>3} {s['n']:>5} {s['latency_s']['mean']:>7.3f} {s['latency_s']['p95']:>7.3f} "
              f"{s['llm_served_rate'] * 100:>6.1f}% [{lo * 100:5.1f}, {hi * 100:5.1f}]")
    print(f"Raw:     {raw_path}\nSummary: {sum_path}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--levels", type=int, nargs="+", default=[1, 2, 4, 8, 17])
    ap.add_argument("--requests", type=int, default=100, help="requests per k per repeat")
    ap.add_argument("--repeats", type=int, default=3)
    ap.add_argument("--warmup", type=int, default=3)
    ap.add_argument("--pause", type=float, default=0.5, help="seconds between batches")
    ap.add_argument("--seed", type=int, default=42)
    asyncio.run(main_async(ap.parse_args()))


if __name__ == "__main__":
    main()
