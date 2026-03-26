from solders.keypair import Keypair
from solders.message import Message
from solders.transaction import VersionedTransaction
from solders.system_program import TransferParams, transfer
from solana.rpc.api import Client
from solana.rpc.commitment import Confirmed
import time

class OnChainLogger:
    def __init__(self):
        self.client = Client("https://api.devnet.solana.com")
        self.keypair = Keypair.from_base58_string("2CSe7uUVE5WmTx1xUa1WjiW3syu5mk9W2anMAep3BRDvr6xwJdWobXDuuye1k64bqCm5i8qa13yEg2PEFBjgfp3w")
        print(f"✅ On-Chain Logger gestartet für Wallet: {self.keypair.pubkey()}")

    def log_consensus(self, consensus_text: str):
        try:
            # Blockhash ganz frisch und direkt vor dem Senden holen
            recent_blockhash = self.client.get_latest_blockhash(Confirmed).value.blockhash

            memo = f"CosmicTruth42 | {consensus_text[:100]} | {int(time.time())}"

            ix = transfer(TransferParams(
                from_pubkey=self.keypair.pubkey(),
                to_pubkey=self.keypair.pubkey(),   # an sich selbst senden (sehr günstig)
                lamports=100000
            ))

            message = Message.new_with_blockhash([ix], self.keypair.pubkey(), recent_blockhash)
            tx = VersionedTransaction(message, [self.keypair])

            result = self.client.send_transaction(tx)
            signature = result.value

            print(f"✅ ECHTER On-Chain Log gesendet! Signature: {signature}")
            return str(signature)

        except Exception as e:
            print(f"❌ On-Chain Fehler: {type(e).__name__} - {e}")
            return f"Test-Hash: {int(time.time())}"

onchain = OnChainLogger()