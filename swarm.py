from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import integrated_swarm
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

@app.get("/twin")
async def cosmic_twin(query: str):
    if not query or len(query.strip()) < 3:
        return {"error": "Bitte gib eine sinnvolle Frage ein."}

    # === 1. Roh-Antworten der Agents ===
    raw_insights = []
    for agent in integrated_swarm.agents:
        personal_query = f"Beantworte die folgende Frage des Menschen ehrlich, weise und tiefgründig: '{query}'."
        insight = agent.contribute(personal_query)
        raw_insights.append(insight)

    # === 2. Starkes Cleaning (deine bestehende Logik behalten + leicht verbessert) ===
    clean_insights = []
    for text in raw_insights:
        clean = re.sub(r"Cosmic Twin \(.*?\) zu .*?:", "", text, flags=re.IGNORECASE)
        clean = re.sub(r"Agents debattieren .*? Claims: .*? Claims:", "", clean)
        clean = re.sub(r"Weisheit aus Quellen: \[.*?\]", "", clean)
        clean = re.sub(r"Abstracts: \[.*?\]", "", clean)
        clean = re.sub(r"Validation: .*?– niedrige Entropie\.", "", clean)
        clean = re.sub(r"\s+", " ", clean).strip()
        if len(clean) > 30:
            clean_insights.append(clean)

    # === 3. Starke, aktive Meta-Instanz (weniger Glättung, mehr Divergenz) ===
    meta = f"**Cosmic Twin zu deiner Frage:** „{query}“\n\n"
    meta += "Die vier spezialisierten Agents haben unabhängig darüber nachgedacht. Hier ihre Perspektiven:\n\n"

    for i, text in enumerate(clean_insights[:4]):
        agent_name = integrated_swarm.agents[i].name if i < len(integrated_swarm.agents) else f"Agent {i+1}"
        meta += f"**{agent_name}**: {text}\n\n"

    meta += "Die Wahrheit entsteht in der **Spannung** zwischen diesen Perspektiven. "
    meta += "Es gibt keine einfache, endgültige Antwort – und genau das ist der Wert dieser Frage."

    signature = onchain.log_consensus(meta)

    return {
        "query": query,
        "insights": raw_insights,      # für Debugging
        "consensus": meta.strip(),
        "avgFit": 88,                  # später echte Metrik
        "hash": signature
    }

@app.get("/swarm")
async def get_swarm():
    # Test-Endpoint bleibt erstmal gleich
    topic = "ist dark energy konstant?"
    insights = [agent.contribute(topic) for agent in integrated_swarm.agents]
    return {
        "topic": topic,
        "insights": insights,
        "consensus": "Starke Evidenz für evolvierende Dark Energy (basierend auf Kollision)",
        "avgFit": 90,
        "hash": "test-hash"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)