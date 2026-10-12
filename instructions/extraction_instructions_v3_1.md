# Extractor Instructions — LLM-Based Decision Support for the Strategic Planning Horizon in Manufacturing and Logistics

**Version:** 3.1 (changes from 3.0: §3.3 planning horizon tiers, theoretical framework rationale; §6 boundary cases; §9 tier agreement; §3.4 models restricted to deployed and evaluated LLMs)
**Project:** OSF [link]
**Scope:** SLR on LLM-based decision support at the strategic and upper-tactical manufacturing and logistics planning horizon.
**Subdomains:** Factory planning (VDI 5200), SC network design, strategic logistics/distribution network design, technology selection & investment appraisal, GPN design.
**Reviewer roles:** R1 (primary researcher), R2 (fellow researcher), R3 (supervisor / adjudicator).

---

## 1. Extraction Tiers

| Tier | Fields | Method | Verification |
|------|--------|--------|--------------|
| **Bibliographic metadata** | DOI, title, authors, affiliations, country, year, venue, venue type, language, funding source | LLM-extracted | R1 spot-checks 10% |
| **Descriptive fields** | Study characterization, strategic planning scope, LLM/AI intervention, OR substrate, evaluation & outcomes, retrieval traceability | LLM pre-fill | R1 verifies 100% against source text |
| **Interpretive fields** | Gap indicators, quality appraisal, VDI 5200 phase mapping, validation-status judgments | extracted by R1 with 100% dual-verification by R2

---

## 2. Workflow

1. Open source PDF and extraction table (`extraction_table.csv`).
2. **Bibliographic tier:** scan LLM output, spot-check flagged fields.
3. **Descriptive tier:** verify each LLM-prefilled value against source text; correct or confirm using the provenance protocol (§8).
4. **Interpretive tier:** extract manually following the field rules below.
5. Log page/section reference for every numeric metric.
6. Flag uncertainties in the `notes` column; escalate ambiguous cases per §10.
7. Save after each source; commit to OSF daily.

---

## 3. Field-by-Field Rules

Full field definitions and JSON schema: <https://github.com/RaikoPipe/slr-data-model>

### 3.1 Bibliographic metadata (LLM-prefilled; R1 spot-check 10%)

- **DOI, title, authors, affiliations, country of corresponding author, year, venue, language:** verify against source header/footer.
- **Venue type:** Scimago Q1–Q4 journal (lookup current year) · conference proceedings · Tier 1 preprint (institutional affiliation confirmed) · grey literature.
- **Funding source:** as reported; `NR` if absent.
- **Self-authored flag:** `Y` if any review author appears in author list.

### 3.2 Study characterization (LLM pre-fill; R1 verifies 100%)

- **Research type:** empirical / conceptual / design-science.
- **Validation status:**

| Value | Definition |
|-------|------------|
| `implemented-validated` | Working system + quantitative evaluation |
| `prototype` | Working system, limited or no evaluation |
| `framework-only` | Architecture described, no implementation |
| `conceptual` | Position or vision paper |

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

### 3.8 Gap indicators (R1 manual; interpretive)

- **HITL pattern present:** Y / N. If Y → type: approval-gate / what-if-interface / escalation-protocol / other (specify).
- **Domain knowledge formalization present:** Y / N. If Y → type: ontology / knowledge-graph / standards-encoding / other (specify).
- **Evaluation framework used:** Y / N. If Y → type: benchmark / rubric / domain-specific-metric / other (specify).

### 3.9 Quality appraisal (R1 manual; interpretive)

Three-dimension rubric, each scored 1–3. Score each dimension independently before summing.

| Dimension | 1 | 2 | 3 |
|-----------|---|---|---|
| **Methodological transparency** | Method description insufficient to replicate | Key steps described but gaps remain | Fully replicable |
| **Empirical grounding** | Conceptual or framework-only | Prototype or limited evaluation | Implemented + quantitative evaluation |
| **Venue tier** | Preprint | Q3–Q4 journal or conference | Q1–Q2 journal |

**Composite range: 3–9.** Sources scoring **≤ 4** are dual-verified by R2.

---

## 4. Data Format

- **Primary table:** tidy data — one row per study, one column per field.
- **Multi-valued fields** (e.g., multiple LLM models per study): separate long-format table linked by study ID.
- **Not reported vs. not applicable:** use `NR` for missing data, `NA` for structurally inapplicable fields. Never leave cells blank.
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
- **Contradictions within source:** extract both values, flag in `notes`, escalate.
- **Uncertainty about field assignment:** mark field with `?` suffix, add note, adjudicate.
- **Subdomain boundary cases:** if a paper spans tactical and strategic tasks, include only if a strategic task is explicitly addressed (i.e., `Strategic` is among the planning horizon tiers addressed); record all tiers addressed and document the reasoning in the horizon rationale.
- **Outlier metrics** (> 2× the range of other sources for the same metric type): flag, verify, report with context — do not exclude.

---

## 7. LLM Extraction Pipeline

### Input preparation

- Full-text PDF converted to markdown via **pymupdf**.
- **Bibliographic fields:** only the title page and references section are passed.
- **All other fields:** the full text is passed as a single document context.

### Output validation

- LLM output is structured JSON conforming to the schema.
- Schema-invalid outputs are flagged and re-extracted before human review.

### Verification protocol

For each LLM-prefilled field:

1. Locate the claim in the source PDF.
2. If verified → mark `verified=Y` in provenance column.
3. If incorrect → overwrite value, mark `verified=corrected`, log original in `llm_raw` column.
4. If unverifiable → mark `verified=unverifiable`, escalate.

Report count of LLM errors per field type at the end of each extraction session. If ≥ 3 same-type LLM errors are detected, refine the prompt, re-extract affected records, and update the pre-registration.

---

## 8. Provenance Tagging

Every extracted field receives a provenance tag:

| Tag | Meaning |
|-----|---------|
| `H` | Human extracted |
| `L-V` | LLM extracted, human verified |
| `L-C` | LLM extracted, human corrected |
| `D` | Dual-reviewer extraction |

---

## 9. Pilot Extraction (Stage 1)

- **Sample:** 5 representative sources.
- **Procedure:** R1 and R2 independently extract all fields manually. LLM pipeline runs in parallel.
- **Agreement:** assessed between R1–R2 and between human–LLM per field type.
- **Thresholds:** κ ≥ 0.7 (categorical fields), ≥ 80% agreement (continuous fields). Multi-valued categorical fields (e.g., planning horizon tiers) are assessed per value (present/absent).
- **Outcome:** pilot results frozen in pre-registration update before full extraction proceeds. Instruction revisions triggered if thresholds unmet.

---

## 10. Escalation

Escalate to R3 when:

- R1 and R2 disagree after one discussion round.
- Source contradicts itself on a key field.
- Subdomain classification or strategic-scope determination is genuinely ambiguous (document reasoning in notes).
- Self-authored paper: always routed to R2 for independent extraction; disagreements to R3.

---

## 11. Session Rules

- **Max 2 hours** per session (fatigue → errors).
- Log start/end time per session.
- No extraction under time pressure; defer rather than guess.

---

## Appendices

- **Appendix A:** Strategic subdomain mapping decision tree — `/extraction/appendix_A_subdomain_tree.pdf`
- **Appendix B:** Quality appraisal rubric (full scoring guide) — `/extraction/appendix_B_quality_rubric.pdf`
- **LLM prompts and version log:** `/extraction/llm_artifacts/`
