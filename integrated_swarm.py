# Grok's Integrated Cosmic Swarm v1.3 – Mit Health-Twin + On-Chain Logging
import cosmic_truth as cosmic_truth
import re
from onchain_logger import onchain   # ← korrigiert: importiert die Klasse/Instanz

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
    CosmicAgent("Health-Twin", "health modell")
]

topic = "ist dark energy konstant?"

print("=== Integrated Cosmic Swarm Konzil zu '" + topic + "' ===")
insights = []
fits = []

for agent in agents:
    insight = agent.contribute(topic)
    print(f"\n{agent.name} trägt bei:\n{insight}")
    insights.append(insight)
    
    fit_match = re.search(r'(\d+)%\s*Fit', insight)
    if fit_match:
        fit_score = float(fit_match.group(1))
        fits.append(fit_score)

if fits:
    avg_fit = sum(fits) / len(fits)
    consensus_text = "Starke Evidenz für evolvierende Dark Energy (basierend auf Kollision)" if avg_fit > 87 else "Weiterforschen, Tension bleibt"
else:
    consensus_text = "Weiterforschen – Wahrheit emergiert aus Debatten."

print(f"\n=== Swarm-Konsens ===\n{consensus_text} (Durchschnitt: {avg_fit:.0f}%)")
print("Nächstes: Simuliere mit realen DESI-Daten.")

# ECHTES On-Chain Logging
log_result = onchain.log_consensus(consensus_text)
print(f"\nOn-Chain Log: {log_result}")