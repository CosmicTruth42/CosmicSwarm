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

@app.get("/swarm")
async def get_swarm():
    topic = "ist dark energy konstant?"
    insights = []
    fits = []
    for agent in integrated_swarm.agents:
        insight = agent.contribute(topic)
        insights.append(insight)
        fit_match = re.search(r'(\d+)%\s*Fit', insight)
        if fit_match:
            fits.append(float(fit_match.group(1)))
    avg_fit = round(sum(fits) / len(fits)) if fits else 90
    consensus = "Starke Evidenz für evolvierende Dark Energy (basierend auf Kollision)" if avg_fit > 87 else "Weiterforschen, Tension bleibt"
    signature = onchain.log_consensus(consensus)
    return {
        "topic": topic,
        "insights": insights,
        "consensus": consensus,
        "avgFit": avg_fit,
        "hash": signature
    }

@app.get("/twin")
async def cosmic_twin(query: str):
    """Cosmic Twin – jetzt wirklich dynamisch"""
    if not query or len(query.strip()) < 3:
        return {"error": "Bitte gib eine sinnvolle Frage ein."}

    insights = []
    fits = []

    for agent in integrated_swarm.agents:
        # Jeder Agent bekommt die echte Frage + persönlichen Kontext
        personal_query = f"Gib eine ehrliche, nuancierte und weise Antwort auf diese konkrete Frage des Menschen: '{query}'. Sei tiefgründig, vermeide Floskeln und verbinde kosmische, wissenschaftliche und menschliche Perspektiven."
        insight = agent.contribute(personal_query)
        insights.append(insight)
        
        fit_match = re.search(r'(\d+)%\s*Fit', insight)
        if fit_match:
            fits.append(float(fit_match.group(1)))

    avg_fit = round(sum(fits) / len(fits)) if fits else 88

    # Dynamische Synthese – hier wird die echte Antwort aus den Agenten zusammengefasst
    consensus = f"Cosmic Twin zu deiner Frage '{query}':\n\n"
    consensus += "Die Agents haben intensiv debattiert. Zusammengefasst ergibt sich folgendes Bild:\n\n"
    
    # Kurze Zusammenfassung der wichtigsten Punkte aus den Insights
    key_points = [insight.split("Rat:")[0][-150:] if "Rat:" in insight else insight[-120:] for insight in insights]
    consensus += " • " + "\n • ".join(key_points[:3]) + "\n\n"
    consensus += "Gesamteinschätzung: Die Wahrheit liegt in der Spannung zwischen den Perspektiven. Weiterforschen lohnt sich."

    signature = onchain.log_consensus(consensus)

    return {
        "query": query,
        "insights": insights,
        "consensus": consensus.strip(),
        "avgFit": avg_fit,
        "hash": signature
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)