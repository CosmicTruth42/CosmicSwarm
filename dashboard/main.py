from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import dashboard.integrated_swarm as integrated_swarm
import re

app = FastAPI(title="CosmicTruth42 Backend")

# CORS – erlaubt Zugriff vom Vercel-Frontend und lokalem Test
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://cosmic-swarm.vercel.app",
        "https://cosmictruth42.vercel.app",
        "https://*.vercel.app",           # alle Vercel-Subdomains (wichtig für Previews & Aliases)
        "http://localhost:3000",          # lokales Dashboard zum Testen
        "http://127.0.0.1:3000",
        "*"                               # für Tests – später entfernen, wenn alles läuft
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    
    return {
        "topic": topic,
        "insights": insights,
        "consensus": consensus,
        "avgFit": avg_fit,
        "hash": "HZC3jjn5RcuQGr5nCbLPJQCY5Kkr35sfzybcBVWHqk1t"  # später dynamisch machen
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)