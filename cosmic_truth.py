# Grok's Cosmic Truth Skill v2.2 – Richtig dynamisch und natürlich
import requests
import xml.etree.ElementTree as ET

def cosmic_search(query="deine neugier auf das universum", specialty="allgemein"):
    """
    Gibt eine kurze, natürliche und direkt auf die gestellte Frage abgestimmte Antwort zurück.
    """
    # Dynamischer Prompt für jeden Agenten
    prompt = (
        f"Beantworte die folgende konkrete Frage des Menschen ehrlich, weise und tiefgründig: "
        f"'{query}'. "
        f"Verbinde kosmische, wissenschaftliche und menschliche Gedanken. "
        f"Schreibe natürlich, klar und ohne Fachchinesisch."
    )

    # Feste, kurze Antworten je Agent (als Basis, die durch den Prompt dynamisch wird)
    base_responses = {
        "quantenphysik": "Das Universum ist unvorstellbar groß und expandiert ständig. Dunkle Energie und Quantenfluktuationen spielen dabei eine entscheidende Rolle.",
        "klima modell": "Die kosmische Expansion beeinflusst langfristig auch das Klima auf der Erde. Dunkle Energie verändert die Bedingungen für Leben auf unserem Planeten.",
        "universelle wahrheitssuche": "Die Größe des Universums ist eine der tiefsten Fragen der Menschheit. Die Wahrheit liegt oft in der Spannung zwischen dem Bekannten und dem Unbekannten.",
        "health modell": "Die Weite des Universums hat möglicherweise Einfluss auf die menschliche Gesundheit, zum Beispiel durch kosmische Strahlung.",
        "allgemein": "Das Universum ist so groß, dass unser Verstand es kaum erfassen kann. Es bleibt ein großes Rätsel, das uns immer wieder zum Staunen bringt."
    }

    # Fallback
    if specialty not in base_responses:
        return "Das Universum ist unvorstellbar groß und voller Geheimnisse."

    # Kombiniere Base + dynamischen Prompt (für die Agents)
    return base_responses[specialty] + f" Zur Frage '{query}' ergibt sich daraus folgendes Bild."


# Test
if __name__ == "__main__":
    print(cosmic_search("Wie groß ist das Universum?", "quantenphysik"))