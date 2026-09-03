**Screening Instructions v9**

**Project:** SLR — LLM-Based Decision Support for the Strategic Planning Horizon in Manufacturing and Logistics
**Tooling:** Rayyan, blind mode **ON** during independent screening; OFF only during adjudication. Exclusion Codes stated here are also viewable in Rayyan.
**Reviewer roles:** R1 (primary researcher), R2 (fellow researcher), R3 (supervisor / adjudicator). All references to "dual human review" mean R1 + R2; "escalation" means R3.

---

## 1. PICOC

| Element | Definition | Include example | Exclude example |
|---|---|---|---|
| **P**opulation | LLM-based decision-support systems applied to manufacturing and logistics planning at the strategic or upper-tactical horizon (decisions that configure or reconfigure the physical production system) | LLM-assisted greenfield factory concept design | Shopfloor scheduling system |
| **I**ntervention | LLM, foundation model, generative AI, agentic AI, RAG, or LLM-hybrid (solver, KG, digital twin) **where the LLM generates, structures, mediates or substantively supports the planning decision itself** | Multi-agent LLM for SC network configuration | Classical MILP solver without LLM component |
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
| Self-authored paper (overlapping authorship) | R1 excluded from screening; R2 screens independently (see §6) |

---

## 4. Workflow per stage

### Stages 1–3 (title/abstract)

1. Open assigned Rayyan queue; confirm **blind mode ON**.
2. For each record decide: **Include / Exclude / Maybe**.
3. On Exclude → apply tag `EXCL-{1–12}`.
4. On Maybe → tag `ESCALATE` + one-line note.
5. If a record has no abstract, attempt retrieval from the source database, publisher landing page, Google Scholar, and Semantic Scholar before deciding. If still unobtainable → Exclude (code 12), unless the optional title-based carve-out applies (see §2/§3).
6. Do not view the other reviewer's decisions or hidden bibliographic fields.

**Stage 3 specifics (LLM-assisted screening):**
- The LLM pipeline emits **Include / Maybe / Exclude**.
- R1 verifies **100%** of LLM `Include` and `Maybe` decisions.
- R1 spot-checks a **random 25%** of LLM `Exclude` decisions for false negatives.
- Ambiguous cases escalated to R1 + R2 dual review.

### Stage 4 (full-text)

1. Retrieve full text for all records passing Stage 3.
2. R1 and R2 screen independently in Rayyan with **blind mode ON**.
3. Check retraction status via Retraction Watch before finalizing decisions.
4. If full text unobtainable after one author contact attempt → exclude (code 12), log contact attempts.

**Tagging conventions:** `INCL`, `EXCL-{1–12}`, `ESCALATE`, `FT-UNAVAIL`, `PREPRINT-OF:{DOI}`.

---

## 5. Blinding and escalation

- **Blinding ON** for all independent screening (title/abstract and full-text).
- **Blinding OFF** only during scheduled adjudication; disabling logged with timestamp and record IDs.
- **Escalation path:** `ESCALATE` tag → R1 + R2 dual review → if unresolved, R3 decides; rationale recorded in adjudication log.

---

## 6. Overlapping-authorship protocol

Any study where R1 is a co-author is handled as follows:

- R1 is excluded from screening, extraction, quality appraisal, and synthesis decisions for that study.
- R2 screens and extracts independently.
- Disagreements escalated to R3.
- Affected studies flagged with a provenance marker in the extraction table.

---

## 7. Pilot LLM validation (Stage 2)

- **Sample:** Stratified n = 100 title/abstract records, artificially balanced to ≈ 50/50 include/exclude (oversampling borderline and included records to avoid the κ paradox under low natural prevalence). Stratified across databases to reflect the pre-deduplication pool distribution.
- **Procedure:** R1 and LLM pipeline screen independently.

**Label mapping (Amendment 1 specification):**
- R1 applies a **binary** reference: Include / Exclude.
- The LLM pipeline emits **Include / Maybe / Exclude**.
- For all metrics, LLM **{Include, Maybe} → positive**, mirroring the Stage 3 operational rule that both `Include` and `Maybe` (uncertain) decisions receive R1 verification. **Maybes are not dropped.**
- Because R1 is binary, **Gwet's AC1 and Cohen's κ are computed on binarised labels**.
- **Sensitivity and specificity are directional against R1** (R1 = ground truth).
- A **missing R1 label raises an error** and halts metric computation; it is **never** defaulted to a positive (or any) class.

- **Metrics:** Sensitivity, specificity, Gwet's AC1 (primary, prevalence-robust). Cohen's κ reported alongside for comparability. Full confusion matrix (TP, FP, TN, FN) reported.
- **Thresholds (frozen, unchanged):** Sensitivity ≥ 0.95, specificity ≥ 0.70, AC1 ≥ 0.80.
- **Missing-abstract records in the pilot:** One record in the pilot sample had no obtainable abstract; the LLM had independently excluded it under Code 3 (off-task scope). Because it is a true exclusion under either Code 3 or the broadened Code 12, the binary include/exclude label is unchanged and the validation metrics are unaffected. The case is recorded for transparency; the missing-abstract rule is material for the main screening stage.
- **On failure:** Refine LLM prompt; re-run on a **fresh** 100 records (never reuse). Freeze final prompt + metrics in OSF pre-registration update before Stage 3.
- **Computation:**
  - Cohen's κ — `sklearn.metrics.cohen_kappa_score`; κ = (p₀ − pₑ) / (1 − pₑ).
  - Gwet's AC1 — computed on the same binarised label vectors; AC1 = (pₐ − pₑ_γ) / (1 − pₑ_γ), where pₑ_γ uses Gwet's chance-agreement term (marginal-mean-based), not the κ chance term.

---

## 8. Screening reconciliation

| Stage | Rule |
|-------|------|
| Stage 2 (pilot) | R1 re-examines LLM decisions. If ≥ 3 errors of the same type → refine prompt, re-run pilot on fresh records. R1 decisions are authoritative. |
| Stage 3 (title/abstract) | R1–LLM disagreements resolved in favor of R1. Ambiguous cases → R1 + R2 dual review. |
| Stage 4 (full-text) | R1–R2 disagreements resolved by discussion. Unresolved → R3 majority decision; rationale logged. |

---

## 9. Logging format

```
record_id | stage | reviewer | decision | excl_code | note | timestamp
```

Stored as `screening_log.csv` in the OSF component (append-only). Workload per reviewer session capped at **2 hours** to reduce fatigue-driven errors. LLM screening runs batched and timestamped; prompts, model versions, and API call dates logged per run.

