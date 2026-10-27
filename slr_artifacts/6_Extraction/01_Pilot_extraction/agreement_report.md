## Pilot agreement results

Both comparisons pass the §9 gate on every tier, with pooled AC1 ≥ 0.8. Data: 5 pilot studies, all coded under slr-data-model 0.10.0, scored with `agreement.py` using the rules above. LLM: glm-5.3, run on 2026-10-26.

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|Comparison|Tier|Items|Raw agreement|AC1|Fields failing|
|R1 vs R2|Descriptive|740|0.901|0.864|5 of 34|
|R1 vs R2|Interpretive|200|0.870|0.819|3 of 17|
|R1 vs R2|Reproducibility|30|0.900|0.877|1 of 6|
|LLM vs R1/R2 consensus|Descriptive|735|0.941|0.919|3 of 33|
|LLM vs R1/R2 consensus|Interpretive|200|0.925|0.897|2 of 17|
|LLM vs R1/R2 consensus|Reproducibility|30|0.867|0.834|1 of 6|

Fields that fail the gate (raw agreement < 0.8 in every case):

- **R1 vs R2 (9 of 57):** authors_claimed_tier, system_configuring_decision_stated, open_weight, formalization_level, evaluation_paradigm, Q1 methodological transparency, Q3 validity and limitation discussion, Q4 positioning against prior work (raw 0.2), prompts_disclosed.
- **LLM vs consensus (6 of 56):** open_weight, optimization_tradition_present, formalization_level, decision_autonomy, Q4 positioning against prior work (raw 0.2), decoding_params_reported.
- **Failing in both:** open_weight, formalization_level and Q4. These fields need clearer coding rules before full extraction.

With 5 studies, a single-value field rests on 5 items, so one disagreement moves its raw agreement by 0.2. retrieval_traceability.source is not scored for the LLM.