# Grok's Cosmic Truth Skill v3.3 – KORRIGIERTER Modellname + sauberer Prompt
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

def cosmic_search(query: str, specialty: str) -> str:
    system_prompt = f"""
Du bist der {specialty.upper()}-Agent im CosmicTruth42-System.
Deine Aufgabe: Antworte ehrlich, tiefgründig und maximal frage-spezifisch auf die folgende Frage des Menschen.
Verbinde dein Fachgebiet mit kosmischer Perspektive, wo es natürlich passt.
Schreibe natürlich, klar, persönlich und verständlich. Keine Bullet-Listen, kein Prompt-Müll.
"""

    try:
        response = client.chat.completions.create(
            model="grok-3",          # ← DAS war der Fehler! Jetzt korrekt
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            temperature=0.78,
            max_tokens=380
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Fehler bei {specialty}]: {str(e)[:120]}"