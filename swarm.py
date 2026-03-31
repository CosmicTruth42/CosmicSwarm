@app.get("/twin")
async def cosmic_twin(query: str):
    if not query or len(query.strip()) < 3:
        return {"error": "Bitte gib eine sinnvolle Frage ein."}

    raw_insights = []
    for agent in integrated_swarm.agents:
        personal_query = f"Antworte weise, persönlich und tiefgründig auf diese Frage: '{query}'. Verbinde kosmische, wissenschaftliche und menschliche Gedanken. Schreibe klar und verständlich."
        insight = agent.contribute(personal_query)
        raw_insights.append(insight)

    clean_insights = [clean_insight(i) for i in raw_insights if clean_insight(i)]

    meta = f"**Cosmic Twin zu deiner Frage:** „{query}“\n\n"
    meta += "Die vier Agents haben intensiv darüber nachgedacht. Hier ist ihre gemeinsame, klare Erkenntnis:\n\n"
    
    for text in clean_insights[:3]:
        if text:
            meta += f"• {text}\n\n"
    
    meta += "Zusammengefasst liegt die Wahrheit meist in der Spannung zwischen den verschiedenen Perspektiven. "
    meta += "Es gibt selten eine einfache Antwort – und genau das macht solche Fragen wertvoll."

    signature = onchain.log_consensus(meta)

    return {
        "query": query,
        "insights": raw_insights,      # ← wichtig für Dashboard (verhindert den Crash)
        "consensus": meta.strip(),
        "avgFit": 88,
        "hash": signature
    }