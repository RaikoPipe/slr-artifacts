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
## 07.08.2026
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
