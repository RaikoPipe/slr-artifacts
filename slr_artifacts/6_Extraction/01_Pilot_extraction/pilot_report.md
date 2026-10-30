# Pilot Extraction Report (Stage 1)

**Date:** 2026-10-27
**Outcome:** The §9 agreement gate is passed. After one rule revision (schema 0.10.1) and a follow-up revision (0.10.2), the LLM pre-fill (glm-5.3) meets AC1 ≥ 0.8 on every tier against the R1/R2 consensus, and no field fails. Full extraction may proceed under slr-data-model 0.10.2.

Protocol: extraction instructions v5.1 (`instructions/extraction_instructions_v5_1.md`). Scoring rules and deviations: pre-registration amendment of 2026-10-26/27. Rule changes per schema version: slr-data-model README, "Version".

## Setup

| Item | Value |
|---|---|
| Sample | 5 representative sources (Zotero collection `representatives`) |
| Human coders | R1 and R2, independent; tagged `H` |
| LLM | glm-5.3 (Ollama cloud), temperature 0, one call per field group over the docprep full text |
| Agreement tool | `agreement.py` (langgraph-literature-workflows); Gwet's AC1 and raw agreement per field, pooled per tier |
| Scored fields | 57 categorical fields (56 for the LLM: `retrieval_traceability.source` is human-filled); free-text and continuous fields not scored |
| Tiers | descriptive (34 fields), interpretive (17), reproducibility (6) |
| Gate | pooled tier AC1 ≥ 0.8; a field fails if its raw agreement is < 0.8, or if its own AC1 and its tier's AC1 are both < 0.8 |

## Results

### R1 vs R2 (schema 0.10.0)

| Tier | Items | Raw | AC1 | Fields failing |
|---|---|---|---|---|
| Descriptive | 740 | 0.901 | 0.864 | 5 of 34 |
| Interpretive | 200 | 0.870 | 0.819 | 3 of 17 |
| Reproducibility | 30 | 0.900 | 0.877 | 1 of 6 |

Failing fields (9): `authors_claimed_tier`, `system_configuring_decision_stated`, `open_weight`, `formalization_level`, `evaluation_paradigm`, Q1, Q3, Q4, `prompts_disclosed`. Each triggered an instruction revision (§9), made in 0.10.1. Human agreement was not re-measured after the revision. Per-field table and disagreements: `v0.10.0/agreement_r1_vs_r2_v0.10.0.{csv,txt}`.

### LLM vs R1/R2 consensus

| Tier | Pilot (0.10.0) | Re-pilot (0.10.1) | Re-pilot (0.10.2) | Raw (0.10.2) |
|---|---|---|---|---|
| Descriptive | 0.919 | 0.943 | **0.947** | 0.962 |
| Interpretive | 0.897 | 0.846 | **0.903** | 0.930 |
| Reproducibility | 0.834 | 1.000 | **0.959** | 0.967 |
| Fields failing | 6 of 56 | 1 of 56 | **0 of 56** | |

Pilot and the 0.10.1 re-pilot were scored against the consensus as it stood at the time; the 0.10.2 re-pilot against the consensus reviewed under 0.10.2 (`v0.10.2/consensus_extraction.ods`). Per-field tables and disagreement lists for each run are in the matching `v0.10.x/` folder (see Artifacts).

- **Pilot failures (6):** `open_weight`, `optimization_tradition_present`, `formalization_level`, `decision_autonomy`, Q4 (raw 0.2), `decoding_params_reported`. All pass after 0.10.1.
- **0.10.1 re-pilot:** only Q2 failed (raw 0.6). Its rule had not been revised, so under §9 it received one revision (0.10.2) and a second re-pilot instead of reverting to manual extraction.
- **0.10.2 re-pilot:** no failing field. Eight fields sit exactly at raw 0.8 (one disagreement in five): Q2, Q3, Q4, `system_configuring_decision`, `research_type`, `llm_as_judge`, `efficiency_metrics_reported`, `prompts_disclosed`.

## Rule revisions

| Version | Change |
|---|---|
| 0.10.1 | Clarified definitions of the 12 fields below the gate in either comparison; placeholder reasoning (`...`) rejected so the LLM retries; `H` tag covers AI-assisted human extraction |
| 0.10.2 | From the R1/R2 review of the consensus: Q1 counts details in an explicitly cited publication and does not count confidential company data as missing; Q2 applies only the criterion of the derived study-type category, with anchors for category A; selecting network members counts as a stated system-configuring decision; naturalistic evaluation rests on real operational data or real users of the organisation's own system |

No vocabulary or type changed, so 0.10.0 records stay structurally valid.

## Consensus corrections under the revised rules

| Study | Field | 0.10.0 | 0.10.2 |
|---|---|---|---|
| 10.1145/3742413.3789061 | `authors_claimed_tier` | Strategic | NA |
| 10.1145/3742413.3789061 | `system_configuring_decision_stated` | FALSE | TRUE |
| 10.2139/ssrn.5370043 | Q3 | Yes | Partially |
| all | `schema_version` | 0.10.0 | 0.10.2 |

`evaluation_paradigm` of 10.1016/j.jmsy.2026.02.015 stays `both` under the 0.10.2 rule. The 0.10.0 consensus is kept unchanged in `v0.10.0/`.

## Notes for full extraction

- **Run-to-run variance:** with identical rules, several LLM fields moved by 0.2 between runs (Q2 went 1.0 → 0.6). 
- **Q2 category:** the `quality_appraisal` call does not receive the extracted `validation_status`, so the LLM re-derives the study-type category; in one study it read an implemented-validated study as a demonstration (category B). R1/R2 dual verification of Q2 must check the category.
- **Placeholder reasoning:** glm-5.3 returned `...` for whole reasoning groups; validation now rejects it and the group is retried.

## Artifacts

| Path | Content |
|---|---|
| `v0.10.0/r1_retrieval.ods`, `v0.10.0/r2_retrieval.ods` | R1 and R2 pilot extractions |
| `v0.10.0/extraction_review_r1_r2_final.xlsx` | R1/R2 disagreement review producing the consensus |
| `v0.10.0/consensus_extraction.ods` | Consensus as first agreed |
| `v0.10.2/consensus_extraction.ods` | Consensus reviewed under 0.10.2 (reference for the gate) |
| `v0.10.0/agreement_r1_vs_r2_v0.10.0.{csv,txt}` | R1 vs R2 agreement: per-field table (`.csv`) and report with disagreements (`.txt`) |
| `agreement_report.md`, `v0.10.0/agreement_llm_vs_*_retrieval_v0.10.0.{csv,txt}`, `v0.10.0/agreement_llm_vs_consensus_extraction_v0.10.0.{csv,txt}` | First-pilot agreement results (0.10.0) |
| `v0.10.1/agreement_llm_vs_consensus_repilot_v0.10.1.{csv,txt}` | LLM re-pilot under 0.10.1 vs. consensus: per-field table (`.csv`) and report with disagreements (`.txt`) |
| `v0.10.2/agreement_llm_vs_consensus_repilot_v0.10.2.{csv,txt}` | LLM re-pilot under 0.10.2 vs. `v0.10.2/consensus_extraction.ods` (gate decision) |
| `v0.4.0/` – `v0.9.0/` | Earlier extraction iterations, by schema version |

LLM outputs are kept in langgraph-literature-workflows under `outputs/` (0.10.2 re-pilot) and `outputs/archive/glm-5.3_pilot1/`, `outputs/archive/glm-5.3_repilot_0.10.1/`.
