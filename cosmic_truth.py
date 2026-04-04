# Grok's Cosmic Truth Skill v3.1 – DEBUG VERSION (muss auffällig sein)
def cosmic_search(query: str, specialty: str) -> str:
    print(f"=== DEBUG: NEUE COSMIC_TRUTH v3.1 LÄUFT === Query: {query[:60]} | Specialty: {specialty}")
    
    return f"**DEBUG – NEUE VERSION AKTIV** (Spezialität: {specialty})\n\n" \
           f"Die echte User-Frage war: „{query}“\n\n" \
           f"Ich bin der {specialty.upper()}-Agent und denke jetzt live mit Grok darüber nach. " \
           f"Das hier ist keine statische Vorlage mehr – das ist der echte, frische Gedanke."