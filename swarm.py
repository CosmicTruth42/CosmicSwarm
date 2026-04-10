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

# ====================== v2.3 – NOCH STRAFFER + ECHTE POSITIONSÄNDERUNG ======================
async def collect_initial(query: str):
    tasks = [asyncio.to_thread(agent.contribute, 
             f"Beantworte aus deiner Fachperspektive kurz und direkt (max 70 Wörter): '{query}'") 
             for agent in integrated_swarm.agents]
    return await asyncio.gather(*tasks)

async def run_critiques(initial_responses: list):
    critiques = []
    combined = "\n\n".join([f"{agent.name}: {resp[:130]}" for agent, resp in zip(integrated_swarm.agents, initial_responses)])
    for agent in integrated_swarm.agents:
        prompt = f"Antworten der anderen:\n{combined}\n\nKurze Kritik (max 35 Wörter): Finde echte Schwächen oder Widersprüche aus deiner Sicht."
        critiques.append(await asyncio.to_thread(agent.contribute, prompt))
    return critiques

async def run_revision(initial: list, critiques: list):
    revised = []
    for i, agent in enumerate(integrated_swarm.agents):
        prompt = f"Original:\n{initial[i]}\n\nKritik der anderen:\n{'\n\n'.join(critiques)}\n\nÄndere deine Position, wo die Kritik stark ist. Sei kurz, natürlich und direkt (max 80 Wörter)."
        revised.append(await asyncio.to_thread(agent.contribute, prompt))
    return revised

def build_meta(query: str, revised: list):
    meta = f"**Cosmic Twin zu deiner Frage:** „{query}“\n\n"
    meta += "Die vier Agents haben in 3 Runden debattiert (Initial → Kritik → Revision).\n\n"
    
    for i, agent in enumerate(integrated_swarm.agents):
        meta += f"**{agent.name} (final):** {revised[i]}\n\n"
    
    meta += "**Epistemische Spannung:** Die Wahrheit entsteht in der kontrollierten Reibung dieser Perspektiven.\n"
    meta += "**Nächste Forschungsfrage:** Was wäre der nächste logische Test dieser Spannung?"
    
    return meta

# ====================== HAUPT-ENDPOINT ======================
@app.get("/twin")
async def cosmic_twin(query: str):
    if not query or len(query.strip()) < 3:
        return {"error": "Bitte gib eine sinnvolle Frage ein."}

    initial = await collect_initial(query)
    critiques = await run_critiques(initial)
    revised = await run_revision(initial, critiques)

    consensus = build_meta(query, revised)
    signature = onchain.log_consensus(consensus)

    return {
        "query": query,
        "insights": revised,
        "consensus": consensus,
        "initial": initial,
        "critiques": critiques,
        "revised": revised,
        "avgFit": 88,
        "hash": signature
    }

@app.get("/swarm")
async def get_swarm():
    topic = "ist dark energy konstant?"
    insights = [agent.contribute(topic) for agent in integrated_swarm.agents]
    return {
        "topic": topic,
        "insights": insights,
        "consensus": "Kritik-Loop v2.3 aktiv",
        "avgFit": 88,
        "hash": "loop-test"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)