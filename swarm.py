from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import integrated_swarm
import re
from onchain_logger import onchain  # <-- echtes Logging wird hier eingebunden

app = FastAPI(title="CosmicTruth42 Backend")

# CORS – erlaubt Zugriff vom Vercel-Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://cosmicswarm.vercel.app",
        "https://*.vercel.app",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "*"
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
    
    # === ECHTES ON-CHAIN LOGGING ===
    signature = onchain.log_consensus(consensus)
    
    return {
        "topic": topic,
        "insights": insights,
        "consensus": consensus,
        "avgFit": avg_fit,
        "hash": signature   # <-- jetzt echter Solana-Hash statt Test-Hash
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)