# Extractor Instructions — LLM-Based Decision Support for the Strategic Planning Horizon in Manufacturing and Logistics

**Version:** 5.0 
**Project:** https://github.com/RaikoPipe/slr-artifacts
**Scope:** SLR on LLM-based decision support at the strategic and upper-tactical manufacturing and logistics planning horizon.
**Subdomains:** Factory planning (VDI 5200), SC network design, strategic logistics/distribution network design, technology selection & investment appraisal, GPN design.
**Reviewer roles:** R1 (primary researcher), R2 (fellow researcher), R3 (supervisor / adjudicator).

---

## 1. Extraction Tiers

| Tier | Fields | Method | Verification |
|------|--------|--------|--------------|
| **Bibliographic metadata** | DOI, title, authors, affiliations, country, year, venue, venue type, language, funding source | Imported from search-stage records (Scopus / WoS / OpenAlex); gaps filled by R1 | R1 spot-checks 10% against title page |
| **Descriptive fields** | Study characterization, strategic planning scope, LLM/AI intervention, OR substrate, evaluation & outcomes, retrieval traceability | LLM pre-fill | R1 verifies 100% against source text |
| **Interpretive fields** | Gap indicators, quality appraisal, VDI 5200 phase mapping, validation-status judgments | LLM-extracted with reasoning + evidence locator | R1 and R2 each verify 100%, blind to each other (§7) |

---

## 2. Workflow

1. Open source PDF and extraction table (`extraction_table.csv`).
2. **Bibliographic tier:** fill fields missing from the imported record; spot-check per §3.1.
3. **Descriptive tier:** verify each LLM-prefilled value against source text; correct or confirm using the provenance protocol (§8).
4. **Interpretive tier:** verify each LLM value and its reasoning against the source per §7 (R1 and R2 separately).
5. Log page/section reference for every numeric metric.
6. Record uncertainties in the affected field's `_reasoning` column; escalate ambiguous cases per §10.
7. Save after each source; commit to the GitHub repository daily.

---

## 3. Field-by-Field Rules

Full field definitions and JSON schema: <https://github.com/RaikoPipe/slr-data-model>

### 3.1 Bibliographic metadata (imported from search-stage records; R1 spot-check 10%)

- Source: deduplicated search records (OpenAlex for snowballed records), joined by DOI or record ID. Not LLM-extracted.
- Fields missing in the record: R1 fills from the title page, else `NR`.

- **DOI, title, authors, affiliations, country of corresponding author, year, venue, language:** verify against source header/footer.
- **Venue type:** Scimago Q1–Q4 journal (lookup current year) · conference proceedings · Tier 1 preprint (institutional affiliation confirmed) · grey literature.
- **Funding source:** as reported; `NR` if absent.
- **Self-authored flag:** `Y` if any review author appears in author list.

### 3.2 Study characterization (LLM pre-fill; R1 verifies 100%)

- **Research type:** empirical / conceptual / design-science.
- **Validation status:**

| Value | Definition |
|-------|------------|
| `implemented-validated` | Working system + evaluation under a defined protocol with defined metrics (benchmark, case study with quantitative metrics, user study) |
| `prototype` | Working system demonstrated on illustrative case(s) or a single walkthrough without defined metrics |
| `framework-only` | Architecture described, no implementation |
| `conceptual` | Position or vision paper |

- Validation status is an **interpretive** field (§1): LLM-extracted, R1 + R2 verify 100%. It fixes the quality-appraisal category (§3.9).
- **Industry sector** and **case study domain:** as reported.
- **Stated research questions:** verbatim or close paraphrase of the paper's RQs; `NR` if none stated.

### 3.3 Strategic planning scope (LLM pre-fill; R1 verifies 100%)

- **Subdomain:** one or more of {factory-planning · SC-network-design · logistics-distribution-network-design · technology-selection · site-selection · GPN-design}. If not stated explicitly, map by task description using Appendix A.
- **Planning task type:** controlled vocabulary (§5).
- **Time horizon explicitly stated:** Y / N.
- **Planning horizon tiers addressed** (pick all applicable): `Strategic` / `Tactical` / `Operational`; `NA` if the paper addresses no planning horizon (`NA` cannot be combined with other values). Record every tier the paper addresses separately instead of collapsing multi-tier papers into one class.
- **Planning horizon rationale:** free text; quote the paper's horizon statement(s) per tier.
- **System-configuring decision explicitly stated:** Y / N (does the paper frame the decision as determining *what exists*, not *how existing resources are used*?).
- **Theoretical framework cited:** VDI-5200 / SC-Planning-Matrix / Lanza-et-al-2019 / Wiendahl-Nyhuis / Melo-Nickel-Saldanha-da-Gama-2009 / other / none. `none` cannot be combined with other values.
  - If `none` → **theoretical framework rationale** (required): brief reasoning why no framework applies (e.g., no planning-theory framework is referenced in the text).
  - If `other` → **other theoretical framework specification** (required): name and cite the specific framework(s) utilized, as free text (not restricted to a controlled vocabulary).
  - Both fields stay empty (`NA`) when their value is not selected.

### 3.4 LLM/AI intervention (LLM pre-fill; R1 verifies 100%)

- **Model(s):** exact name + version (e.g., "GPT-4o", "Llama 3.1 70B") of only the LLMs deployed and evaluated with the paper's own method.
- **Models rationale:** free text; list other LLMs discussed in the paper but not deployed and evaluated with the method (e.g., in related work or as external baselines) and their role.
- Model family and open-weight refer only to the models listed under Model(s).
- **Model family:** GPT / Claude / Gemini / Llama / Mistral / Qwen / DeepSeek / other (specify).
- **Open-weight:** Y (Llama, Mistral, Qwen, DeepSeek …) / N (GPT, Claude, Gemini …) / mixed.
- **Fine-tuning:** none / prompt-engineering-only / LoRA / full-fine-tuning / other (specify).
- **Architectural pattern:** RAG / multi-agent / LLM+solver / LLM+digital-twin / other (specify).
- **Agentic architecture:** single-agent / multi-agent / supervisor-agent / pipeline / none.
- **Integrations:** list all applicable: RAG · KG · solver · digital-twin · simulation-platform · none.

### 3.5 OR/optimization substrate (LLM pre-fill; R1 verifies 100%)

- **Optimization tradition present:** Y / N.
- **Formalization level:** mature-MILP / mid-maturity-RL-metaheuristic / low-formalization / none.
- **Solver type** (if applicable): exact name as reported (e.g., Gurobi, COPT, CPLEX).

### 3.6 Evaluation and outcomes (LLM pre-fill; R1 verifies 100%)

- **Validation method:** as reported (e.g., benchmark comparison, user study, ablation).
- **Dataset or benchmark used:** name + size as reported; `NR` if absent.
- **Comparator:** human-planner / conventional-method / prior-AI-ML / none.
- **Reported metrics:** extract all quantitative values with units, context, and page reference. Use `NR` (never blank) if absent.
- **Study design:** developer-reported / single-case / benchmark / user-study / quasi-experimental.
- **Sample size:** number of test cases, users, or records as reported.
- **Reported limitations:** 1–3 sentence paraphrase of author-stated limitations.

### 3.7 Retrieval traceability (LLM pre-fill; R1 verifies 100%)

- **Source:** Scopus / WoS / OpenAlex / snowballing.
- **Anchor paper(s):** if retrieved via snowballing, list the anchor(s).

### 3.8 Gap indicators (LLM; interpretive; R1 + R2 verify 100%)

- **HITL pattern present:** Y / N. If Y → type: approval-gate / what-if-interface / escalation-protocol / other (specify).
- **Domain knowledge formalization present:** Y / N. If Y → type: ontology / knowledge-graph / standards-encoding / other (specify).
- **Evaluation framework used:** Y / N. If Y → type: benchmark / rubric / domain-specific-metric / other (specify).

### 3.9 Quality appraisal (LLM; interpretive; R1 + R2 verify 100%)

Lightweight checklist informed by MMAT (Hong et al., 2018) and Hevner et al. (2004). Two steps: classify, then appraise.

**Step 1 — Study-type category** (one value):

| Category | Definition |
|----------|------------|
| `A` Empirical | Primary data collection with a defined evaluation protocol (case study with quantitative metrics, controlled benchmark, user study) |
| `B` Prototype / design science | Implemented system demonstrated on illustrative cases without controlled evaluation |
| `C` Conceptual / framework | Architecture, taxonomy, or framework without implementation or empirical evaluation |

The category is **derived** from validation status (§3.2), not coded independently:

| Validation status | Category |
|-------------------|----------|
| `implemented-validated` | `A` |
| `prototype` | `B` |
| `framework-only` | `C` |
| `conceptual` | `C` |

Decision rules (apply when setting validation status): prototype + controlled evaluation → `implemented-validated` → `A`; prototype demonstrated on a single walkthrough without defined metrics → `prototype` → `B`. The category rationale is the `validation_status_rationale`. To change the category, change the validation status.

**Step 2 — Appraisal items**, each scored `Yes` / `Partially` / `No`, each with its own `_reasoning`:

| Item | Question |
|------|----------|
| **Q1** Methodological transparency | Is the method (study design, system architecture, or framework logic) described in enough detail for independent replication? |
| **Q2** Empirical or demonstration grounding | `A`: are metrics defined and results reported with context (sample size, variance, comparator)? `B`: is the artifact demonstrated on a case that exercises its core claims? `C`: is the argumentation internally consistent and traceable? |
| **Q3** Validity and limitation discussion | Are the boundaries of the contribution explicitly discussed (failure modes, scalability, external validity, domain assumptions)? |
| **Q4** Positioning against prior work | Is the contribution compared against existing solutions with explicit differentiation? |

Q2 is read conditionally on the category; Q1, Q3, Q4 apply uniformly. No composite score is computed.

**Low-quality flag:** `Y` if a source scores `No` on ≥ 2 items. The flag drives the pre-registered sensitivity analysis. Quality scores are never used for exclusion.

**Venue tier** is not an appraisal item; it is recorded in the bibliographic tier (§3.1: Q1–Q2 journal / Q3–Q4 journal or peer-reviewed conference / Tier 1 preprint).

---

## 4. Data Format

- **Primary table:** tidy data — one row per study, one column per field.
- **Multi-valued fields** (e.g., multiple LLM models per study): separate long-format table linked by study ID.
- **Not reported vs. not applicable:** use `NR` for missing data, `NA` for structurally inapplicable fields. Never leave cells blank.
- **Reasoning columns:** every extracted field `<field>` has a `<field>_reasoning` column (replaces the former `notes` column): justification + evidence locator (page/section; for interpretive fields also a short verbatim anchor). Filled by the LLM; verifiers append their own reasoning when correcting or flagging. Fields already named `*_rationale` in the schema serve this role.
- **Output format:** structured JSON conforming to the schema at <https://github.com/RaikoPipe/slr-data-model>. Raw LLM output validated against the schema before human review; schema-invalid outputs flagged and re-extracted.

---

## 5. Controlled Vocabularies

Full vocabularies: <https://github.com/RaikoPipe/slr-data-model>

**Planning tasks (pick all applicable):**
requirements-elicitation · Lastenheft-generation · factory-layout-planning · capacity-dimensioning · material-flow-design · simulation-modeling · SC-network-configuration · facility-location · make-or-buy · technology-scouting · investment-appraisal · site-selection · GPN-configuration · distribution-network-planning · logistics-network-planning · norm-compliance · tender-evaluation · other (specify)

**Architectural patterns:**
RAG · multi-agent · LLM+solver · LLM+digital-twin · single-agent-pipeline · other (specify)

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

- Full-text PDF converted to markdown via **pymupdf**.
- **Bibliographic fields:** not passed to the LLM (§3.1).
- **Descriptive and interpretive fields:** the full text is passed as a single document context; the LLM returns value + `_reasoning` per field.

### Output validation

- LLM output is structured JSON conforming to the schema.
- Schema-invalid outputs are flagged and re-extracted before human review.

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
| `H` | Human extracted |
| `L-V` | LLM extracted, human verified |
| `L-C` | LLM extracted, human corrected |
| `D` | Dual-reviewer extraction |

Record the verifier(s) in `verified_by` (e.g., `R1;R2`).

---

## 9. Pilot Extraction (Stage 1)

- **Sample:** 5 representative sources.
- **Procedure:** R1 and R2 independently extract all descriptive and interpretive fields manually, blind to LLM output. LLM pipeline runs in parallel on the same fields. Bibliographic fields are imported and not piloted.
- **Agreement:** assessed between R1–R2 and between human–LLM per field type.
- **Thresholds:** Gwet's AC1 ≥ 0.8 (categorical fields), ≥ 80% agreement (continuous/text fields). Multi-valued categorical fields (e.g., planning horizon tiers) are assessed per value (present/absent). Report raw agreement alongside AC1. With 5 sources, AC1 is computed per field and, as the gating figure, pooled per tier (descriptive / interpretive); per-field values are reported but a single field fails the gate only if its pooled tier also fails or the field's raw agreement is < 80%.
- **LLM gate:** LLM vs. R1–R2 consensus agreement reported per field, separately for descriptive and interpretive tiers. An interpretive field below threshold after one prompt revision and re-pilot reverts to manual R1 extraction with 100% R2 verification.
- **Outcome:** pilot results frozen in pre-registration update before full extraction proceeds. Instruction revisions triggered if thresholds unmet.

---

## 10. Escalation

Escalate to R3 when:

- R1 and R2 disagree after one discussion round.
- Source contradicts itself on a key field.
- Subdomain classification or strategic-scope determination is genuinely ambiguous (document reasoning in notes).
- Self-authored paper: R1 excluded; R2 independently verifies all tiers; disagreements with the LLM value that R2 cannot resolve go to R3.

---

## 11. Session Rules

- **Max 2 hours** per session (fatigue → errors).
- Log start/end time per session.
- No extraction under time pressure; defer rather than guess.
