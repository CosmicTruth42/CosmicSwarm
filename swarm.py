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
    """Cosmic Twin – persönlicher, reflektierter Agent mit Meta-Instanz"""
    if not query or len(query.strip()) < 5:
        return {"error": "Bitte gib eine sinnvolle Frage ein."}

    insights = []
    fits = []
    raw_insights = []

    for agent in integrated_swarm.agents:
        personal_query = f"Persönliche, tiefe und ehrliche Reflexion zu dieser Frage: {query}. Wie beeinflusst das die Wahrheitssuche, die Zukunft des Menschen und die kosmische Perspektive? Sei nuanciert, mutig und weise."
        insight = agent.contribute(personal_query)
        insights.append(insight)
        raw_insights.append(insight)
        
        fit_match = re.search(r'(\d+)%\s*Fit', insight)
        if fit_match:
            fits.append(float(fit_match.group(1)))

    avg_fit = round(sum(fits) / len(fits)) if fits else 90

    # Einfache Meta-Instanz (dynamischer Schwellenwert)
    variance = max(fits) - min(fits) if fits else 0
    threshold = 85 if variance < 15 else 78   # dynamisch: bei hoher Varianz niedrigerer Schwellenwert

    if avg_fit >= threshold and variance < 25:
        consensus = f"Cosmic Twin zu deiner Frage '{query}': Die Agents sehen ein hohes Potenzial, dass KI eine transformative Rolle spielt – sie kann Wahrheit verstärken, aber auch verzerren. Die entscheidende Frage ist, ob wir weise genug sind, sie zu führen."
    else:
        consensus = f"Non-Consensus zu deiner Frage '{query}'. Die Agents sind uneins. Kernkonflikt liegt in der Spannung zwischen Erkenntnispotenzial und systemischem Risiko. Nächste Forschungsfrage: Unter welchen Bedingungen kann KI die positiven Potenziale maximieren und die Risiken minimieren?"

    signature = onchain.log_consensus(consensus)

    return {
        "query": query,
        "insights": raw_insights,
        "consensus": consensus,
        "avgFit": avg_fit,
        "hash": signature
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)