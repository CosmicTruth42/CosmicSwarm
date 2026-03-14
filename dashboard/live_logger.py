from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solders.system_program import TransferParams, transfer
from solders.transaction import Transaction
from solders.message import Message
from solana.rpc.api import Client
from solana.rpc.commitment import Confirmed

print("🚀 Starte finalen Live-Test...")

# Dein Key
keypair = Keypair.from_base58_string("2CSe7uUVE5WmTx1xUa1WjiW3syu5mk9W2anMAep3BRDvr6xwJdWobXDuuye1k64bqCm5i8qa13yEg2PEFBjgfp3w")   # ← Hier deinen Key

client = Client("https://api.devnet.solana.com")
wallet = Pubkey.from_string("F5wrH3SCFjpH6E9fmfJxrKHMzaywYBNubqG2ubwSPCey")

# Blockhash holen
blockhash = client.get_latest_blockhash(Confirmed).value.blockhash

# Transaction bauen
ix = transfer(TransferParams(
    from_pubkey=keypair.pubkey(),
    to_pubkey=wallet,
    lamports=100000
))

message = Message.new_with_blockhash([ix], keypair.pubkey(), blockhash)
tx = Transaction.new_unsigned(message)
signed_tx = tx.sign([keypair], blockhash)

# Senden
sig = client.send_transaction(signed_tx, keypair)

print("\n🎉 ERFOLG!")
print(f"TX: {sig.value}")
print(f"Explorer: https://explorer.solana.com/tx/{sig.value}?cluster=devnet")