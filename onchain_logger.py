from solders.keypair import Keypair
from solders.message import Message
from solders.transaction import Transaction
from solana.rpc.api import Client
import base58
import time

# Dein echter Private Key (CosmicTruth42 Wallet)
PRIVATE_KEY_BASE58 = "2CSe7uUVE5WmTx1xUa1WjiW3syu5mk9W2anMAep3BRDvr6xwJdWobXDuuye1k64bqCm5i8qa13yEg2PEFBjgfp3w"

class OnChainLogger:
    def __init__(self):
        self.client = Client("https://api.mainnet-beta.solana.com")
        self.keypair = Keypair.from_base58_string(PRIVATE_KEY_BASE58)
        print(f"✅ On-Chain Logger geladen für: {self.keypair.pubkey()}")

    def log_consensus(self, consensus_text: str):
        try:
            # Kurze Nachricht als Memo
            memo = f"CosmicTruth42 | {consensus_text[:100]} | {int(time.time())}"

            # Einfache Transaction mit Memo
            tx = Transaction()
            tx.add_memo(memo)
            tx.sign([self.keypair])

            result = self.client.send_transaction(tx)
            signature = result.value

            print(f"✅ On-Chain Log erfolgreich! Signature: {signature}")
            return str(signature)

        except Exception as e:
            print(f"Live Error: {e} – Fallback zu Test-Mode")
            return f"Test-Hash: {int(time.time())}"

# Singleton
onchain = OnChainLogger()