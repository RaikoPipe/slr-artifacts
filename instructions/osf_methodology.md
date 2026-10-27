## Landing Page

#### Intended use

This Generalized Systematic Review Registration Form is intended as a general-purpose registration form. The form is designed to be applicable to reviews across disciplines (i.e., psychology, economics, law, physics, or any other field) and across review types (i.e., scoping review, review of qualitative studies, meta-analysis, or any other type of review). That means that the reviewed records may include research reports as well as archive documents, case law, books, poems, etc. This form, therefore, is a fall-back for more specialized forms and can be used if no specialized form or registration platform is available.

#### Citation

Van den Akker, O. R., Peters, G. Y., Bakker, C., Carlsson, R., Coles, N. A., Corker, K. S., Feldman, G., , Moreau, D., Nordström, T., Pickering, J. S., Riegelman, A., Topor, M., Veggel, N., Yeung, S., Mellor, D., & Pfeiffer, N. Generalized Systematic Review Registration Form. MetaArXiv.. https://doi.org/g5fj.

## Review Methods

In this section, you register the general type, background and goals of your review.

#### Type of review

Systematic literature review following PRISMA 2020 (Page et al., 2021) and PRISMA-S (Rethlefsen et al., 2021) reporting guidelines. Protocol development informed by Kitchenham & Charters (2007) and Tingelhoff, Brugger & Leimeister (2025) for structured SLRs in engineering and management research. AI-use reporting follows PRISMA-trAIce (2024). Reviewer Team: R1 (primary researcher): Search execution, deduplication, LLM pipeline development, Stage 3 human verification, Stage 4 full-text screening (reviewer 1), all extraction (single reviewer unless dual required), quality appraisal, synthesis R2 (fellow researcher): Stage 4 full-text screening (reviewer 2), dual extraction and quality appraisal of self-authored studies (overlapping-authorship cases), 100% independent second verification of LLM-extracted interpretive fields, review of synthesis tables R3 (supervisor): Adjudication of unresolved screening and extraction disagreements, external consistency review of narrative and inferential claims All downstream references refer to this role allocation.

#### Review stages

1. Preparation 2. Protocol Registration (OSF) 3. Search 4. Pilot LLM Screening Validation 5. Prereg Update 6. Screening 7. Pilot Extraction 8. Prereg Update 9. Extraction 10. Quality Appraisal 11. Synthesis 12. Reporting

#### Current review stage

Preparation complete

#### Start date

2026-04-20

#### End date Updated

2027-01-31

#### Background

Strategic manufacturing and logistics planning encompasses decisions that configure or reconfigure the physical production system at the strategic or upper-tactical horizon: facility location and layout, technology and equipment selection, supply chain network topology, and global production network design. Since the release of ChatGPT in late 2022, large language models (LLMs) and agentic AI systems have been increasingly proposed as decision-support tools in manufacturing and supply chain contexts, employing architectural patterns such as retrieval-augmented generation, multi-agent systems, LLM+solver hybrids, and LLM+digital-twin integration. The domain is anchored in the strategic row of the Supply Chain Planning Matrix (Fleischmann, Meyr; Wagner, 2002) and scoped through five frameworks: Factory planning (VDI 5200) Supply chain network design (Fleischmann, Meyr; Wagner, 2002) Strategic logistics and distribution network design (Melo, Nickel; Saldanha-da-Gama, 2009) Technology selection and investment appraisal (Hamzeh; Xu (2019) for methodological landscape, Shehabuddeen et al. (2006) for process-framework) Global production network design (Lanza et al., CIRP Annals 2019) Organizational configuration decisions (governance structures, workforce architecture) are acknowledged as strategic but excluded from this review to maintain coherence with the physical-system focus. Several systematic reviews have examined LLM applications in adjacent manufacturing and supply chain domains, but none target the strategic planning horizon specifically. In the SCM space, Song et al. (IJPR, 2026) mapped LLM competencies onto SCOR processes, Srivastava et al. (JGIM, 2024) identified application themes via big data analysis. In the manufacturing domain, Ouerghemmi and Ertz (Computers, 2025) classified LLM themes across digital manufacturing, Bajestani et. al (Journal of Manufacturing Systems, 2026) scoped LLM applications with a human-in-the-loop focus, Galdino et al. (Engineering Reports, 2025) derived deployment requirements for LLM-based cognitive assistants in quality management and Nguyen and Kittur (Frontiers in Education, 2025) reviewed LLMs across engineering disciplines broadly. None of these reviews addresses the intersection of LLMs with the strategic planning tier: where and how factories are built, how production networks are configured, which technologies are selected, and how supply chain topology is designed. This review aims to fill this gap.

#### Primary research question(s)

- RQ1: What strategic manufacturing and logistics planning tasks have been addressed by LLM-based decision-support systems, and what architectural patterns do these systems employ? - RQ2: What empirical evidence exists for the effectiveness of LLM-based decision-support systems at the strategic planning horizon in manufacturing and logistics, and how robust is that evidence? - RQ3: What gaps and barriers constrain the maturity and adoption of LLM-based decision support at the strategic manufacturing planning level?

#### Secondary research question(s)

- RQ1a: How does LLM maturity vary across strategic planning subdomains, and how does this variation relate to the maturity of the underlying optimization tradition (solver-specificity hypothesis)? - RQ2a: Which efficiency or effectiveness claims reported in the literature are based on robust empirical designs, and which rest on developer-reported or single-case evidence?

#### Expectations / hypotheses

- Corpus composition: Factory planning will dominate; SC network design second; technology selection and GPN design sparsely populated, with GPN as the clearest white space. - Solver-specificity maturity: LLM maturity will correlate with OR tradition maturity across subdomains: mature MILP substrates yielding LLM+solver hybrids; mid-maturity RL substrates yielding emerging hybrids; low-formalization subdomains yielding RAG/multi-agent patterns with weaker validation. - Evidence base: Thin and heterogeneous: developer-reported results on selected use cases, single-company deployments, curated benchmarks. No randomized or quasi-experimental designs expected. - Gap confirmation: All three hypothesized gaps (strategic HITL designs, domain knowledge formalization, evaluation frameworks) will be confirmed as structural absences. Evaluation framework gap expected most acute. - Framing bias: The review is conducted from within the German engineering-research tradition.

#### Dependent variable(s) / outcome(s) / main variables

Dependent / Main Variables: - Task coverage: strategic planning subdomains addressed by LLM-based systems - Architectural pattern: RAG, multi-agent, LLM+solver hybrid, LLM+digital twin - Empirical evidence type: metric reported, study design, external validity - Gap presence: whether each of the three hypothesized gaps is documented as absent - Subdomain OR maturity: formalization level of the optimization tradition (operationalization of the solver-specificity lens)

#### Independent variable(s) / intervention(s) / treatment(s)

Not applicable. This review is descriptive and taxonomic rather than effect-estimating. No association or intervention is tested.

#### Additional variable(s) / covariate(s)

Venue quality tier (Q1–Q4 journal, Procedia CIRP short paper, grey literature), publication year, country of corresponding author, funding source where disclosed, language of publication.

#### Software

- Zotero for literature item management - Rayyan for screening - Various Python implementations for API requesting handling, cleaning and deduplication - LangChain + LLM for information extraction; temperature 0.0; output schema: (https://github.com/RaikoPipe/slr-data-model); LangChain Pipeline with system prompt: (https://github.com/RaikoPipe/llm-screening-workflows). The exact model name, version, and access method will be logged as a preregistration amendment before each pipeline stage begins, following the pilot validation protocol registered in the screening instructions.; selection between the two candidates will be made prior to the pilot validation stage and frozen for the remainder of the review.

#### Funding

This review is conducted as part of a PhD project at Engineering of Products and Systems, Otto-von-Guericke-University Magdeburg, Germany, funded by the Federal Ministry of Research, Technology and Space (BMFTR) under the project GenAI4FFD (grant no. 01MK25003E).

#### Conflicts of interest

The authors declare no conflicts of interest. No author has financial or advisory relationships with vendors of LLM-based planning tools referenced in this review.

#### Overlapping authorships

One or more authors of this review have published prior work at the intersection of LLMs and factory planning that may meet the inclusion criteria. To mitigate bias, any such study will be handled as follows: R1 (the affected author) will be excluded from screening, data extraction, quality appraisal, and synthesis decisions pertaining to their own work. These tasks will be performed independently by R2. The affected studies will be flagged in the extraction table with a provenance marker, and any disagreements will be escalated to R3 for adjudication. A list of self-authored included studies will be disclosed in the final report.

## Search Strategy

In this section, you register your search strategy: the procedures you designed to obtain all (potentially) relevant sources to review (e.g., articles, books, preprints, reports, case law, policy papers, archived documents).

#### Databases

- Scopus - Web of Science Core Collection - OpenAlex

#### Interfaces

- Scopus: Elsevier Scopus API - Web of Science Core Collection: Clarivate Web of Science API - OpenAlex: OpenAlex API via pyalex

#### Grey literature

Restricted to Tier 1 only (per Adams et al., 2017 grey literature taxonomy): preprints with documented institutional affiliation, captured via OpenAlex (e.g. preprints from arXiv that OpenAlex ingests).

#### Inclusion and exclusion criteria

Framework: PICOC Population: LLM, foundation model, generative AI, agentic AI, RAG, or LLM-hybrid (solver, KG, digital twin) where the LLM generates, structures, mediates or substantively supports the planning decision itself Intervention: LLMs, foundation models, generative AI, agentic AI, RAG, or LLM+solver/Knowledge Graph/digital-twin hybrids Comparison: Not required (descriptive review) Outcomes: Task coverage, architectural pattern, empirical evidence, adoption barriers Context: Strategic and upper-tactical planning horizon in manufacturing and logistics (decisions that configure or reconfigure the physical production system) Published between January 2022 and the search execution date Peer-reviewed journal article, conference paper, book chapter, institutional report, or preprint with institutional anchor Written in English or German

#### Query strings

Scopus TITLE-ABS-KEY(large language model* OR LLM* OR "generative AI" OR "generative artificial intelligence" OR "retrieval-augmented generation" OR "LLM-based agent" OR "ChatGPT" OR GPT* OR "foundation model") AND TITLE-ABS-KEY("factory planning" OR "factory design" OR "factory layout" OR "facility layout" OR "layout planning" OR "manufacturing system design" OR "production system design" OR ("digital twin" AND ("factory planning" OR "production system design" OR "supply chain network" OR "facility layout" OR "layout planning")) OR "supply chain network design" OR "supply chain optimization" OR "supply chain planning" OR "partner selection" OR "supplier selection" OR "facility location" OR "global production network" OR "multi-site" OR "warehouse location" OR "warehouse planning" OR "distribution network design" OR "distribution network planning" OR "logistics network design" OR "logistics network planning" OR "hub location" OR "depot location" OR "technology selection" OR "technology scouting" OR "equipment selection" OR "investment appraisal" OR "capital investment" OR "make-or-buy" OR "site selection" OR "location planning" OR "capacity planning" OR "line balancing" OR "greenfield" OR "brownfield" OR "Fabrikplanung") AND PUBYEAR > 2021 AND PUBYEAR < 2027 Web of Science TS=(large language model* OR LLM* OR "generative AI" OR "generative artificial intelligence" OR "retrieval-augmented generation" OR "LLM-based agent" OR "ChatGPT" OR GPT* OR "foundation model") AND TS=("factory planning" OR "factory design" OR "factory layout" OR "facility layout" OR "layout planning" OR "manufacturing system design" OR "production system design" OR ("digital twin" AND ("factory planning" OR "production system design" OR "supply chain network" OR "facility layout" OR "layout planning")) OR "supply chain network design" OR "supply chain optimization" OR "supply chain planning" OR "partner selection" OR "supplier selection" OR "facility location" OR "global production network" OR "multi-site" OR "warehouse location" OR "warehouse planning" OR "distribution network design" OR "distribution network planning" OR "logistics network design" OR "logistics network planning" OR "hub location" OR "depot location" OR "technology selection" OR "technology scouting" OR "equipment selection" OR "investment appraisal" OR "capital investment" OR "make-or-buy" OR "site selection" OR "location planning" OR "capacity planning" OR "line balancing" OR "greenfield" OR "brownfield" OR "Fabrikplanung") AND PY=(2022-2027) OpenAlex ("large language model" OR "LLM" OR "generative AI" OR "generative artificial intelligence" OR "retrieval-augmented generation" OR "LLM-based agent" OR "ChatGPT" OR "GPT" OR "foundation model") AND ("factory planning" OR "factory design" OR "factory layout" OR "facility layout" OR "layout planning" OR "manufacturing system design" OR "production system design" OR ("digital twin" AND ("factory planning" OR "production system design" OR "supply chain network" OR "facility layout" OR "layout planning")) OR "supply chain network design" OR "supply chain optimization" OR "supply chain planning" OR "partner selection" OR "supplier selection" OR "facility location" OR "global production network" OR "multi-site" OR "warehouse location" OR "warehouse planning" OR "distribution network design" OR "distribution network planning" OR "logistics network design" OR "logistics network planning" OR "hub location" OR "depot location" OR "technology selection" OR "technology scouting" OR "equipment selection" OR "investment appraisal" OR "capital investment" OR "make-or-buy" OR "site selection" OR "location planning" OR "capacity planning" OR "line balancing" OR "greenfield" OR "brownfield" OR "Fabrikplanung") Note: "Digital twin" is nested with strategic-scope terms because the standalone phrase retrieves a large volume of operational-level literature (shopfloor monitoring, predictive maintenance, real-time control) that falls outside the review's planning horizon.

#### Search validation procedure

The search must retrieve each anchor: 1. Factory planning: Ferry, Huang Reinhart, "Anwendung von Large Language Models (LLMs) in der Fabrikplanung" (ZWF 120(3), 2025) 2. SC network design (LLM+solver): Li, Mellou, Zhang, Pathuri & Menache, "OptiGuide: Large Language Models for Supply Chain Optimization" (arXiv:2307.03875, Microsoft Research, 2023) 3. SC partner selection (LLM+multi-agent): Gao et al., "SCSimulator: An Exploratory Visual Analytics Framework for Partner Selection in Supply Chains through LLM-driven Multi-Agent Simulation" (IUI 2026, arXiv:2601.14566) 4. Technology selection: Werheid et al., "Designing an LLM-Based Copilot for Manufacturing Equipment Selection" (arXiv:2412.13774, RWTH/FLAIR, 2024)

#### Other search strategies

Single pass of: - Backward (ascendancy) snowballing: references of all included studies are screened against inclusion criteria. - Forward (descendancy) snowballing: forward citations of all included studies are retrieved via OpenAlex and screened against inclusion criteria.

#### Procedures to contact authors

Authors will be contacted only when critical extraction fields (architecture details, validation metrics, dataset size) are missing from the published paper and cannot be inferred. Initial contact via institutional email with a standardized request. One follow-up after 14 days if no response. Non-response after follow-up results in the study being retained with missing fields marked as "not reported." No personal data or communication content is shared. Records for which full text is unobtainable through institutional subscription, open access, or preprint repositories (arXiv, SSRN, ResearchGate author pages) are excluded.

#### Results of contacting authors

Reported in the final manuscript as aggregate counts: number of authors contacted, number of responses received, number of studies enriched with author-provided data. Non-responses are noted without identifying individuals.

#### Search expiration and repetition Updated

One repeat search will run after Stage 4 screening is complete, covering 2026-06-09 to 2026-10-06, using identical databases, query strings, and eligibility criteria. Round 2 records are deduplicated against the full Round 1 pool (including excluded records), pass through the same Stage 3 and 4 screening with the same frozen LLM model and prompt, and are merged into the main corpus with a search-round tag in the extraction table.

#### Search strategy justification

The Scopus/WoS dual anchor follows standard practice in engineering SLRs and provides reproducible peer-reviewed coverage. OpenAlex is added to close coverage gaps for preprints and recent open-access contributions. Grey literature is restricted to institutionally affiliated preprints (Tier 1). The 2022 start date reflects the ChatGPT release as the LLM adoption inflection point. Seed-paper snowballing compensates for indexing lag in the most recent publications.

#### Miscellaneous search strategy details

All search execution dates, full query strings, hit counts per database, and raw export files (RIS/BibTeX/CSV) are archived on OSF as supplementary materials for reproducibility.

## Screening

In this section, you register your screening procedure: the procedure you designed to eliminate all irrelevant sources from the results of the search strategy (and retain the relevant sources).

#### Screening stages

Stage 1: Deduplication (automated + human review) Python pandas pipeline: (1) exact DOI match, (2) DOI-less records matched by normalized title + first author + year, (3) fuzzy title deduplication via RapidFuzz to catch preprint/journal pairs, preprint-vs-published versions, and formatting variants. All flagged pairs manually reviewed; when duplicates differ in version (preprint vs. peer-reviewed), the peer-reviewed version is retained and the preprint DOI logged for traceability. Stage 2: Pilot LLM screening validation (100 records, human vs. LLM) A random sample of 100 title/abstract records is screened independently by R1 and LLM pipeline. Gwet's AC1 is used as the primary agreement metric (prevalence-robust); Cohen's κ reported alongside for comparability. Sensitivity, specificity, and the full confusion matrix (TP, FP, TN, FN) are reported. Stage 3: Full title/abstract screening (LLM + R1 adjudication) All records screened by LLM pipeline; all LLM "include" and "uncertain" decisions verified by R1. LLM "exclude" decisions spot-checked on random 25% by R1 to catch false negatives. Ambiguous cases escalated to R1 + R2 dual review. Screening of self-authored papers done by R2. Stage 4: Full-text screening (R1 + R2) All records passing Stage 3 retrieved in full text and screened independently by R1 and R2. LLM not used at this stage. Records with unobtainable full text excluded with reason logged. Retraction status checked via Retraction Watch.

#### Screened fields / blinding

Stage 4 screening is conducted in Rayyan with blind mode enabled: bibliographic fields and reviewer decisions of the other reviewer are hidden during independent screening. Blinding is disabled only during adjudication discussions.

#### Used exclusion criteria

| Code | Reason | | 1 | Scope exclusively operational or tactical (scheduling, MES/ERP, shopfloor control, predictive maintenance, quality control, S&OP). Upper-tactical decisions are included only when they alter the physical system configuration (e.g., capacity expansion, line reconfiguration); decisions that schedule or sequence within a fixed configuration are excluded. | | 2 | No qualifying LLM / foundation model / generative AI / agentic AI / RAG / LLM-hybrid component. The LLM must generate, structure, mediate, or substantively support the planning decision itself. Qualifying functions include: proposing or parametrising plans, RAG over planning knowledge that feeds the decision, reasoning over the decision, LLM↔solver query mediation, synthesising heterogenous data to derive planning-relevant conclusions, running or interpreting what-if/scenario analyses, data-driven forecasting that directly informs a planning judgment, or recommendation/advisory output that combines information to support a planning decision. | | 3 | Does not address at least one strategic manufacturing and logistics planning task. Supplier, partner, sourcing, and bid-evaluation decisions qualify only when they determine production-network topology or site/echelon structure; procurement within a fixed network is excluded under this code. | | 4 | AI/ML contribution without LLM component (pure RL, classical ML, metaheuristics). VAE/GAN "generative design" is non-LLM generative ML and is excluded here. | | 5 | Non-manufacturing/logistics domain (healthcare, finance, logistics outside production network context). Facility/site-selection methods qualify only in a manufacturing/logistics production context; generic urban, retail, energy-grid, and abstract mechanism-design siting are excluded under this code. | | 6 | Grey literature below Tier 1 (vendor white papers, blog posts, unaffiliated preprints) | | 7 | Published before January 2022 | | 8 | Language ≠ English or German | | 9 | Editorial, opinion, or position piece only. Conceptual frameworks, taxonomies, and design-science architectures are not excluded here — they are valid Category-C study types and are screened in for full-text resolution. | | 10 | Secondary literature (SLR, narrative review) — retain for reference snowballing only | | 11 | Duplicate record | | 12 | Full text and/or abstract unavailable. Where the title alone is unambiguously in-scope and full text is obtainable, screen in on title and resolve at Stage 4.

#### Screener instructions

Screeners are provided with an instruction sheet stored on OSF as `screening_instructions_v9.md`.

No files selected

#### Screening reliability

Two-reviewer model with asymmetric allocation per stage: Stage 1 (deduplication): Automated pipeline + R1 for flagged pairs; no metric used (deterministic) Stage 2 (pilot LLM validation): R1 + LLM pipeline on 100 records. Agreement assessed via sensitivity, specificity, and Gwet's AC1. Thresholds: sensitivity ≥ 0.95, specificity ≥ 0.70, AC1 ≥ 0.8. Stage 3 (full title/abstract): LLM screens all; R1 verifies 100% includes/uncertain, 25% random excludes. Agreement logged per record but not formally tested. Stage 4 (Full-text screening): R1 + R2 independent screening. Agreement assessed via Gwet's AC1 on full-text decisions.

#### Screening reconciliation procedure

- Stage 2: R1 re-examines LLM decision. If ≥3 errors of the same type emerge, prompt is refined and pilot re-run. R1 decisions are not altered. - Stage 3: R1-LLM disagreements always resolved in favor of R1. Ambiguous cases escalated to R1 + R2 dual review. - Stage 4: R1-R2 disagreements resolved by discussion. Unresolved cases escalated to R3; majority decision recorded with rationale logged. All reconciliation decisions and rationales logged in Rayyan and exported with final corpus.

#### Sampling and sample size

All records passing Stage 4 are included; no sampling. Expected final corpus size: 25–40 records based on current scoping. No formal power analysis applicable. If the final corpus falls below 8 records, quantitative synthesis will be reported descriptively only, without inferential claims. For the Stage 2 validation sample of 100 records: Gwet's AC1 95% CI width of approximately ±0.08–0.12 at AC1 = 0.80, depending on marginal distributions. The sample is stratified across databases to reflect the full pre-deduplication pool distribution; prevalence stratification and robustness metrics are specified under Screening Stages, Stage 2.

#### Screening procedure justification

The four-stage design balances comprehensiveness with feasibility. Dual human screening at Stage 4 follows Cochrane Handbook, PRISMA 2020, and Waffenschmidt et al. (2019). LLM-assisted title/abstract screening at Stage 3 follows emerging 2024–2025 practice and is justified by (a) the high recall threshold enforced at pilot validation, (b) 100% human verification of LLM includes and uncertain decisions, (c) spot-checking of LLM excludes to detect false negatives, and (d) documented fallback to dual human screening if pilot thresholds fail.

#### Data management and sharing

All materials deposited on the OSF project page under a CC-BY 4.0 license with no embargo: Raw search exports (RIS and CSV per database) — /search_exports/ Deduplicated corpus (CSV with DOI, title, abstract, source) — /corpus/deduplicated.csv Pilot validation records with human and LLM decisions (CSV) — /screening/pilot_validation.csv Full screening log (CSV: record ID, reviewer, decision, exclusion code, timestamp) — /screening/screening_log.csv LLM prompts, versions, and API call logs — /screening/llm_artifacts/ Disagreement and adjudication log — /screening/adjudication_log.csv PRISMA 2020 flow diagram— /reporting/prisma_flow/ Work-in-progress files are committed daily to the project's GitHub repository (https://github.com/RaikoPipe/slr-artifacts), whose commit history serves as the timestamped audit trail. Third-party copyrighted content (full-text PDFs of included studies) is not redistributed; only metadata and decision records are shared.

#### Miscellaneous screening details

Reviewer workload per session capped at 2 hours to reduce fatigue-driven errors, following guidance from Wang et al. (2020) on screening accuracy decline over extended sessions. LLM screening runs are batched and timestamped to enable reproducibility checks. Prompts, model versions, and API call dates are logged at each screening run because model behavior drifts over API versions even when the version string is unchanged.

## Extraction

In this section, you register your plans for data extraction: the procedures you designed to extract the data you are interested in from the included sources. Examples of such data are text fragments, effect sizes, study design characteristics, year of publication, characteristics of measurement instruments, final verdicts and associated penalties in a legal system, company turnovers, sample sizes, or prevalences.

#### Entities to extract

Bibliographic metadata: DOI, title, authors, affiliations, country, publication year, venue, venue type (Q1–Q4 journal, conference proceedings, Tier 1 preprint), language, funding source. Study characterization: research type (empirical / conceptual / design-science), validation status (implemented-validated / prototype / framework-only / conceptual), industry sector, case study domain, stated research questions. Strategic planning scope: subdomain, specific planning task, time horizon explicitly stated (Y/N), planning horizon tier (strategic / upper tactical / ambiguous) system-configuring decision explicitly stated (Y/N), theoretical framework cited (VDI 5200 / SC Planning Matrix / Lanza et al. / Wiendahl-Nyhuis / other / none). LLM/AI intervention: LLM model(s) used, model family, open-weight vs. proprietary, fine-tuning (Y/N + method), architectural pattern (RAG / multi-agent / LLM+solver / LLM+digital twin / other), agentic architecture (single / multi / supervisor-agent), knowledge graph integration (Y/N), solver type if applicable, hybrid architecture description. OR/optimization substrate: underlying optimization tradition present (Y/N), formalization level (mature MILP / mid-maturity RL-metaheuristic / low-formalization / none). Evaluation and outcomes: validation method, dataset or benchmark used, reported metrics (efficiency gains, time savings, accuracy, hallucination rate, user acceptance), comparator (human planner / prior AI-ML / none), sample size, reported limitations. Gap indicators: HITL pattern present (Y/N + type), domain knowledge formalization present (Y/N + type), evaluation framework used (Y/N + type). Quality appraisal: study-type category (A: empirical / B: prototype-design-science / C: conceptual-framework), per-item scores (Yes / Partially / No) on Q1–Q4, venue tier, extraction provenance (metadata import / human / LLM-verified / LLM-corrected / dual). Reasoning: every extracted field is paired with a reasoning field stating the justification and an evidence locator (page/section and, for interpretive fields, a short verbatim anchor). Retrieval traceability: source (Scopus / WoS / OpenAlex / snowballing), anchor paper(s) if via snowballing.

#### Extraction stages

Stage 0: Bibliographic tier (metadata re-use) Bibliographic fields are imported from the deduplicated search-stage records (Scopus / WoS / OpenAlex; OpenAlex for snowballed records). Fields absent from the database record (e.g., funding, affiliation country) are filled by R1 from the title page or coded NR. Venue tier is looked up in Scimago for the publication year. Self-authored flag is set by matching author lists against the review team. Stage 1 pilot: R1 and R2 independently extract all descriptive and interpretive fields on 5 sources, blind to LLM output; the LLM pipeline extracts the same fields in parallel. Agreement is reported per field for R1–R2 and for LLM vs. the R1–R2 consensus value, separately for the descriptive and the interpretive tier. Thresholds: Gwet's AC1 ≥ 0.8 for categorical (prevalence-robust, consistent with the screening threshold; raw agreement reported alongside). Below threshold → revise instructions/prompt, re-pilot on 5 fresh sources. Interpretive fields still below the LLM–consensus threshold after one re-pilot revert to the originally registered procedure (manual extraction by R1, 100% verification by R2). Stage 2: Full extraction (LLM extraction + human verification) - Descriptive fields: LLM pre-fill with per-field reasoning, 100% R1 verification against source text. - Interpretive fields (gap indicators, quality appraisal, validation-status judgments): LLM extraction with per-field reasoning and evidence locator; 100% verification by R1 and 100% independent verification by R2, each blind to the other's verdicts. Values where R1 and R2 disagree are resolved by discussion; unresolved cases escalated to R3 with rationale logged. Stage 3: Quality appraisal Quality-appraisal items are part of the interpretive tier and follow the Stage 2 interpretive procedure. 

#### Extractor instructions

Extractor instructions stored on https://github.com/RaikoPipe/slr-artifacts as extraction_instructions_v5.md



#### Extractor masking

No masking applied. The SLR is descriptive/taxonomic, not effect-estimating.

#### Extraction reliability

Stage 0 bibliographic: imported from search-stage records; no reliability metric (deterministic). Stage 1 pilot: R1 + R2 blind manual extraction vs. LLM on 5 sources; per-field Gwet's AC1 (categorical) / % agreement (continuous) for R1–R2 and LLM–consensus, reported separately per tier. Stage 2 full extraction: descriptive fields LLM pre-fill + 100% R1 verification; interpretive fields LLM extraction + 100% R1 and 100% R2 independent verification. Reported: per-field LLM correction rate per verifier, and R1–R2 agreement (Gwet's AC1 and raw agreement) on post-verification interpretive values. 

#### Extraction reconciliation procedure

- Pilot: Field-by-field comparison; R1 and R2 discuss each disagreement, revise instructions. Unresolvable cases escalated to R3. - Full extraction: R1–R2 disagreements on verified interpretive values resolved by consensus discussion; unresolved → R3; decision logged in the field's reasoning column. Self-authored sources: R2 is the sole verifier for all tiers. - LLM-human: R1 decision authoritative. If ≥3 same-type LLM errors detected, prompt refined, affected records re-extracted, pre-registration updated.

#### Extraction procedure justification

Tiered approach follows PRISMA-trAIce (2024) guidance on human oversight of AI-assisted extraction. Bibliographic fields are taken from structured database records because they are authoritative, already deduplicated, and avoid LLM transcription errors. Interpretive fields are LLM-extracted to enforce a uniform, criterion-referenced first pass with explicit reasoning, and are then independently verified by two humans, so every final interpretive value is still confirmed by R1 and R2 as in the original dual-verification design. The pilot measures LLM accuracy against blind human extraction for both tiers and gates LLM use per field. Dual verification is limited to interpretive fields.

#### Data management and sharing

All extraction artifacts deposited on OSF under CC-BY 4.0 with no embargo: - LLM prompts, model versions, API call logs, extraction JSON schema - Pilot extraction results with dual-rater comparison - Adjudication log - Quality appraisal scores FAIR compliance: all files include persistent OSF identifiers, open access. Targeting 4-star open data per Berners-Lee's 5-star scheme. If a third-party API is used, source text (titles/abstracts/full-text excerpts) will be transmitted to the provider's cloud infrastructure. No personally identifiable data is involved. Use will comply with the respective provider's terms of service for research use. Authors retain no extracted data on third-party servers beyond the API call lifecycle. If a self-hosted open-weight model is used, no data leaves institutional infrastructure. The infrastructure choice will be documented with the submitted artifacts of each pipeline stage.

#### Miscellaneous extraction details

Extraction table structured as tidy data (one row per study, one column per field) with separate long-format table for multi-valued fields (e.g., multiple LLM models per study). All numeric metrics extracted with units and source page/section reference. Where primary source reports ranges or conditional values, all reported values captured with context. For non-reported fields, "not reported" is logged explicitly rather than left blank. LLM extraction input consists of the full-text PDF converted as markdown (using python library pymupdf) of each source, passed as a single document context. Bibliographic fields are not LLM-extracted (see Stage 0); for all other field categories, the full text is used. Each LLM-extracted value is returned together with a reasoning field (justification + evidence locator); free-text notes columns are replaced by these per-field reasoning columns, which verifiers amend when correcting a value. LLM extraction output is structured JSON conforming to the schema at [https://github.com/RaikoPipe/slr-data-model](https://github.com/RaikoPipe/slr-data-model), with one object per study. Raw output is validated against the schema before human review; schema-invalid outputs are flagged and re-extracted.

## Synthesis and Quality Assessment

In this section, you register the procedure for the review’s synthesis: the procedure you designed to use the data that was extracted from each source to answer your research question(s). This often includes transforming the raw extracted data, verifying validity, applying predefined inference criteria, interpreting results, and presenting results. Additionally, you register procedures you designed to assess bias in individual sources and the synthesis itself.

#### Planned data transformations

Extracted data will be transformed along three tracks: 1. Subdomain classification and architectural pattern fields recoded into controlled vocabularies for cross-tabulation (subdomain × architecture matrix). 2. OR formalization level cross-mapped against architectural pattern and validation status to operationalize the solver-specificity hypothesis. 3. Reported effectiveness metrics (too heterogeneous to aggregate quantitatively) tabulated as-reported with standardized context descriptors and synthesized narratively. Gap indicator fields (HITL, domain knowledge, evaluation framework) will be binarized per source and aggregated as gap-presence rates across the corpus.

#### Missing data

Fields not reported in a source are coded 'NR'. One author contact attempt will be made for missing data critical to RQ2. No imputation will be performed. Systematic patterns of missingness will be reported as a finding under RQ3.

#### Data validation

- All LLM-prefilled fields undergo human verification with error rates reported per field type. - Numeric metrics cross-checked against source text with page references logged. - Outlier metrics (2× the range of other sources for the same metric type) flagged, verified, and reported with context rather than excluded.

#### Quality assessment

Quality appraisal uses a lightweight bespoke checklist informed by the category-conditional logic of MMAT (Hong et al., 2018) and Hevner et al. (2004) design-science guidelines. Each source is first classified into one of three study-type categories, then appraised on four items scored Yes / Partially / No: Category A (Empirical): Primary data collection with a defined evaluation protocol (case studies with quantitative metrics, controlled benchmarks, user studies) Category B ( Prototype/Design Science): Implemented systems demonstrated on illustrative cases but without controlled evaluation Category C ( Conceptual/Framework only): Architectures, taxonomies, or frameworks without implementation or empirical evaluation Decision rules: a source with both a prototype and a controlled evaluation is classified as A; a prototype demonstrated on a single walkthrough without defined metrics is B. The category is derived from the extracted validation status (implemented-validated → A; prototype → B; framework-only or conceptual → C) so the two fields cannot diverge. Uncertain cases resolved by R1 + R2 discussion, escalated to R3 if unresolved. Classification rationale logged for every source. Appraisal items: Q1 (Methodological Transparency): Is the method (study design, system architecture, or framework logic) described with sufficient detail for independent replication? Q2 (Empirical or demonstration grounding): For A: are metrics defined and results reported with context (sample size, variance, comparator)? For B: is the artifact demonstrated on a case that exercises its core claims? For C: is the argumentation internally consistent and traceable? Q3 (Validity and limitation discussion): Are the boundaries of the contribution explicitly discussed — failure modes, scalability constraints, external validity, or domain assumptions? Q4 (Positioning against prior work): Is the contribution compared against existing solutions with explicit differentiation? Q2 is interpreted conditionally by study type. Items Q1, Q3, and Q4 apply uniformly. Venue tier is recorded as a separate descriptive field: Q1-Q2 journal: Scimago or JCR at time of publication Q3-Q4 / conference: Q3–Q4 journal or peer-reviewed conference proceedings Preprint: Tier 1 preprint (institutional affiliation, no peer review) Scoring and dual verification: Item-level results are reported per source in the extraction table. All appraisals are LLM-extracted and verified 100% by R1 and R2 as part of the interpretive tier; disagreements resolved by discussion, unresolved cases escalated to R3 with rationale logged. Sources receiving "No" on ≥ 2 of the 4 items are flagged as low quality. Quality scores are used for sensitivity analysis but not for exclusion.

#### Synthesis plan

Tier 1: Descriptive mapping (RQ1) Cross-tabulation of subdomain × architectural pattern generating a frequency matrix. Sources plotted on a subdomain coverage map. Second cross-tabulation maps subdomain × theoretical framework cited. Narrative synthesis accompanies each cell. Descriptive bibliometric profiling (publication trend by year, geographic distribution of corresponding authors, venue-type distribution, keyword co-occurrence) accompanies the subdomain × architecture cross-tabulation; PRISMA 2020 Flow Diagram Tier 2: Evidence appraisal (RQ2) Sources reporting quantitative outcomes tabulated by metric type, comparator, study design, and sample size. No meta-analysis. Harvest plot or evidence table groups claims by design strength. Negative evidence reported with equal prominence. Tier 3: Gap and barrier analysis (RQ3) Gap indicators aggregated as described in Planned Data Transformations. Additionally, author-stated limitations and future-work sections of included sources undergo lightweight inductive thematic coding to surface barriers and enablers beyond the three pre-hypothesized gaps. Emergent themes are reported alongside the deductive gap indicators. Tier 4 — Research framework (RQ1–RQ3) A conceptual framework is developed that maps the relationships between strategic planning subdomain, LLM architectural pattern, OR substrate maturity, and validation level. The framework integrates a consolidated taxonomy constructed from the subdomain × architectural pattern × validation status dimensions and a structured research agenda derived from confirmed gaps, thematic barrier analysis, and under-populated framework cells.

#### Criteria for conclusions / inference criteria

Gap confirmation: < 10% of sources address the gap → Structural absence confirmed 10–30% → Emerging but sparse coverage ≥ 30% → Gap not confirmed Evidence Robustness: Implemented-validated, independent comparator, n > 1: Robustly evidenced Implemented-validated, no independent comparator or n = 1: Partially evidenced Prototype, framework-only, or conceptual: Weakly evidenced

#### Synthesist blinding

No synthesist blinding is applied. Synthesis is conducted by R1 (primary researcher); blinding is infeasible given the domain expertise required for interpretive coding. R2 reviews synthesis tables; R3 reviews narrative and inferential claims.

#### Synthesis reliability

R1 is sole synthesist for all three tiers. Reliability ensured through: 1. Pre-registered inference criteria 2. All coding decisions traceable via provenance tags and extraction log 3. Sensitivity analysis/robustness check 4. Reviews by R2 and R3

#### Synthesis reconciliation procedure

Not applicable for synthesis (single synthesist).

#### Publication bias analyses

Formal publication bias tests are not applicable (no pooled effect sizes). Publication bias is addressed qualitatively: 1. Inclusion of preprints mitigates journal-only bias 2. Evidence table flags developer-reported results where positive-result bias is most acute 3. Negative evidence synthesized with equal weight 4. Discussion will explicitly address the risk that the corpus over-represents successful implementations

#### Sensitivity analyses / robustness checks

Two pre-registered sensitivity analyses: 1. Repeat Tier 1 cross-tabulation and Tier 3 gap-presence rates with sources scoring "No" on ≥ 2 quality appraisal items removed. 2. Repeat descriptive cross-tabulation excluding sources without explicit time-horizon or system-configuring framing or removing all upper-tactical-only sources

#### Synthesis procedure justification

Narrative synthesis with structured cross-tabulation is the appropriate method for a corpus of 25–40 sources spanning heterogeneous study designs, metrics, and subdomains. Meta-analysis is precluded by metric heterogeneity and the dominance of non-experimental designs. Gap confirmation at 10% corpus presence is conservative.

#### Synthesis data management and sharing

All synthesis files deposited on OSF: - extraction_table.csv - Cross-tabulation matrices (.csv) - Evidence tables (.csv) - Synthesis narrative notes (.md) - Analysis scripts if applicable (Python, .py) Files made public upon manuscript submission. No embargo planned.

#### Miscellaneous synthesis details

Sources classified as secondary literature are excluded from the synthesis corpus but retained in a separate reference list for snowballing traceability. Self-authored sources undergo dual extraction by R2 and are flagged in all synthesis tables.