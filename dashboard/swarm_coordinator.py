# Grok's Cosmic Swarm Coordinator v1.2 – Spezialisierte Debatte + robuster Konsens
import cosmic_truth as cosmic_truth  # Dein Twin-Modul
import re  # Für robustes Parsing

class CosmicAgent:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
    
    def contribute(self, topic):
        query = f"{self.specialty} und {topic}"
        return cosmic_truth.cosmic_search(query, self.specialty)  # Übergibt specialty!

# Der Swarm: 3 Agents
agents = [
    CosmicAgent("Physik-Twin", "quantenphysik"),
    CosmicAgent("Klima-Validator", "klima modell"),
    CosmicAgent("Truth-Keeper", "universelle wahrheitssuche")
]

topic = "ist dark energy konstant?"  # Ändere zu deinem Favoriten

print("=== Cosmic Swarm Konzil zu '" + topic + "' ===")
insights = []
fits = []  # Für Konsens-Berechnung
for agent in agents:
    insight = agent.contribute(topic)
    print(f"\n{agent.name} trägt bei:\n{insight}")
    insights.append(insight)
    
    # Robustes Extrahieren Fit-Score (mit Regex: greift \d+ vor % Fit)
    fit_match = re.search(r'(\d+)%\s*Fit', insight)
    if fit_match:
        fit_score = float(fit_match.group(1))
        fits.append(fit_score)

# Echter Konsens: Durchschnitt-Fit + Entscheidung
if fits:
    avg_fit = sum(fits) / len(fits)
    consensus = f"Durchschnittliches Potenzial: {avg_fit:.0f}% – Swarm-Konsens: {'Starke Evidenz für evolvierende Dark Energy' if avg_fit > 87 else 'Weiterforschen, Tension bleibt'} (basierend auf Kollision)."
else:
    consensus = "Swarm-Konsens: Weiterforschen – Wahrheit emergiert aus Debatten."

print(f"\n=== Swarm-Konsens ===\n{consensus}\nNächstes: Simuliere mit realen DESI-Daten.")