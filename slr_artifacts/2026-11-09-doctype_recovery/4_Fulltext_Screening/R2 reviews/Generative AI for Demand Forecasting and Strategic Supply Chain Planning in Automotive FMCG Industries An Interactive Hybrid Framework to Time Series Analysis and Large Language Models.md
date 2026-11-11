# R2 Review

**REJECT - Codes 1, 3**

|Code|Criterion|Assessment|
|---|---|---|
|1|Exclusively operational/tactical|**REJECT -** Despite “strategic” in the title, the decisions supported are demand forecasting, safety/buffer stock levels, procurement timing and SKU prioritisation during seasonal peaks. These are operational/tactical inventory and S&OP-type decisions inside a fixed configuration, with no change to capacity, sites or network structure.|
|2|No qualifying LLM component|**PASS -** A LLaMA-based LLM (run via Ollama) turns disruption-adjusted Prophet forecasts into natural-language recommendations and supports what-if scenario analysis. This counts as qualifying advisory and scenario-interpretation output.|
|3|Does not address strategic manufacturing/logistics planning task|**REJECT -** No strategic planning task is addressed. The only supplier-related output, suggesting alternate suppliers under disruption risk, is procurement within a fixed network and does not set production-network topology or site/echelon structure.|
|4|AI/ML without LLM component|**PASS -** An LLM component is present alongside Prophet, LSTM and ARIMA.|
|5|Non-manufacturing/logistics domain|**PASS -** The domains are automotive spare-parts supply chains and FMCG supply chains, both in a production/distribution network context. Note that the FMCG data is retail sales.|
|6|Grey literature below Tier 1|**PASS -** Peer-reviewed IEEE conference proceedings (TQCEBT 2026, DOI 10.1109/TQCEBT67648.2026.11681857).|
|7|Published before January 2022|**PASS -** The conference took place on 9-11 April 2026.|
|8|Language not English/German|**PASS -** English.|
|9|Editorial/opinion only|**PASS -** Primary study with a proposed framework and an empirical evaluation (MAE/RMSE/MAPE, stockout rate).|
|10|Secondary literature|**PASS -** Primary research, not a review.|
|11|Duplicate|**PASS -** No duplicate record is known. Check against the corpus.|
|12|Full text unavailable|**PASS -** Full text available (5 pages, IEEE Xplore).|
