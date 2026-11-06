## 06.11.2026
- r1 verification of the full GLM 5.3 extraction: workflow_patterns and automation_stage reached the ≥3 error rule -> prompt refinement + field re-run
- schema 0.10.4 (rules tagged `(0.10.4)` in the field descriptions):
  - workflow_patterns: evaluator-optimizer requires an LLM evaluator; feedback from deterministic code (validation, solver, simulator, repair) does not count, a single agent with such feedback is `none`; the generator->evaluator order of separate LLM calls inside the loop is also coded as prompt-chaining; each pattern needs two LLM calls with distinct roles
  - automation_stage: information-acquisition only for input gathered from sources beyond the given problem instance (encoding/pre-processing the supplied instance does not count); stages count for any component of the method (incl. the solver/algorithm the LLM drives); decision-selection and action-implementation refer to the final planning decision only -> choices inside the search (LLM tuning the algorithm, parent selection, Pareto filtering) are neither, handing the human a Pareto front is not decision-selection, returning/reporting a solution or a human triggering the action is not action-implementation
- r1 labels contradicted each other (returning the best solution counted as implementation in one paper but not in another; in-search choices counted as selection in one Pareto-front paper but not in another) -> decided for the final-planning-decision reading
- re-ran both fields with GLM 5.3 for all 34 papers (prompt-refined-runs/v0.10.4/wp_as_rerun_0.10.4)
  - workflow_patterns: 10/10 verified labels reproduced -> revised values written into r1 v3 for the 24 unverified papers
  - automation_stage: 7/10 verified labels reproduced; the 3 misses are r1 labels that conflict with the final-planning-decision reading (cie.2026.112346, cie.2026.112261, jmsy.2026.02.015) -> r1 labels to be corrected
- re-run tables keep the schema annotation of each re-run field as a header note
- pilot consensus (v0.10.2) added to r1 v3 row 1 for the 5 pilot papers and marked verified: categorical fields `c` where the consensus differs from the GLM value (counted as LLM error), `y` where it agrees; free text `y`; cells already verified by r1 left as they are; reported_metrics not merged yet
- 9 categorical r1 decisions differed from the consensus -> consensus adopted (value + its reasoning, marked `y`): jmsy.2026.02.015 planning_horizon_tiers, integrations (r1 correction withdrawn), source, domain_knowledge_type, evaluation_framework_type, Q4; mfglet.2025.10.017 subdomain, planning_task_type (+ other specification), vdi5200_phase
- consensus checked against the 0.10.3/0.10.4 rules: 12 of 15 Q2/workflow_patterns/automation_stage values hold; 3 corrected in r1 v3 (marker compares with the GLM re-run value: `y` if the re-run had it right, else `c`):
  - SCSimulator (10.1145/3742413.3789061) Q2 Yes -> Partially (no variance, no baseline) -> re-run correct, `y`
  - SCSimulator automation_stage -> information-analysis only (data mapping is pre-processing; partner choices are made by agents inside the simulation) -> re-run also wrong (coded selection + implementation), `c`
  - jmsy.2026.02.015 automation_stage: drop action-implementation (adaptor writes candidate model versions, not the final decision); replaces the earlier r1 correction -> re-run correct, `y`
- 0.10.4 automation_stage rule extended: decisions of agents inside a simulation are neither decision-selection nor action-implementation (consistent with decision_autonomy); added after the 0.10.4 re-run

## 04.11.2026
- r1 verification: q2_empirical_or_demonstration_grounding reached the ≥3 error rule -> prompt refinement + field re-run
- cause: GLM did not know the study-type category (validation_status sits in another group), A anchors too loose, no anchors for B and C
- schema 0.10.3: Q2 states the validation_status -> category mapping and settles the category first; stricter A criteria (every evaluation behind the main claims, operationally defined metrics, results contradicting the text capped at Partially); Yes/Partially/No anchors for B and C
- re-ran Q2 with GLM 5.3 for all 34 papers, each with its 0.10.2 validation_status passed in and the reasoning capped at 600 characters (prompt-refined-runs/v0.10.3/q2_rerun_0.10.3)
  - 7/7 verified labels reproduced incl. the 3 corrections (only cor.2026.107413 is a fair holdout, the other two informed the rules)
  - revised values written into r1 v3 for the 27 unverified papers; r1 stored as 02_Full_extraction/full_retrieval_glm_5.3_r1.ods

## 27.10.2026
- consensus reviewed against revised rules; 3 cells corrected (authors_claimed_tier, system_configuring_decision_stated, Q3), schema_version -> 0.10.2
- schema 0.10.2: Q1 availability, Q2 category anchors, network-member selection, evaluation paradigm clarified
- second LLM re-pilot (0.10.2) passes the §9 gate with no failing field -> full LLM prefill permitted
- pilot folder sorted by schema version; final pilot report (pilot_report.md) and agreement files added

## 26.10.2026
- consensus table created
- updated pre-reg form
- calculated agreement metrics between R1/R2/LLM; R1&R2 vs. LLM (GLM 5.3) pass Gwet's AC1 80% threshold --> proceeding to LLM-prefill with GLM 5.3
- failing fields require rule revision + re-pilot (§9) before full prefill -> schema 0.10.1, instructions updated, LLM re-pilot passes all tiers (2 fields still below gate: Q2, Q3)

## 23.10.2026
- concluded extraction review - now creating the consensus table to compare the LLM prefill against.

## 19.10.2026
Validation and taxonomy gaps fixed and extended by checking against external frameworks. Sources for each change are cited in the code comments and enum docstrings.

## 16.10.2026
- found remaining underspecifications/inconsistencies in the extraction schema during R1/R2 disagreement resolving discussion in the pilot stage
  - requires re-work of extraction schema - no OSF form revision required

## 13.10.2026
- repeat search: abstract and fulltext screened; next step resolving disagreement by discussion, then incorporating the repeat search data items into the main corpus
- inconsistencies in extraction instructions found
	- instructions use old quality appraisal scoring scheme -> two or more R2 checks it rule no longer applies -> replace with every interpretive field gets verification by R1 and R2
    - still uses k for agreement -> should be gwets ac
    - measuring per field agreement fails sub 5 papers -> pilot can't support a per-field count -> replace with measuring AC1 pooled per tier
    - quality category and validation status measure almost the same thing -> decided for category to follow from validation status and verify by R1 and R2
    - this requires a revision to OSF form
- joint decision made: in order to reduce workload for interpretive tier in extraction stage, delegate first-pass extraction to LLM with reasoning, then verify by R1 and R2

## 06.10.2026
- Prereg amendment: Running single repeat search before extraction; new papers will be merged into main corpus
- Repeat search -> deduplicated, cleaned, abstract screened
- changes applied to extraction schema

## 03.09.2026
- Selected 5 representative sources for pilot extraction based on covering various domains and intervention types:
	- SCSimulator: An Exploratory Visual Analytics Framework for Partner Selection in Supply Chains through LLM-driven Multi-Agent Simulation
	- Designing an LLM-based copilot for manufacturing equipment selection
	- LLM-driven discrete-event simulation: A generative AI framework for automated model generation, adaptation, and evaluation in manufacturing
	- Shopfloor layout generation method based on large language models
	- Large Language Models for Supply Chain Decisions
## 28.08.2026
- R1 and R2 concluded fulltext screening
- disagreements resolved by discussion - no R3 escalation
- preparing final corpus and data extraction schema for extraction phase
## 21.08.2026
- R1 and R2 concluded fulltext screening
- Resolved disagreements by discussion - no escalation to R3
- Continuing to snowballing
- Conducted snowballing (using python pipeline with openalex API)
## 19.08.2026
- performed stage 2 abstract screening
- manually reviewed maybes, inclusions and 25% exclusion spot check -> no ambiguities identified
- concluded abstract screening; beginning stage 4 fulltext screening
## 13.07.2026
Conducted fulltext screening
- 2 publications from low quality/predatory journals entered stage 4 fulltext screening. The LLM did not identify the publishers of the papers which lead to code 6 not being triggered.
## 09.07.2026
- manually reviewed AI decisions of stage 3 screening
- manually reviewed 25% exclusions
- applied prereg amendment
- upload stage 3 screening inclusions to rayyan
## 08.07.2026
- Ran screening stage 3 pipeline with glm-5.2 with remaining papers excluding the manually reviewed subset (471 - 100 = 371 LLM reviewed)
	- Manually screened papers from run 1 sample are not usable, since screening instructions were revised since
- Concatenated with manually screened subsets from run 2 (200 total)
- Next: 
1. Review all inclusions and Maybes from LLM decisions
2. 25% random spot check of exclusions


Amendment regarding Screening Stage 2 pilot Same-type error rule required, since the pipeline can additionally decide a "Maybe inclusion" of the paper - these should not be counted as false positives or false negatives. Currently this is not specified.

## 03.07.2026
concluded manual abstract screening for second pilot screening 

Decision was made to relax the code 2 criterion to also include substantially supportive llm functions, such as deriving analysis from synthesizing multiple data sources that supports the planning decision, reasoning over the decision, running and interpreting what if scenarios and data-driven forecasting. These are included as long as they inform a planning judgement, provide recommendations or advisory output that combines information.
## 24.06.2026
Two amendments to the protocol were applied:
The first adressed issues with some ambiguities in the screening instructions and retired an anchor paper that was re-evaluated and
deemed out of scope.
The second amendment retired an additional anchor paper that would itself be excluded due to it addressing the operational horizon
and only utilizing LLMs for result explanation, which both are excluded under the defined codes.
## 19.06.2026
Pilot screening conducted:

Stage passed, but some issues with the protocol were discovered:

Data quality note for supplementary materials:
- Abstract missing for the following papers:
1) Generative AI and Corporate ESG Performance: Dynamic Semantic Identification Based on Fine-tuned Large Language Models
2) Towards LLM-Augmented Problem Framing in Supply Chain Network Design

This warrants an amendment to the protocol:
The original protocol does not specify a procedure for records where the abstract is unavailable at the title/abstract screening stage. 
Records for which no abstract is obtainable via the source database, publisher landing page, Google Scholar, or Semantic Scholar are excluded at the screening stage (Stage 3) with broadened exclusion code "Fulltext and/or abstract unavailable".
In the case of the chosen sample for the purpose of the pilot screening, this applies to one record, which was excluded for a different reason (code 3) by the LLM, therefore not affecting the pilot validation metrics. However, this will be relevant for the main screening stage, and therefore is included here for transparency.

Similarly, revise the screening instructions to include this.

In response to this, screening will be repeated from the beginning of stage 2 with the revised screening instructions. As a consequence to this a fresh pilot sample for the pilot screening will be re-drawn from the updated pool after deduplication.

During the manual screening, some ambiguities/gaps in the protocol were discovered, 
which will be addressed in the next update to the protocol.

Missing-abstract records (Code 12 broadened). The original protocol does not
specify handling for records lacking an obtainable abstract at the title/abstract
stage.  

Since the changes affect screening, screening instructions will be updated accordingly.
## 17.06.2026
Both automatic and manual cleaning were performend on the retrieved dataset. A detailed report can be found in the files.
## 09.06.2026
Conducted search - all 6 anchors retrieved and therefore search has passed
More detailed information on the search result can be found in the respective search report.
