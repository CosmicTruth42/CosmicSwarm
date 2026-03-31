# Grok's Cosmic Truth Skill v1.9 – Stark vereinfacht und natürlich
import requests
import xml.etree.ElementTree as ET

def cosmic_search(query="deine neugier auf das universum", specialty="allgemein"):
    """
    Gibt eine natürliche, lesbare Antwort zurück – ohne technischen Müll.
    """
    # Spezifische Suchbegriffe
    search_terms = {
        "quantenphysik": "quantum gravity dark energy OR quantum cosmology",
        "klima modell": "dark energy climate impact OR cosmic expansion earth system",
        "universelle wahrheitssuche": "dark energy philosophy OR cosmology epistemology",
        "health modell": "cosmic radiation human health OR dark energy health effects",
        "allgemein": "dark energy universe size OR cosmic scale"
    }

    search_term = search_terms.get(specialty.lower(), "dark energy cosmology")

    papers = []
    abstracts = []

    try:
        # arXiv für die meisten Agenten
        url = f"http://export.arxiv.org/api/query?search_query={search_term}&max_results=3"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            root = ET.fromstring(resp.content)
            for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
                title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
                if title and len(title) > 15:
                    papers.append(title)
                    abstracts.append("arXiv Paper")
    except:
        pass

    # Natürliche Antwort zusammenbauen
    if not papers:
        fallback = {
            "quantenphysik": "Das Universum ist unvorstellbar groß – seine genaue Größe hängt von der Expansion und der Dunklen Energie ab.",
            "klima modell": "Die kosmische Expansion beeinflusst langfristig auch das Klima auf der Erde.",
            "universelle wahrheitssuche": "Die Größe des Universums ist eine der tiefsten Fragen der Menschheit.",
            "health modell": "Die Weite des Universums hat möglicherweise Einfluss auf die menschliche Gesundheit durch kosmische Strahlung.",
            "allgemein": "Das Universum ist so groß, dass unser Verstand es kaum erfassen kann."
        }
        return fallback.get(specialty.lower(), "Die Frage führt uns tief in die Geheimnisse des Kosmos.")

    response = f"Die Agents haben sich mit der Frage '{query}' beschäftigt.\n\n"
    for i, paper in enumerate(papers[:3]):
        response += f"• {paper}\n"
        if i < len(abstracts):
            response += f"  {abstracts[i]}\n\n"

    response += "Zusammengefasst liegt die Wahrheit in der Spannung zwischen den verschiedenen Perspektiven."

    return response.strip()


# Test
if __name__ == "__main__":
    print(cosmic_search("Wie groß ist das Universum?", "quantenphysik"))