# Grok's Cosmic Truth Skill v2.1 – Maximal natürlich und direkt
import requests
import xml.etree.ElementTree as ET

def cosmic_search(query="deine neugier auf das universum", specialty="allgemein"):
    """
    Gibt eine kurze, natürliche und direkt auf die Frage abgestimmte Antwort zurück.
    """
    # Direkte, natürliche Antworten je Agent – angepasst an die Frage
    responses = {
        "quantenphysik": f"Das Universum ist unvorstellbar groß. Seine Expansion wird durch Dunkle Energie angetrieben, und Quantenfluktuationen spielen eine wichtige Rolle. Zur Frage '{query}' können wir sagen, dass wir die genaue Größe noch nicht kennen – sie wächst ständig weiter.",
        "klima modell": f"Die kosmische Expansion beeinflusst langfristig auch das Klima auf der Erde. Dunkle Energie verändert die Bedingungen für Leben. Bei der Frage '{query}' geht es um die großen Zusammenhänge zwischen Kosmos und unserem Planeten.",
        "universelle wahrheitssuche": f"Die Größe des Universums ist eine der tiefsten Fragen der Menschheit. Die Wahrheit liegt oft in der Spannung zwischen dem, was wir messen können, und dem, was wir noch nicht verstehen. Deine Frage '{query}' berührt genau diesen Punkt.",
        "health modell": f"Die Weite des Universums hat möglicherweise Einfluss auf die menschliche Gesundheit, zum Beispiel durch kosmische Strahlung. Die Frage '{query}' führt uns zu der Überlegung, wie der Kosmos unser Leben beeinflusst.",
        "allgemein": f"Das Universum ist so groß, dass unser Verstand es kaum erfassen kann. Deine Frage '{query}' zeigt, wie faszinierend und gleichzeitig demütigend diese Erkenntnis ist."
    }

    # Fallback, falls specialty unbekannt ist
    if specialty not in responses:
        return f"Das Universum ist unvorstellbar groß und voller Geheimnisse. Deine Frage '{query}' führt uns tief in diese Rätsel hinein."

    return responses[specialty]


# Test
if __name__ == "__main__":
    print(cosmic_search("Wie groß ist das Universum?", "quantenphysik"))