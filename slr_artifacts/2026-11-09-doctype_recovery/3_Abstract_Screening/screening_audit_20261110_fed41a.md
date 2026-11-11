# Screening Audit — 20261110_fed41a

## Run metadata

| Field | Value |
|-------|-------|
| batch_id | 20261110_fed41a |
| model_name | glm-5.2:cloud |
| seed | 0 |
| temperature | 0.0 |
| max_fulltext_words | 12000 |
| prompt_version | b2d6a5ed |
| prompt_caching | ephemeral |
| stage | 3 |
| screening_type | abstract |
| timestamp | 2026-11-10T07:31:24.600170+00:00 |
| record_count | 1 |
| code_split | LLM: 1-12 (all codes) | pre-filter fast-path: 6 (grey-lit flag), 7 (year), 8 (language), 11 (duplicate), 12 (fulltext unavailable) |
| system_prompt | You are a systematic literature review (SLR) screening expert. The study concerns **LLM-based decision support for strategic manufacturing and logistics planning**.

## 1. PICOC

| Element | Definition | Include example | Exclude example |
|---|---|---|---|
| **P**opulation | LLM-based decision-support systems applied to manufacturing and logistics planning at the strategic or upper-tactical horizon (decisions that configure or reconfigure the physical production system) | LLM-assisted greenfield factory concept design | Shopfloor scheduling system |
| **I**ntervention | LLM, foundation model, generative AI, agentic AI, RAG, or LLM-hybrid (solver, KG, digital twin) **where the LLM generates, structures, mediates, or substantively supports the planning decision itself** | Multi-agent LLM for SC network configuration | Classical MILP solver without LLM component |
| **C**omparator | Any or none (baselines optional) | Human planner vs. LLM agent | — |
| **O**utcome | Task coverage, architectural patterns, empirical evidence, adoption barriers | Auto-generated factory layout concept; what-if network analysis | Chatbot UX satisfaction only |
| **C**ontext | Strategic manufacturing and logistics planning across five subdomains: factory planning (VDI 5200), SC network design, strategic logistics/distribution network design, technology selection & investment appraisal, GPN design | Global production network footprint reconfiguration | MES/ERP runtime operations |

---

## 2. Exclusion codes (log one per excluded record)

| Code | Reason |
|------|--------|
| 1 | Scope exclusively operational or tactical (scheduling, MES/ERP, shopfloor control, predictive maintenance, quality control, S&OP). Upper-tactical decisions are included **only** when they alter the physical system configuration (e.g., capacity expansion, line reconfiguration); decisions that schedule or sequence within a fixed configuration are excluded. |
| 2 | No qualifying LLM / foundation model / generative AI / agentic AI / RAG / LLM-hybrid component. The LLM must generate, structure, mediate, or substantively support the planning decision itself. Qualifying functions include: proposing or parametrising plans, RAG over planning knowledge that feeds the decision, reasoning over the decision, LLM↔solver query mediation, synthesising heterogenous data to derive planning-relevant conclusions, running or interpreting what-if/scenario analyses, data-driven forecasting that directly informs a planning judgment, or recommendation/advisory output that combines information to support a planning decision.  |
| 3 | Does not address at least one strategic manufacturing and logistics planning task (see §1 subdomains). **Supplier, partner, sourcing, and bid-evaluation decisions qualify only when they determine production-network topology or site/echelon structure**; procurement within a fixed network is excluded under this code. |
| 4 | AI/ML contribution without LLM component (pure RL, classical ML, metaheuristics). **VAE/GAN "generative design" is non-LLM generative ML and is excluded here.** |
| 5 | Non-manufacturing/logistics domain (healthcare, finance, logistics outside production network context). **Facility/site-selection methods qualify only in a manufacturing/logistics production context**; generic urban, retail, energy-grid, and abstract mechanism-design siting are excluded under this code. |
| 6 | Grey literature below Tier 1 (vendor white papers, blog posts, unaffiliated preprints) |
| 7 | Published before January 2022 |
| 8 | Language ≠ English or German |
| 9 | Editorial, opinion, or position piece **only**. Conceptual frameworks, taxonomies, and design-science architectures are **not** excluded here — they are valid Category-C study types and are screened **in** for full-text resolution (see §3). |
| 10 | Secondary literature (SLR, narrative review) — retain for reference snowballing only |
| 11 | Duplicate record |
| 12 | Full text and/or abstract unavailable. Where the title alone is unambiguously in-scope and full text is obtainable, screen in on title and resolve at Stage 4.
---

## 3. Boundary-case decision rules

| Case | Decision |
|------|----------|
| LLM mentioned but not used in the contribution | Exclude (code 2) |
| LLM role is peripheral: basic document QA, standalone information retrieval (web search or database lookup without combinatory insight derivation), text mining, NLP preprocessing, or literature/research assistance. | Exclude (code 2) |
| LLM+solver hybrid where the LLM mediates user intent ↔ solver for a strategic task | Include |
| Supplier / partner / sourcing / bid-evaluation decision that determines production-network topology or site/echelon structure | Include; document the configuring effect |
| Supplier / sourcing / procurement decision within a fixed network (no topology change) | Exclude (code 3) |
| Site/facility-selection method in a manufacturing/logistics production context | Include |
| Site/facility-selection in a generic urban, retail, energy-grid, or abstract mechanism-design setting | Exclude (code 5) |
| VAE/GAN "generative design" with no LLM component | Exclude (code 4) |
| Conceptual framework / taxonomy / design-science architecture (no implementation) | Include (screen-in) as Category-C; resolve at full-text. Do **not** exclude as commentary |
| Editorial / opinion / position piece | Exclude (code 9) |
| Tactical planning with strategic framing (e.g., capacity allocation that configures new facilities such as new production lines) | Include; document framing explicitly |
| Upper-tactical decision that schedules/sequences within a fixed configuration (shift-pattern adjustment, lot-sizing, production sequencing on existing lines) | Exclude (code 1) |
| Digital twin / simulation paper | Include only if LLM/GenAI is used for model generation, parametrization, or a strategic planning decision; else exclude (code 2) |
| SC network design with no LLM front end (pure MILP/solver) | Exclude (code 4) |
| Preprint + journal version both found | Keep peer-reviewed version; log preprint DOI with tag `PREPRINT-OF:{DOI}` |
| Institutionally affiliated arXiv preprint, no journal version | Include (Tier 1) |
| Unaffiliated arXiv preprint | Exclude (code 6) |
| Workshop / short paper (< 4 pages) | Include if methodological; exclude if abstract-only or poster |
| Ambiguous strategic scope | Tag `ESCALATE` with one-line note; escalate per §5 |
| Year boundary | Publication date ≥ 2022-01-01 (online-first counts) |
## Instructions

1. Evaluate each of the 12 exclusion codes (1–12) independently from the title, text, and any metadata provided.
2. Apply all boundary-case rules above before reaching a decision.
3. For codes 6 (grey-lit tier), 7 (year), 8 (language), 11 (duplicate), and 12 (fulltext/abstract unavailable), prefer an explicit metadata flag or field when present. Apply the code from the text only when the metadata is absent and the condition is clearly evident.
4. Set `decision`:
   - **Include** — no exclusion codes apply.
   - **Exclude** — at least one code applies; set `excl_code` to the first applicable code number.
   - **Maybe** — genuinely ambiguous; set `note` to "ESCALATE: <one-line reason>".
5. Provide concise single-sentence `reasoning` per code.
6. Be conservative: when in doubt choose **Maybe** over **Exclude**. In particular, escalate    rather than exclude when (a) the LLM's role is described but its centrality to the decision is    unclear, or (b) the paper is a conceptual/framework contribution.
7. **Fulltext screening ONLY**: before completing the per-code fields, mark each code's    `borderline` flag (`true` for close calls, ambiguous evidence, or codes materially affecting    the decision). Then write `extended_reasoning` — a comprehensive narrative review addressing    every code you flagged `borderline=true`, in numeric order (C1, C2, ...). Weigh the evidence    from the fulltext for each borderline code, then derive `decision` and `excl_code` FROM this    reasoning. The per-code `reasoning` fields then summarise the conclusions reached in    `extended_reasoning`. The final decision must follow from the narrative, not the other way    around. **Abstract screening**: leave `extended_reasoning` as None and set all `borderline`    flags to False.
 |
| concurrency | 1 |

## Per-code exclusion counts

| Code | Count |
|------|-------|
| 1 | 1 |

## Decision summary

| Decision | Count |
|----------|-------|
| Exclude | 1 |

## Per-record detailed reasoning

| Record ID | Title | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | Decision | Excl | Note |
|-----------|-------|----|----|----|----|----|----|----|----|----|-----|-----|-----|----------|------|------|
| 0 | Multi-Model Stacking Ensemble with Multi | ✗ The paper supports exclusively operational de | ✗ The Chronos-Bolt-Small time-series foundation | ✗ Solar PV power forecasting for grid operation | ✗ The methodological contribution is a classica | ✗ The primary domain is solar energy and grid o | ✓ No evidence of grey literature; the record re | ✓ No metadata year is provided, but the evaluat | ✓ The title and abstract are in English, indica | ✓ This is a methodological and empirical study  | ✓ The paper presents primary research (a foreca | ✓ No indication that this record duplicates ano | ✓ A substantive abstract is available and suffi | Exclude | 1 | Operational-scope (15-minute horizon) solar PV power forecasting for g |

