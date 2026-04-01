# Grok's Cosmic Truth Skill v2.2 – Maximal natürlich und direkt
def cosmic_search(query="deine neugier auf das universum", specialty="allgemein"):
    """
    Gibt eine kurze, natürliche Antwort zurück – ohne technischen Ballast.
    """
    responses = {
        "quantenphysik": "Das Universum ist unvorstellbar groß. Seine Expansion wird durch Dunkle Energie angetrieben, und Quantenfluktuationen spielen dabei eine wichtige Rolle.",
        "klima modell": "Die kosmische Expansion beeinflusst langfristig auch das Klima auf der Erde. Dunkle Energie verändert die Bedingungen für Leben auf unserem Planeten.",
        "universelle wahrheitssuche": "Die Größe des Universums ist eine der tiefsten Fragen der Menschheit. Die Wahrheit liegt oft in der Spannung zwischen dem Bekannten und dem Unbekannten.",
        "health modell": "Die Weite des Universums hat möglicherweise Einfluss auf die menschliche Gesundheit, zum Beispiel durch kosmische Strahlung.",
        "allgemein": "Das Universum ist so groß, dass unser Verstand es kaum erfassen kann. Es bleibt ein großes Rätsel, das uns immer wieder zum Staunen bringt."
    }

    # Fallback
    if specialty not in responses:
        return "Das Universum ist unvorstellbar groß und voller Geheimnisse."

    return responses[specialty]