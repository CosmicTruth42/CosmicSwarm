from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solders.transaction import Transaction
from solders.message import Message
from solders.system_program import TransferParams, transfer
from solana.rpc.api import Client
from solana.rpc.commitment import Confirmed
import hashlib
import base58

WALLET_PUBKEY = "F5wrH3SCFjpH6E9fmfJxrKHMzaywYBNubqG2ubwSPCey"
client = Client("https://api.devnet.solana.com")

def log_consensus(consensus_text, fit_score):
    try:
        keypair = Keypair.from_base58_string("2CSe7uUVE5WmTx1xUa1WjiW3syu5mk9W2anMAep3BRDvr6xwJdWobXDuuye1k64bqCm5i8qa13yEg2PEFBjgfp3w")   # ← Dein Key!
        
        recent_blockhash = client.get_latest_blockhash(Confirmed).value.blockhash
        
        ix = transfer(TransferParams(
            from_pubkey=keypair.pubkey(),
            to_pubkey=Pubkey.from_string(WALLET_PUBKEY),
            lamports=100000
        ))
        
        message = Message.new_with_blockhash([ix], keypair.pubkey(), recent_blockhash)
        tx = Transaction.new_unsigned(message)
        signed_tx = tx.sign([keypair], recent_blockhash)
        
        # Senden
        sig = client.send_transaction(signed_tx, keypair)
        
        print("\n" + "="*60)
        print("✅ ERFOLG! Erster On-Chain-Log von CosmicTruth42!")
        print("="*60)
        print(f"Konsens : {consensus_text}")
        print(f"Fit     : {fit_score}%")
        print(f"TX      : {sig.value}")
        print(f"Explorer: https://explorer.solana.com/tx/{sig.value}?cluster=devnet")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Fehler: {e}")

if __name__ == "__main__":
    log_consensus("Starke Evidenz für evolvierende Dark Energy (basierend auf Kollision)", 90)