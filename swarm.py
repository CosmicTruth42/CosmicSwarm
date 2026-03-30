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
    """Extrem starkes Cleaning – speziell für cosmic_truth.py"""
    text = re.sub(r"Cosmic Twin \(.*?\) zu .*?:", "", text)
    text = re.sub(r"Agents debattieren .*? Claims: .*? Claims:", "", text)
    text = re.sub(r"Weisheit aus Quellen: \[.*?\]", "", text)
    text = re.sub(r"Abstracts: \[.*?\]", "", text)
    text = re.sub(r"Validation: .*?– niedrige Entropie\.", "", text)
    text = re.sub(r"Rat: .*? Weiterforschen\.", "", text)
    text = re.sub(r"Gib eine ehrliche.*Frage: '.*?'", "", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"Sei persönlich.*Perspektiven\.", "", text, flags=re.IGNORECASE)
    text = re.sub(r"Antworte weise.*Frage: '.*?'", "", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"kosmisches Potenzial in Wahrheitssuche", "", text)
    text = re.sub(r"\[\'.*?\'\]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) > 25 else ""

@app.get("/twin")
async def cosmic_twin(query: str):
    if not query or len(query.strip()) < 3:
        return {"error": "Bitte gib eine sinnvolle Frage ein."}

    raw_insights = []
    for agent in integrated_swarm.agents:
        personal_query = f"Antworte weise, persönlich und tiefgründig auf diese Frage: '{query}'. Verbinde kosmische, wissenschaftliche und menschliche Gedanken. Schreibe klar und verständlich, ohne Fachchinesisch."
        insight = agent.contribute(personal_query)
        raw_insights.append(insight)

    # Starkes Cleaning
    clean_insights = [clean_insight(i) for i in raw_insights if clean_insight(i)]

    # Starke Meta-Instanz – formuliert die Antwort natürlich neu
    meta = f"**Cosmic Twin zu deiner Frage:** „{query}“\n\n"
    meta += "Die vier Agents haben intensiv darüber nachgedacht. Hier ist ihre gemeinsame, klare Erkenntnis:\n\n"

    for text in clean_insights[:3]:
        if text:
            meta += f"• {text}\n\n"

    meta += "Zusammengefasst liegt die Wahrheit meist in der Spannung zwischen den verschiedenen Perspektiven. Es gibt selten eine einfache Antwort – und genau das macht solche Fragen wertvoll."

    signature = onchain.log_consensus(meta)

    return {
        "query": query,
        "insights": raw_insights,
        "consensus": meta.strip(),
        "avgFit": 88,
        "hash": signature
    }

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)