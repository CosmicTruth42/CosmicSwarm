# onchain_logger.py – On-Chain Logging vorübergehend deaktiviert (solders entfernt)

def log_consensus(consensus_text):
    # Nur Test-Modus – kein solders mehr
    print(f"Test-Mode: {consensus_text}")
    return "Test-Hash: offline"

# Falls andere Dateien das importieren, funktioniert es jetzt