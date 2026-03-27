from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import integrated_swarm
import re
from onchain_logger import onchain

app = FastAPI(title="CosmicTruth42 Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://cosmicswarm.vercel.app", "https://*.vercel.app", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/swarm")
async def get_swarm():
    # ... (alter Code bleibt unverändert)
    topic = "ist dark energy konstant?"
    # ... (alles wie bisher)
    return { ... }

@app.get("/twin")
async def cosmic_twin(query: str):
    """Cosmic Twin – persönlicher Agent für deine Frage"""
    insights = []
    fits = []

    for agent in integrated_swarm.agents:
        insight = agent.contribute(query)   # Hier kommt deine persönliche Frage rein
        insights.append(insight)
        
        fit_match = re.search(r'(\d+)%\s*Fit', insight)
        if fit_match:
            fits.append(float(fit_match.group(1)))

    avg_fit = round(sum(fits) / len(fits)) if fits else 90
    consensus = "Starke Evidenz für evolvierende Dark Energy (basierend auf Kollision)" if avg_fit > 87 else "Weiterforschen, Tension bleibt"

    signature = onchain.log_consensus(consensus)   # On-Chain bleibt vorerst Test-Hash

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