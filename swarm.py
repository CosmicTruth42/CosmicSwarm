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

# ====================== NEUER KRITIK-LOOP ======================
async def collect_initial(query: str):
    tasks = [asyncio.to_thread(agent.contribute, f"Beantworte ehrlich und tiefgründig: '{query}'") for agent in integrated_swarm.agents]
    return await asyncio.gather(*tasks)

async def run_critiques(initial_responses: list):
    critiques = []
    combined = "\n\n".join([f"{agent.name}: {resp}" for agent, resp in zip(integrated_swarm.agents, initial_responses)])
    for agent in integrated_swarm.agents:
        prompt = f"Du siehst die Antworten der anderen:\n{combined}\n\nKritisiere kritisch und ehrlich: Wo siehst du Schwächen, Widersprüche oder fehlende Aspekte?"
        critiques.append(await asyncio.to_thread(agent.contribute, prompt))
    return critiques

async def run_revision(initial: list, critiques: list):
    revised = []
    for i, agent in enumerate(integrated_swarm.agents):
        prompt = f"Deine ursprüngliche Antwort:\n{initial[i]}\n\nKritik der anderen:\n{'\n\n'.join(critiques)}\n\nÜberarbeite deine Antwort jetzt."
        revised.append(await asyncio.to_thread(agent.contribute, prompt))
    return revised

def build_meta(query: str, revised: list):
    meta = f"**Cosmic Twin zu deiner Frage:** „{query}“\n\n"
    meta += "Die Agents haben in 3 Runden miteinander debattiert (Initial → Kritik → Revision).\n\n"
    for i, agent in enumerate(integrated_swarm.agents):
        meta += f"**{agent.name} (final):** {revised[i]}\n\n"
    meta += "Die Wahrheit entsteht in der **Spannung** zwischen diesen Perspektiven."
    return meta

# ====================== HAUPT-ENDPOINT (neu) ======================
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
        "initial": initial,
        "critiques": critiques,
        "revised": revised,
        "consensus": consensus,
        "avgFit": 88,
        "hash": signature
    }

# ====================== ALTER ENDPOINT (für Dashboard-Kompatibilität) ======================
@app.get("/swarm")
async def get_swarm():
    """Temporärer Wrapper – damit das alte Dashboard weiterhin funktioniert"""
    # Einfache Test-Antwort für den alten Endpoint
    topic = "ist dark energy konstant?"
    insights = [agent.contribute(topic) for agent in integrated_swarm.agents]
    return {
        "topic": topic,
        "insights": insights,
        "consensus": "Starke Evidenz für evolvierende Dark Energy (Kritik-Loop aktiv)",
        "avgFit": 88,
        "hash": "loop-test"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)