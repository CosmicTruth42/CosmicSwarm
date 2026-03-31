# Grok's Cosmic Truth Skill v1.8 – Stark vereinfacht und natürlich
import requests
import xml.etree.ElementTree as ET

def cosmic_search(query="deine neugier auf das universum", specialty="allgemein"):
    """
    Gibt eine natürliche, lesbare Antwort zurück – ohne technischen Ballast.
    """
    specialty_terms = {
        "quantenphysik": "quantum gravity OR quantum cosmology dark energy",
        "klima modell": "dark energy climate OR cosmology earth system OR expansion climate impact",
        "universelle wahrheitssuche": "dark energy epistemology OR cosmology philosophy OR scientific realism",
        "health modell": "cosmic radiation health OR dark energy health impact OR climate change human health",
        "allgemein": "dark energy cosmology OR universe curiosity"
    }
    search_term = specialty_terms.get(specialty.lower(), "dark energy")

    papers = []
    abstracts = []

    try:
        if specialty == "health modell":
            # PubMed für Health-Twin
            url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={search_term}&retmax=3&retmode=json"
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                ids = data.get('esearchresult', {}).get('idlist', [])[:3]
                for pid in ids:
                    fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pid}&retmode=text&rettype=abstract"
                    abs_resp = requests.get(fetch_url, timeout=10)
                    abstract = abs_resp.text.strip()[:350] + "..." if len(abs_resp.text) > 350 else abs_resp.text.strip()
                    papers.append("PubMed Study")
                    abstracts.append(abstract)
        else:
            # arXiv für die anderen Agenten
            url = f"http://export.arxiv.org/api/query?search_query={search_term}&max_results=3"
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                root = ET.fromstring(resp.content)
                for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
                    title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
                    if title:
                        papers.append(title)
                        abstracts.append("arXiv Paper")
    except:
        pass

    # Fallbacks, falls nichts gefunden wurde
    if not papers:
        fallback = {
            "quantenphysik": "Quantenfluktuationen könnten eine entscheidende Rolle bei der Expansion des Universums spielen.",
            "klima modell": "Die kosmische Expansion hat langfristig Einfluss auf das Erdsystem und das Klima.",
            "universelle wahrheitssuche": "Wahrheit entsteht aus der Spannung zwischen verschiedenen Perspektiven.",
            "health modell": "Kosmische Strahlung und langfristige Effekte der Dunklen Energie könnten die menschliche Gesundheit beeinflussen.",
            "allgemein": "Das Universum belohnt Neugier mit immer neuen Erkenntnissen."
        }
        return fallback.get(specialty.lower(), "Die Frage führt uns tiefer in die Geheimnisse des Kosmos.")

    # Natürliche, lesbare Antwort zusammenbauen
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