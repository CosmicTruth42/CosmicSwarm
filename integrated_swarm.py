# Grok's Integrated Cosmic Swarm v1.5 – Sauberer Prompt an Agents
import cosmic_truth as cosmic_truth

class CosmicAgent:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
    
    def contribute(self, full_prompt: str):
        # Jetzt wird der saubere Prompt aus swarm.py direkt übergeben
        return cosmic_truth.cosmic_search(full_prompt, self.specialty)

# Der Swarm: 4 Agents
agents = [
    CosmicAgent("Physik-Twin", "quantenphysik"),
    CosmicAgent("Klima-Validator", "klima modell"),
    CosmicAgent("Truth-Keeper", "universelle wahrheitssuche"),
    CosmicAgent("Health-Twin", "health modell")
]