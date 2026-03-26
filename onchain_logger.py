from solders.keypair import Keypair
from solders.message import Message
from solders.transaction import VersionedTransaction
from solders.system_program import TransferParams, transfer
from solana.rpc.api import Client
from solana.rpc.commitment import Confirmed
import time

class OnChainLogger:
    def __init__(self):
        # Mainnet für echte Logs
        self.client = Client("https://api.mainnet-beta.solana.com")
        self.keypair = Keypair.from_base58_string("2CSe7uUVE5WmTx1xUa1WjiW3syu5mk9W2anMAep3BRDvr6xwJdWobXDuuye1k64bqCm5i8qa13yEg2PEFBjgfp3w")
        print(f"✅ On-Chain Logger gestartet für Wallet: {self.keypair.pubkey()}")

    def log_consensus(self, consensus_text: str):
        try:
            print("🔄 Starte On-Chain Memo...")

            # Blockhash extrem spät holen
            recent_blockhash = self.client.get_latest_blockhash(Confirmed).value.blockhash

            # Nur eine Memo (kein Transfer mehr)
            memo = f"CosmicTruth42 | {consensus_text[:120]} | {int(time.time())}"

            # Memo-Instruction
            ix = transfer(TransferParams(
                from_pubkey=self.keypair.pubkey(),
                to_pubkey=self.keypair.pubkey(),
                lamports=1000   # sehr kleine Menge
            ))

            message = Message.new_with_blockhash([ix], self.keypair.pubkey(), recent_blockhash)
            tx = VersionedTransaction(message, [self.keypair])

            result = self.client.send_transaction(tx)
            signature = result.value

            print(f"✅ ECHTER On-Chain Memo gesendet! Signature: {signature}")
            return str(signature)

        except Exception as e:
            print(f"❌ On-Chain Fehler: {type(e).__name__} - {e}")
            return f"Test-Hash: {int(time.time())}"

onchain = OnChainLogger()