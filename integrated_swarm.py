# Grok's Integrated Cosmic Swarm v1.6 – mit Role-Prompts für Kritik-Loop
import cosmic_truth as cosmic_truth

class CosmicAgent:
    def __init__(self, name, specialty, role_prompt=""):
        self.name = name
        self.specialty = specialty
        self.role_prompt = role_prompt or f"Du bist der {name} im CosmicTruth42-System."

    def contribute(self, prompt: str):
        full_prompt = f"{self.role_prompt}\n\n{prompt}"
        return cosmic_truth.cosmic_search(full_prompt, self.specialty)

# Der Swarm: 4 Agents mit klaren Rollen
agents = [
    CosmicAgent("Physik-Twin", "quantenphysik", "Du bist der Physik-Twin. Sei präzise, wissenschaftlich und kosmisch tiefgründig."),
    CosmicAgent("Klima-Validator", "klima modell", "Du bist der Klima-Validator. Verbinde kosmische Prozesse mit irdischen Auswirkungen."),
    CosmicAgent("Truth-Keeper", "universelle wahrheitssuche", "Du bist der Truth-Keeper. Betone epistemische Bescheidenheit und Spannung."),
    CosmicAgent("Health-Twin", "health modell", "Du bist der Health-Twin. Verbinde kosmische Einflüsse mit menschlicher Gesundheit und Bewusstsein.")
]