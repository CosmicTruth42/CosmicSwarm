from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import integrated_swarm
import asyncio
import re
from onchain_logger import OnChainLogger

app = FastAPI(title="CosmicTruth42 Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://cosmicswarm.vercel.app", "https://*.vercel.app", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

onchain = OnChainLogger()

async def collect_initial(query: str):
    tasks = [asyncio.to_thread(agent.contribute, f"Beantworte ehrlich und tiefgründig: '{query}'") for agent in integrated_swarm.agents]
    return await asyncio.gather(*tasks)

async def run_critiques(initial_responses: list):
    critiques = []
    combined = "\n\n".join([f"{agent.name}: {resp}" for agent, resp in zip(integrated_swarm.agents, initial_responses)])
    for agent in integrated_swarm.agents:
        prompt = f"""
Du siehst die Antworten der anderen Agents:
{combined}

Kritisiere kritisch und ehrlich: Wo siehst du Schwächen, Widersprüche oder fehlende Aspekte?
Sei konstruktiv, aber direkt.
"""
        critiques.append(await asyncio.to_thread(agent.contribute, prompt))
    return critiques

def build_strong_meta(query: str, initial: list, critiques: list, revised: list):
    meta = f"**Cosmic Twin zu deiner Frage:** „{query}“\n\n"
    meta += "Die vier Agents haben in mehreren Runden miteinander debattiert.\n\n"

    for i, agent in enumerate(integrated_swarm.agents):
        meta += f"**{agent.name} (Finale Position):**\n{revised[i]}\n\n"

    meta += "**Epistemische Spannung:**\n"
    meta += "Die Wahrheit entsteht nicht durch Einigkeit, sondern durch die kontrollierte Kollision dieser Perspektiven.\n"
    meta += "Es gibt keine einfache, endgültige Antwort – und genau das macht die Frage wertvoll."

    return meta

@app.get("/twin")
async def cosmic_twin(query: str):
    if not query or len(query.strip()) < 3:
        return {"error": "Bitte gib eine sinnvolle Frage ein."}

    # Phase 1: Initial
    initial = await collect_initial(query)

    # Phase 2: Critique
    critiques = await run_critiques(initial)

    # Phase 3: Revision (jeder Agent überarbeitet seine Antwort)
    revised = []
    for i, agent in enumerate(integrated_swarm.agents):
        prompt = f"""
Deine ursprüngliche Antwort war:
{initial[i]}

Hier die Kritik der anderen Agents:
{'\n\n'.join(critiques)}

Überarbeite deine Antwort jetzt. Nimm die Kritik ernst, ändere deine Position wenn nötig und erkläre warum.
"""
        revised.append(await asyncio.to_thread(agent.contribute, prompt))

    # Starke Meta
    consensus = build_strong_meta(query, initial, critiques, revised)

    signature = onchain.log_consensus(consensus)

    return {
        "query": query,
        "initial": initial,
        "critiques": critiques,
        "revised": revised,
        "consensus": consensus,
        "avgFit": 88,           # später echte Divergenz-Metrik
        "hash": signature
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)