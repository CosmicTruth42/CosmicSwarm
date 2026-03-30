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
    """Extrem aggressives Cleaning – entfernt alles Technische und Prompt-Müll"""
    # Entferne den gesamten Prompt-Echo
    text = re.sub(r"Gib eine ehrliche.*Frage des Menschen: '.*?'", "", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"Sei persönlich.*Perspektiven\.", "", text, flags=re.IGNORECASE)
    
    # Entferne alle Agenten-Interna
    text = re.sub(r"Agents debattieren .*? Claims: .*? Claims:", "", text)
    text = re.sub(r"Weisheit aus Quellen: \[.*?\]", "", text)
    text = re.sub(r"Abstracts: \[.*?\]", "", text)
    text = re.sub(r"Validation: .*?– niedrige Entropie\.", "", text)
    text = re.sub(r"Rat: .*? Weiterforschen\.", "", text)
    text = re.sub(r"Cosmic Twin \(.*?\) zu .*?:", "", text)
    
    # Entferne alles, was wie Code/Metadaten aussieht
    text = re.sub(r"\[\'.*?\'\]", "", text)
    text = re.sub(r"Potenzial ≈ .*? Fit", "", text)
    text = re.sub(r"Claims: .*?% sehen", "", text)
    
    # Saubere Leerzeichen
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) > 15 else ""

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
    """Cosmic Twin – jetzt wirklich sauber und natürlich"""
    if not query or len(query.strip()) < 3:
        return {"error": "Bitte gib eine sinnvolle Frage ein."}

    insights = []
    fits = []

    for agent in integrated_swarm.agents:
        # Kurzer, klarer Prompt an die Agents
        personal_query = f"Antworte ehrlich und tiefgründig auf diese Frage: '{query}'. Verbinde kosmische, wissenschaftliche und menschliche Perspektiven. Schreibe klar und verständlich."
        insight = agent.contribute(personal_query)
        insights.append(insight)
        
        fit_match = re.search(r'(\d+)%\s*Fit', insight)
        if fit_match:
            fits.append(float(fit_match.group(1)))

    avg_fit = round(sum(fits) / len(fits)) if fits else 88

    # Sehr starkes Cleaning
    clean_insights = [clean_insight(i) for i in insights if clean_insight(i)]

    # Natürliche, lesbare Synthese
    consensus = f"**Cosmic Twin zu deiner Frage:** „{query}“\n\n"
    consensus += "Die vier Agents haben intensiv darüber nachgedacht. Ihre gemeinsame Erkenntnis lautet:\n\n"
    
    for text in clean_insights[:3]:
        if text and len(text) > 20:
            consensus += f"• {text}\n\n"
    
    consensus += "Zusammengefasst liegt die Wahrheit in der Spannung zwischen den verschiedenen Perspektiven. "
    consensus += "Es gibt keine einfache, endgültige Antwort – aber genau das macht die Frage so wertvoll."

    signature = onchain.log_consensus(consensus)

    return {
        "query": query,
        "insights": insights,           # nur für Debugging
        "consensus": consensus.strip(),
        "avgFit": avg_fit,
        "hash": signature
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)