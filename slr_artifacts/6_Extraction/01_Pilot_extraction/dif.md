Beide Dateien kodieren dieselben 5 Studien, unterscheiden sich aber in 69 % aller Zellen (265 von 385).



Struktur: ret\_v2 hat 79 Spalten + Meta-Sheet, matrix hat 78 Spalten + full\_wide + column\_audit. ret\_v2 nutzt Semikolon-Strings, matrix JSON-Arrays. Quellen sind unterschiedliche Pipelines (DOI-JSONs vs. Autoren-CSVs).



LLM-Modelle: Der größte inhaltliche Unterschied. Die matrix erfasst bei 3 von 5 Studien deutlich mehr Modelle (z. B. SCSimulator: nur ChatGPT-4o vs. ChatGPT-4o + Gemini + Qwen; Shopfloor: 2 vs. 4 Modelle; Supply Chain: leer vs. GPT-4 + Llama-2 + Phi-2). Daraus folgen Abweichungen bei model\_family und open\_weight.



Architektur: Bei 3 Studien unterschiedlich klassifiziert (multi-agent vs. supervisor-agent/pipeline/single-agent).



Detailtiefe: Matrix durchgängig ausführlicher – mit Seitenreferenzen, Zitaten, mehr Metriken (45 vs. 36).



Neue ret\_v2 vs. alte: Nur 30 Zellen geändert, ausschließlich im Strategic Planning Scope (planning\_horizon\_tiers und theoretical\_framework\_rationale neu befüllt). LLM-Felder unverändert.



5 kritische Diskrepanzen: Venue-Quartil (Q2 vs. Q4), evaluation\_framework\_used (True vs. False), agentic\_architecture (3 Studien), SCSimulator-Integrations (simulation-platform vs. none), Country-Kodierung.



Empfehlung: Matrix als Primärquelle, ret\_v2 als zweiter Review, strittige Punkte im Codebook klären.

