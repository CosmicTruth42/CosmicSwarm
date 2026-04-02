# Grok's Cosmic Truth Skill v2.4 – Extrem sauber und kurz
def cosmic_search(query="deine neugier auf das universum", specialty="allgemein"):
    """
    Gibt nur kurze, natürliche Sätze zurück – ohne jeglichen Prompt-Müll.
    """
    responses = {
        "quantenphysik": "Das Universum ist unvorstellbar groß. Es expandiert ständig durch Dunkle Energie, und Quantenfluktuationen spielen eine wichtige Rolle.",
        "klima modell": "Die kosmische Expansion beeinflusst langfristig auch das Klima auf der Erde. Dunkle Energie verändert die Bedingungen für Leben.",
        "universelle wahrheitssuche": "Die Größe des Universums ist eine der tiefsten Fragen der Menschheit. Die Wahrheit liegt in der Spannung zwischen Bekanntem und Unbekanntem.",
        "health modell": "Die Weite des Universums hat möglicherweise Einfluss auf die menschliche Gesundheit, zum Beispiel durch kosmische Strahlung.",
        "allgemein": "Das Universum ist so groß, dass unser Verstand es kaum erfassen kann."
    }

    if specialty not in responses:
        return "Das Universum ist unvorstellbar groß und voller Geheimnisse."

    return responses[specialty]