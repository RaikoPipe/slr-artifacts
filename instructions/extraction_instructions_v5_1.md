# Extractor Instructions — LLM-Based Decision Support for the Strategic Planning Horizon in Manufacturing and Logistics

**Version:** 5.1
**Schema:** slr-data-model 0.10.2 (every record stores the `schema_version` it was coded under)
**Project:** https://github.com/RaikoPipe/slr-artifacts
**Scope:** SLR on LLM-based decision support at the strategic and upper-tactical manufacturing and logistics planning horizon.
**Subdomains:** Factory planning (VDI 5200), SC network design, strategic logistics/distribution network design, technology selection & investment appraisal, GPN design.
**Reviewer roles:** R1 (primary researcher), R2 (fellow researcher), R3 (supervisor / adjudicator).

---

## 1. Extraction Tiers

| Tier | Fields | Method | Verification |
|------|--------|--------|--------------|
| **Bibliographic metadata** | DOI, title, authors, affiliations, country, year, venue, venue type, language, funding source | Imported from search-stage records via Zotero; affiliations, country and funding read from the PDF by the LLM; gaps filled by R1 | R1 spot-checks 10% against title page |
| **Descriptive fields** | Study characterization, strategic planning scope, LLM/AI intervention, OR substrate, evaluation & outcomes, retrieval traceability (human-filled) | LLM pre-fill | R1 verifies 100% against source text |
| **Interpretive fields** | Gap indicators, quality appraisal Q1–Q4, validation status, system-configuring decision | LLM-extracted with reasoning + evidence locator | R1 and R2 each verify 100%, blind to each other (§7) |
| **Reproducibility fields** | Quality appraisal reproducibility items (model version, prompts, decoding parameters, code, data, run date) | LLM-extracted with reasoning + evidence locator | As interpretive; pooled as their own tier for agreement (§9) |

Field-level tier membership follows slr-data-model (`REPRODUCIBILITY_FIELDS`; interpretive fields ask for a verbatim anchor in their reasoning).

---

## 2. Workflow

1. Open source PDF and the extraction workbook (`retrieval_v2.ods`: `studies`, `reported_metrics` and `meta` sheets).
2. **Bibliographic tier:** fill fields missing from the imported record; spot-check 10% against the title page.
3. **Descriptive tier:** verify each LLM-prefilled value against source text; correct or confirm using the provenance protocol (§8).
4. **Interpretive tier:** verify each LLM value and its reasoning against the source per §7 (R1 and R2 separately).
5. Log page/section reference for every numeric metric.
6. Record uncertainties in the affected field's `_reasoning` column; escalate ambiguous cases per §10.
7. Save after each source; commit to the GitHub repository daily.

---

## 3. Field-by-Field Rules

Full field definitions and JSON schema: <https://github.com/RaikoPipe/slr-data-model>. Rule changes per version are listed in its changelog (README, "Version"); rules revised after the extraction pilot are tagged `(pilot 0.10.1)` or `(0.10.2)` in the field descriptions.

## 4. Data Format

- **Primary table:** tidy data — one row per study, one column per field.
- **Multi-valued fields** (e.g., multiple LLM models per study): separate long-format table linked by study ID.
- **Not reported vs. not applicable:** use `NR` for missing data, `NA` for structurally inapplicable fields. Never leave cells blank.
- **Reasoning columns:** every extracted field `<field>` has a `<field>_reasoning` column (replaces the former `notes` column): justification + evidence locator (page/section; for interpretive fields also a short verbatim anchor). Filled by the LLM; verifiers append their own reasoning when correcting or flagging. Fields already named `*_rationale` in the schema serve this role. Placeholder reasoning (e.g., `...`) is invalid.
- **Output format:** structured JSON conforming to the schema at <https://github.com/RaikoPipe/slr-data-model>. Raw LLM output validated against the schema before human review; schema-invalid outputs flagged and re-extracted.

---

## 5. Controlled Vocabularies

Full vocabularies: <https://github.com/RaikoPipe/slr-data-model>

---

## 6. Handling Ambiguity

- **Ranges:** capture both endpoints + context.
- **Conditional values:** capture all values with conditions.
- **Contradictions within source:** extract both values, flag in the field's `_reasoning`, escalate.
- **Uncertainty about field assignment:** mark field with `?` suffix, explain in `_reasoning`, adjudicate.
- **Subdomain boundary cases:** if a paper spans tactical and strategic tasks, include only if a strategic task is explicitly addressed (i.e., `Strategic` is among the planning horizon tiers addressed); record all tiers addressed and document the reasoning in the horizon rationale.
- **Outlier metrics** (> 2× the range of other sources for the same metric type): flag, verify, report with context — do not exclude.

---

## 7. LLM Extraction Pipeline

### Input preparation

- Full-text PDF converted to markdown via **docprep** (docling with OCR fallback; settings in `docprep.yaml` of langgraph-literature-workflows).
- **Bibliographic fields:** imported from Zotero; only affiliations, country and funding are read from the PDF by the LLM (§1).
- **Descriptive, interpretive and reproducibility fields:** each field group is extracted in its own call over the same full text; the LLM returns value + `_reasoning` per field. Model and settings are recorded in the run log.

### Output validation

- LLM output is structured JSON conforming to the schema.
- Schema-invalid output is retried; groups that stay invalid are listed in the record's `failed_groups` and re-extracted before human review.

### Verification protocol

For each LLM-prefilled field:

1. Locate the claim in the source PDF.
2. If verified → mark `verified=Y` in provenance column.
3. If incorrect → overwrite value, mark `verified=corrected`, log original in `llm_raw` column.
4. If unverifiable → mark `verified=unverifiable`, escalate.

**Interpretive fields (dual verification):**

1. R1 and R2 verify in separate copies of the extraction table; neither sees the other's verdicts until both are done.
2. Verify against the cited evidence locator, not the reasoning alone: the value must follow from the source under the field rule.
3. For absence values (`N`, `none`, score 1), run a targeted full-text search (field keywords + synonyms) before confirming; absence claims are where LLM errors are hardest to spot.
4. Each verifier records `verified=Y/corrected/unverifiable` and, if corrected, their own value + reasoning.
5. Merge: identical final values → accepted (tag `L-V` or `L-C`). Differing values → R1–R2 discussion → R3 (§10). Log outcome in `_reasoning`.

Report count of LLM errors per field type at the end of each extraction session. If ≥ 3 same-type LLM errors are detected, refine the prompt, re-extract affected records, and update the pre-registration.

---

## 8. Provenance Tagging

Every extracted field receives a provenance tag:

| Tag | Meaning |
|-----|---------|
| `M` | Imported from search-stage metadata |
| `H` | The reviewer decides the value; a general-purpose AI assistant may have been used for evidence location, verification and phrasing (disclosed per reviewer). |
| `L-V` | LLM extracted, human verified |
| `L-C` | LLM extracted, human corrected |
| `D` | Dual-reviewer extraction |

Record the verifier(s) in `verified_by` (e.g., `R1;R2`).

---

## 9. Pilot Extraction (Stage 1)

- **Sample:** 5 representative sources.
- **Procedure:** R1 and R2 independently extract all descriptive, interpretive and reproducibility fields manually, blind to LLM output; a general-purpose AI assistant is permitted (tag `H`, §8). LLM pipeline runs in parallel on the same fields. Bibliographic fields are imported and not piloted.
- **Agreement:** assessed between R1–R2 and between human–LLM per field type, with `agreement.py` (langgraph-literature-workflows); scoring rules are in its docstring and the pre-registration amendment.
- **Thresholds:** Gwet's AC1 ≥ 0.8 on categorical fields only; free-text and continuous fields are not scored. Multi-valued categorical fields (e.g., planning horizon tiers) are assessed per value (present/absent). Report raw agreement alongside AC1. With 5 sources, AC1 is computed per field and, as the gating figure, pooled per tier (descriptive / interpretive / reproducibility); per-field values are reported but a single field fails the gate only if its pooled tier also fails or the field's raw agreement is < 80%. Only reviews coded under the same schema vocabulary are compared.
- **LLM gate:** LLM vs. R1–R2 consensus agreement reported per field, separately per tier; human-filled fields (retrieval traceability) are not scored. An interpretive field below threshold after one prompt revision and re-pilot reverts to manual R1 extraction with 100% R2 verification.
- **Outcome:** pilot results frozen in pre-registration update before full extraction proceeds. Instruction revisions triggered if thresholds unmet.

---

## 10. Escalation

Escalate to R3 when:

- R1 and R2 disagree after one discussion round.
- Source contradicts itself on a key field.
- Subdomain classification or strategic-scope determination is genuinely ambiguous (document reasoning in the field's `_reasoning`).
- Self-authored paper: R1 excluded; R2 independently verifies all tiers; disagreements with the LLM value that R2 cannot resolve go to R3.

---

## 11. Session Rules

- **Max 2 hours** per session (fatigue → errors).
- Log start/end time per session.
- No extraction under time pressure; defer rather than guess.
