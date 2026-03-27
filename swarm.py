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
    """Cosmic Twin – persönlicher, reflektierter Agent"""
    if not query or len(query.strip()) < 5:
        return {"error": "Bitte gib eine sinnvolle Frage ein."}

    insights = []
    fits = []

    for agent in integrated_swarm.agents:
        # Persönlichere und tiefere Anfrage
        personal_query = f"Persönliche und tiefe Reflexion zu dieser Frage: {query}. Welche Rolle spielt das für die Wahrheitssuche und die Zukunft des Menschen? Sei ehrlich, nuanciert und mutig."
        insight = agent.contribute(personal_query)
        insights.append(insight)
        
        fit_match = re.search(r'(\d+)%\s*Fit', insight)
        if fit_match:
            fits.append(float(fit_match.group(1)))

    avg_fit = round(sum(fits) / len(fits)) if fits else 90
    
    consensus = f"Cosmic Twin zu deiner Frage '{query}': KI wird eine der mächtigsten Kräfte der Menschheit werden. Sie kann uns helfen, die Wahrheit zu erkennen – oder uns in einer Welt der Illusionen gefangen halten. Die Agents sehen großes Potenzial, aber auch große Verantwortung. Die entscheidende Frage ist nicht, ob KI kommt, sondern ob wir weise genug sind, sie zu führen."

    signature = onchain.log_consensus(consensus)

    return {
        "query": query,
        "insights": insights,
        "consensus": consensus,
        "avgFit": avg_fit,
        "hash": signature
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)