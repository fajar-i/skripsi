# ⚠️ SIMULATED — NOT RESEARCH RESULTS

Every script in this folder generates its "data" with random numbers
(`np.random`, mock LLM responses, synthetic students). This includes rater scores,
SUS questionnaires, pre/post-tests and N-Gain.

`evaluation_report_SIMULATED.json` is the output of those scripts. **Never cite these
numbers as findings** in the thesis, the article, or any report.

These scripts are kept only as analysis templates. Use them to check that the analysis
code runs, then replace the generators with real data collected from experts, teachers
or students under an approved protocol.

Reproducible technical benchmarks live one level up:
`evals/benchmark_l3_engine.py` and `evals/benchmark_concurrency_9router.py`.
