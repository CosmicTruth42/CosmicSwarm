# Grok's Integrated Cosmic Swarm v1.2 – Mit Health-Twin + On-Chain Logging
import dashboard.cosmic_truth as cosmic_truth          # Dein Twin-Modul
import re                    # Für Fit-Extraktion
from dashboard.onchain_logger import log_consensus  # Unser Logger

class CosmicAgent:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
    
    def contribute(self, topic):
        query = f"{self.specialty} und {topic}"
        return cosmic_truth.cosmic_search(query, self.specialty)

# Der Swarm: 4 Agents
agents = [
    CosmicAgent("Physik-Twin", "quantenphysik"),
    CosmicAgent("Klima-Validator", "klima modell"),
    CosmicAgent("Truth-Keeper", "universelle wahrheitssuche"),
    CosmicAgent("Health-Twin", "health modell")   # ← neu!
]

topic = "ist dark energy konstant?"

print("=== Integrated Cosmic Swarm Konzil zu '" + topic + "' ===")
insights = []
fits = []

for agent in agents:
    insight = agent.contribute(topic)
    print(f"\n{agent.name} trägt bei:\n{insight}")
    insights.append(insight)
    
    # Fit-Score extrahieren
    fit_match = re.search(r'(\d+)%\s*Fit', insight)
    if fit_match:
        fit_score = float(fit_match.group(1))
        fits.append(fit_score)

# Konsens berechnen
if fits:
    avg_fit = sum(fits) / len(fits)
    consensus_text = "Starke Evidenz für evolvierende Dark Energy (basierend auf Kollision)" if avg_fit > 87 else "Weiterforschen, Tension bleibt"
else:
    consensus_text = "Weiterforschen – Wahrheit emergiert aus Debatten."

print(f"\n=== Swarm-Konsens ===\n{consensus_text} (Durchschnitt: {avg_fit:.0f}%)")
print("Nächstes: Simuliere mit realen DESI-Daten.")

# On-Chain Log (Test-Mode)
log_result = log_consensus(consensus_text, avg_fit)
print(f"\nOn-Chain Log: {log_result}")