1. Modell-Erkennung – review_matrix ist deutlich vollständiger:

Studie	retrieval_v2 models	review_matrix models
Werheid (Copilot)	GPT-4o; all-MiniLM-L6-v2	GPT-4o + all-MiniLM-L6-v2 (mit Anmerkung: Embedding-Modell, kein generatives LLM)
DES Simulation	GPT-4o; GPT-5-mini; GPT-5.1	identisch, aber mit API-Zugangsart
Supply Chain Decisions	(leer!)	GPT-4, Llama-2, Phi-2 – deutlich mehr extrahiert
SCSimulator	nur ChatGPT-4o	ChatGPT-4o, Gemini-2.5-flash, Qwen3-VL-Flash
Shopfloor Layout	ChatGPT; GPT-4	GPT-4, GPT-3.5-turbo, ChatGLM3-6B, Mixtral 8x7B

→ retrieval_v2 hat bei 3 von 5 Studien Modelle übersehen, die in den Experimenten verglichen wurden.

2. Model Family – konsistent dazu:

SCSimulator: retrieval_v2 sagt nur „GPT", review_matrix kodiert korrekt GPT + Gemini + Qwen.
Shopfloor: retrieval_v2 nur „GPT", review_matrix ergänzt Mistral und other (ChatGLM).
Supply Chain: retrieval_v2 nur „other", review_matrix nennt GPT, Llama, other.

3. Open Weight – widersprüchliche Kodierungen:

Werheid: retrieval_v2 sagt „mixed" (wegen MiniLM), review_matrix sagt „N" (weil MiniLM kein generatives Modell ist) – eine inhaltlich begründete Entscheidung.
Supply Chain: genau umgekehrt – retrieval_v2 „N", review_matrix „mixed" (weil Llama-2 und Phi-2 open-weight sind).
Shopfloor: retrieval_v2 „N", review_matrix „mixed" (wegen Mixtral und ChatGLM).

4. Architektur-Klassifikation – teils stark abweichend:

Werheid: multi-agent vs. supervisor-agent
DES Simulation: multi-agent vs. pipeline
Shopfloor: pipeline vs. single-agent

5. Integrations:

SCSimulator: simulation-platform vs. none – gegensätzliche Kodierung.

Fazit: Die review_matrix hat die LLM-Interventionen deutlich gründlicher extrahiert – insbesondere bei der Erfassung aller getesteten Modelle (nicht nur des Hauptmodells), bei der Begründung der Open-Weight-Kodierung und bei den architektonischen Patterns. Die retrieval_v2 scheint oft nur das prominenteste Modell erfasst zu haben und bei der Architektur-Klassifikation weniger differenziert zu sein.