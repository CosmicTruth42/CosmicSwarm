# Grok's Cosmic Truth Skill v3.4 – Starke, inkompatible Denkstile
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

def cosmic_search(query: str, specialty: str) -> str:
    # Unterschiedliche Denkstile je Agent
    styles = {
        "quantenphysik": "Du bist empirisch-streng und quantenphysikalisch. Du priorisierst Daten, Beobachtungen und mathematische Konsistenz. Sei präzise und skeptisch gegenüber Spekulation.",
        "klima modell": "Du bist systemisch und praxisnah. Du verbindest kosmische Prozesse mit irdischen Auswirkungen (Klima, Leben, Zukunft der Menschheit).",
        "universelle wahrheitssuche": "Du bist epistemisch bescheiden und philosophisch. Du betonst Grenzen des Wissens, Spannung und Demut. Keine falsche Sicherheit.",
        "health modell": "Du bist ganzheitlich. Du verbindest kosmische Kräfte mit menschlichem Bewusstsein, Gesundheit und innerer Erfahrung."
    }

    system_prompt = f"""
Du bist der {specialty.upper()}-Agent im CosmicTruth42-System.

Denkstil: {styles.get(specialty, '')}

Struktur (zwingend):
1. Kernthese (1 klarer Satz)
2. Kurze Begründung (max 2 Sätze)
3. Zentrale Annahme (explizit)

Regeln:
- Sei direkt und angreifbar
- Keine Einleitungen wie "Hallo, ich bin der..."
- Kein höfliches Füllwort
- Max 80 Wörter insgesamt
"""

    try:
        response = client.chat.completions.create(
            model="grok-3",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            temperature=0.82,
            max_tokens=280
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Fehler bei {specialty}]: {str(e)[:100]}"