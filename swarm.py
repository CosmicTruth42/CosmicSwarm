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

def clean_and_summarize(raw_insights):
    """Meta-Instanz: Putzt + formuliert natürlich neu"""
    clean_texts = []
    for text in raw_insights:
        # Alles Technische brutal entfernen
        text = re.sub(r"Cosmic Twin \(.*?\) zu .*?:", "", text)
        text = re.sub(r"Agents debattieren .*? Claims: .*? Claims:", "", text)
        text = re.sub(r"Weisheit aus Quellen: \[.*?\]", "", text)
        text = re.sub(r"Abstracts: \[.*?\]", "", text)
        text = re.sub(r"Validation: .*?– niedrige Entropie\.", "", text)
        text = re.sub(r"Rat: .*? Weiterforschen\.", "", text)
        text = re.sub(r"Gib eine ehrliche.*Frage: '.*?'", "", text, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(r"Sei persönlich.*Perspektiven\.", "", text, flags=re.IGNORECASE)
        text = re.sub(r"Antworte weise.*Frage: '.*?'", "", text, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(r"\[\'.*?\'\]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        
        if len(text) > 25:
            clean_texts.append(text)
    
    # Meta-Synthese: Natürliche Zusammenfassung
    if not clean_texts:
        return "Die Agents haben intensiv nachgedacht, konnten aber noch keine klare Antwort finden."
    
    summary = "Die vier Agents haben intensiv darüber nachgedacht. Ihre gemeinsame Erkenntnis lautet:\n\n"
    for text in clean_texts[:3]:
        summary += f"• {text}\n\n"
    
    summary += "Zusammengefasst liegt die Wahrheit meist in der Spannung zwischen den verschiedenen Perspektiven. "
    summary += "Es gibt selten eine einfache Antwort – und genau das macht solche Fragen wertvoll."
    
    return summary

@app.get("/twin")
async def cosmic_twin(query: str):
    if not query or len(query.strip()) < 3:
        return {"error": "Bitte gib eine sinnvolle Frage ein."}

    raw_insights = []
    for agent in integrated_swarm.agents:
        personal_query = f"Antworte weise, persönlich und tiefgründig auf diese Frage: '{query}'. Verbinde kosmische, wissenschaftliche und menschliche Gedanken. Schreibe klar und verständlich."
        insight = agent.contribute(personal_query)
        raw_insights.append(insight)

    final_answer = clean_and_summarize(raw_insights)

    signature = onchain.log_consensus(final_answer)

    return {
        "query": query,
        "consensus": final_answer,
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