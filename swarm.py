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

def clean_insight(text: str) -> str:
    """Entfernt technische Artefakte und macht den Text lesbar"""
    # Entferne arXiv-Platzhalter, Abstracts-Listen etc.
    text = re.sub(r'\[\'arXiv Paper.*?\']', '', text)
    text = re.sub(r'Abstracts: \[.*?\]', '', text)
    text = re.sub(r'Validation: .*?– niedrige Entropie\.', '', text)
    text = re.sub(r'Cosmic Twin \(.*?\) zu .*?:', '', text)
    return text.strip()

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
    """Cosmic Twin – jetzt wirklich dynamisch und natürlich"""
    if not query or len(query.strip()) < 3:
        return {"error": "Bitte gib eine sinnvolle Frage ein."}

    insights = []
    fits = []

    for agent in integrated_swarm.agents:
        personal_query = (
            f"Gib eine ehrliche, weise und tiefgründige Antwort auf diese konkrete Frage des Menschen: "
            f"'{query}'. Sei persönlich, nuanciert, vermeide Floskeln und verbinde kosmische, wissenschaftliche "
            f"und menschliche Perspektiven. Schreibe klar und verständlich."
        )
        insight = agent.contribute(personal_query)
        insights.append(insight)
        
        fit_match = re.search(r'(\d+)%\s*Fit', insight)
        if fit_match:
            fits.append(float(fit_match.group(1)))

    avg_fit = round(sum(fits) / len(fits)) if fits else 88

    # Saubere, natürliche Synthese
    clean_insights = [clean_insight(i) for i in insights if clean_insight(i)]
    
    consensus = f"**Cosmic Twin zu deiner Frage:**\n\n„{query}“\n\n"
    consensus += "Die vier Agents haben intensiv darüber nachgedacht. Hier ist die gemeinsame Erkenntnis:\n\n"
    
    for i, text in enumerate(clean_insights[:4], 1):
        if text:
            consensus += f"• {text}\n\n"
    
    consensus += "Zusammengefasst liegt die Wahrheit in der Spannung zwischen den Perspektiven. "
    consensus += "Es gibt keine einfache Antwort – aber genau das macht die Frage so wertvoll."

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