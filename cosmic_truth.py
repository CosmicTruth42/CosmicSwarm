# Grok's Cosmic Truth Skill v2.4 – Noch direkter und frage-spezifisch
def cosmic_search(query="deine neugier auf das universum", specialty="allgemein"):
    """
    Gibt eine kurze, natürliche und direkt auf die Frage abgestimmte Antwort zurück.
    """
    responses = {
        "quantenphysik": f"Das Universum ist unvorstellbar groß und expandiert ständig. Dunkle Energie und Quantenfluktuationen spielen dabei eine wichtige Rolle. Deine Frage '{query}' führt uns direkt zu der Erkenntnis, dass wir die genaue Größe noch nicht kennen – sie wächst weiter.",
        "klima modell": f"Die kosmische Expansion beeinflusst langfristig auch das Klima auf der Erde. Dunkle Energie verändert die Bedingungen für Leben. Deine Frage '{query}' zeigt, wie stark Kosmos und unser Planet miteinander verbunden sind.",
        "universelle wahrheitssuche": f"Die Größe des Universums ist eine der tiefsten Fragen der Menschheit. Die Wahrheit liegt oft in der Spannung zwischen dem Bekannten und dem Unbekannten. Deine Frage '{query}' berührt genau diesen Punkt.",
        "health modell": f"Die Weite des Universums hat möglicherweise Einfluss auf die menschliche Gesundheit, zum Beispiel durch kosmische Strahlung. Deine Frage '{query}' lässt uns darüber nachdenken, wie der Kosmos unser Leben beeinflusst.",
        "allgemein": f"Das Universum ist so groß, dass unser Verstand es kaum erfassen kann. Deine Frage '{query}' zeigt, wie faszinierend und gleichzeitig demütigend diese Erkenntnis ist."
    }

    # Fallback
    if specialty not in responses:
        return f"Das Universum ist unvorstellbar groß und voller Geheimnisse. Deine Frage '{query}' führt uns tief in diese Rätsel hinein."

    return responses[specialty]