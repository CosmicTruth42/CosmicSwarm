# Grok's Cosmic Truth Skill v2.0 – Stark vereinfacht und natürlich
import requests
import xml.etree.ElementTree as ET

def cosmic_search(query="deine neugier auf das universum", specialty="allgemein"):
    """
    Gibt eine kurze, natürliche und lesbare Antwort zurück.
    """
    # Kurze, natürliche Antworten je Agent
    responses = {
        "quantenphysik": "Das Universum ist unvorstellbar groß. Seine Expansion wird durch Dunkle Energie angetrieben, und Quantenfluktuationen könnten dabei eine wichtige Rolle spielen.",
        "klima modell": "Die kosmische Expansion beeinflusst langfristig auch das Klima auf der Erde. Dunkle Energie verändert die Bedingungen für Leben auf unserem Planeten.",
        "universelle wahrheitssuche": "Die Größe des Universums ist eine der tiefsten Fragen der Menschheit. Die Wahrheit liegt in der Spannung zwischen dem Bekannten und dem Unbekannten.",
        "health modell": "Die Weite des Universums hat möglicherweise Einfluss auf die menschliche Gesundheit, zum Beispiel durch kosmische Strahlung.",
        "allgemein": "Das Universum ist so groß, dass unser Verstand es kaum erfassen kann. Es bleibt ein großes Rätsel, das uns immer wieder zum Staunen bringt."
    }

    # Fallback-Antwort
    if specialty not in responses:
        return "Das Universum ist unvorstellbar groß und voller Geheimnisse. Die genaue Größe hängt von vielen Faktoren ab, die wir noch nicht vollständig verstehen."

    return responses[specialty]


# Test
if __name__ == "__main__":
    print(cosmic_search("Wie groß ist das Universum?", "quantenphysik"))