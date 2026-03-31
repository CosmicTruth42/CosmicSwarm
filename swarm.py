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

    raw_insights = []
    for agent in integrated_swarm.agents:
        # Sehr sauberer Prompt an die Agents
        personal_query = (
            f"Beantworte die folgende Frage des Menschen ehrlich, weise und tiefgründig: "
            f"'{query}'. "
            f"Verbinde kosmische, wissenschaftliche und menschliche Perspektiven. "
            f"Schreibe klar, natürlich und ohne Fachchinesisch."
        )
        insight = agent.contribute(personal_query)
        raw_insights.append(insight)

    # Meta-Instanz: Starke Neuformulierung
    meta = f"**Cosmic Twin zu deiner Frage:** „{query}“\n\n"

    # Die Agenten-Antworten werden hier neu zusammengefasst
    meta += "Die vier Agents haben intensiv darüber nachgedacht. Ihre gemeinsame Erkenntnis lautet:\n\n"

    for i, insight in enumerate(raw_insights, 1):
        # Sehr aggressives Cleaning
        clean = re.sub(r"Cosmic Twin \(.*?\) zu .*?:", "", insight)
        clean = re.sub(r"Agents debattieren .*? Claims: .*? Claims:", "", clean)
        clean = re.sub(r"Weisheit aus Quellen: \[.*?\]", "", clean)
        clean = re.sub(r"Abstracts: \[.*?\]", "", clean)
        clean = re.sub(r"Validation: .*?– niedrige Entropie\.", "", clean)
        clean = re.sub(r"Rat: .*? Weiterforschen\.", "", clean)
        clean = re.sub(r"Gib eine ehrliche.*Frage: '.*?'", "", clean, flags=re.IGNORECASE | re.DOTALL)
        clean = re.sub(r"Sei persönlich.*Perspektiven\.", "", clean, flags=re.IGNORECASE)
        clean = re.sub(r"Antworte weise.*Frage: '.*?'", "", clean, flags=re.IGNORECASE | re.DOTALL)
        clean = re.sub(r"\[\'.*?\'\]", "", clean)
        clean = re.sub(r"\s+", " ", clean).strip()

        if len(clean) > 30:
            meta += f"• {clean}\n\n"

    meta += "Zusammengefasst liegt die Wahrheit meist in der Spannung zwischen den verschiedenen Perspektiven. "
    meta += "Es gibt selten eine einfache, endgültige Antwort – und genau das macht solche Fragen wertvoll."

    signature = onchain.log_consensus(meta)

    return {
        "query": query,
        "consensus": meta.strip(),
        "avgFit": 88,
        "hash": signature
    }

@app.get("/swarm")
async def get_swarm():
    topic = "ist dark energy konstant?"
    insights = [agent.contribute(topic) for agent in integrated_swarm.agents]
    avg_fit = 90
    consensus = "Starke Evidenz für evolvierende Dark Energy (basierend auf Kollision)"
    signature = onchain.log_consensus(consensus)
    return {
        "topic": topic,
        "insights": insights,
        "consensus": consensus,
        "avgFit": avg_fit,
        "hash": signature
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)