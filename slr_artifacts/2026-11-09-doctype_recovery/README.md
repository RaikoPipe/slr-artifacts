# Document-type recovery (09.11.2026)

Protocol deviation: the automated cleaning step (`slr_tools.cleaning_pipeline.drop_invalid_types`) compared
`doc_type` case-sensitively against OpenAlex's type vocabulary and did not list `conference-paper`. Scopus/WoS
records (`Article`, `Article; Early Access`, `Conference Paper`, `Book Chapter`, `Book`, WoS `Meeting`) and all
OpenAlex conference papers were removed before title/abstract screening. The registered Stage 1 contains no
document-type filter, and conference proceedings are a registered venue type.

## Corrected rule (fixed before any recovered record was screened)

Types are normalised to the OpenAlex vocabulary (lower case, first part before `;`, spaces -> `-`, WoS `Meeting`
and `Proceedings Paper` -> `conference-paper`, `Editorial material` -> `editorial`).

- kept: article, conference-paper, book-chapter, book, preprint, report, dissertation
- still excluded (unchanged): review, conference review, conference-abstract, editorial, letter, erratum, paratext,
  dataset, software, peer-review, supplementary-materials, reference-entry, other

All records that pass the corrected rule are recovered, regardless of topic.

## Procedure (`2_Screening/1_Deduplication/`)

The scripts are in `slr-tools/scripts/doctype_recovery/`. Run each one from `2_Screening/1_Deduplication/`
(it reads and writes the files there), e.g.
`python /home/rreider/PycharmProjects/slr-tools/scripts/doctype_recovery/recover_doc_type.py`.

1. `recover_doc_type.py`
   - Original search and 06.10.2026 corpus update: the records removed at the doc_type step (from the saved
     exclusion logs, which ran after deduplication, retraction and year) are re-checked with the corrected rule and
     the language step that followed it. Earlier decisions, including the human deduplication choices, are kept.
   - Snowballing: no exclusion log was saved, so the corrected cleaning steps are re-applied to all candidates in
     `5_Snowballing/1_Search/snowball_out.csv`.
   - All recovered records are then deduplicated against every record that already entered screening (DOI,
     normalised title; fuzzy title >= 80 flagged for review in `fuzzy_matches_for_review.csv`).
   - Output: `dataset_recovered_cleaned.csv`, `exclusion_log_auto.csv`.
2. `fill_abstracts.py`: missing abstracts were looked up via OpenAlex and Semantic Scholar (amendment 19.06.2026).
   Output: `dataset_recovered_cleaned_abstract_filled.csv`; `abstract_source` shows where each abstract came from.
3. `fill_abstracts_publisher.py`: second pass for the rest via Crossref and the publisher landing page (doi.org);
   updates the same file (`abstract_source` = `publisher_page`).

4. `fuzzy_title_candidates.py`: candidate pairs for the human fuzzy-title deduplication step (registered Stage 1,
   step 3). It uses the same matcher as `slr_tools.defuzzer` (fuzz.ratio, threshold 80) on normalised titles. Pairs
   are checked within the recovered set and against everything already screened, and pairs from 70 to 80 are also
   listed. Output: `fuzzy_title_candidates.csv`, with a `human_decision` column for the reviewer.

5. `fetch_languages.py`: Scopus/WoS exports carry no language. It fetches the document language from the
   Scopus Abstract Retrieval API (FULL view, by EID or DOI), then Crossref, then OpenAlex (inferred, last resort),
   recorded in `language`/`language_all`/`language_source`. It then applies the pipeline's language step (en/de)
   and appends exclusions to `exclusion_log_auto.csv`. Output: **`dataset_recovered_for_screening.csv`** (input for
   title/abstract screening).

## Result

| Source | Removed by old step | Recovered for screening |
|---|---|---|
| Original search | 172 | 96 (64 article, 30 conference-paper, 2 book-chapter) |
| Corpus update 06.10.2026 | 129 | 84 (65 conference-paper, 16 article, 2 book-chapter, 1 book) |
| Snowballing | no log | 42 (41 conference-paper, 1 article) |
| **Total** | | **222** |

- 30 recovered records were already screened through another copy (another database, snowballing), and 1 was a duplicate within the recovered set.
- Language: 207 from Scopus, 1 from Crossref, 12 inferred by OpenAlex. 13 are excluded under code 8 (12 Chinese journal papers, all confirmed by Scopus; 1 Turkish snowball record), which leaves **209 records for screening**. 2 have no language source: the WoS proceedings records without a DOI, which need a manual check.
- 5 records are still without an abstract after both passes (19 were filled from publisher pages). They need a manual Google Scholar check before code 12: rsm.2023.0670, jmai-24-31, jclepro.2021.129830, and two WoS proceedings records without a DOI ("Prescriptive AI in Practice…", "AI and its successful implementation in organizational processes…").

## Title/abstract screening (`3_Abstract_Screening/`)

GLM 5.2 (`glm-5.2:cloud`, seed 0, temperature 0, prompt_version b2d6a5ed, the same prompt as the 06.10.2026 corpus
update), 209 records, run 09.11.2026 with a per-record checkpoint.

- Result: **8 Include, 9 Maybe, 192 Exclude** (code 2: 80, 3: 64, 1: 36, 5: 7, 4: 2, 10: 2, 12: 1).
- The Ollama usage limit (HTTP 429) interrupted the run twice. Failed calls were not checkpointed and were screened
  again after the reset. 10.3390/en19153539 failed in the last batch, so it was screened again on 10.11.2026 with the
  same settings (Exclude, code 1) and merged into the CSV. Its audit is `screening_audit_20261110_fed41a.md`.
  `screening_audit_20261109_9ce26f.md` still lists it as an LLM-failed Maybe.
- `r1_verification_worklist.csv` (65 records): all 17 includes and maybes, plus 48 excludes, a 25% random sample
  (`sample(frac=0.25, random_state=42)`, as in the main screening). R1 fills `r1_decision`, `r1_excl_code` and
  `r1_note`. The code 12 exclusion in the sample needs the manual abstract check.

## Next stages (same procedure as the main screening)

- `3_Abstract_Screening`: R1 verification (worklist above).
- `4_Fulltext_Screening`: R1 + R2 blind. Self-authored papers go to R2.
- New includes are snowballed and extracted with schema 0.10.5.
