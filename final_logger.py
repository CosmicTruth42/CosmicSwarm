from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solders.system_program import transfer, TransferParams
from solders.transaction import VersionedTransaction
from solders.message import Message
from solana.rpc.api import Client
from solana.rpc.commitment import Confirmed

print("🚀 Finaler Versuch – CosmicTruth42 Live Log")

# Dein Key
keypair = Keypair.from_base58_string("2CSe7uUVE5WmTx1xUa1WjiW3syu5mk9W2anMAep3BRDvr6xwJdWobXDuuye1k64bqCm5i8qa13yEg2PEFBjgfp3w")

client = Client("https://api.devnet.solana.com")
wallet = Pubkey.from_string("F5wrH3SCFjpH6E9fmfJxrKHMzaywYBNubqG2ubwSPCey")

try:
    # Blockhash ganz frisch holen (direkt vor dem Senden)
    recent_blockhash = client.get_latest_blockhash(Confirmed).value.blockhash
    print("✅ Frischer Blockhash geholt")

    ix = transfer(TransferParams(
        from_pubkey=keypair.pubkey(),
        to_pubkey=wallet,
        lamports=100000
    ))

    message = Message.new_with_blockhash([ix], keypair.pubkey(), recent_blockhash)
    tx = VersionedTransaction(message, [keypair])

    sig = client.send_transaction(tx)

    print("\n" + "="*70)
    print("🎉 ERFOLG! Erster On-Chain-Log von CosmicTruth42!")
    print("="*70)
    print(f"TX Signature: {sig.value}")
    print(f"Explorer: https://explorer.solana.com/tx/{sig.value}?cluster=devnet")
    print("="*70)

except Exception as e:
    print("❌ Fehler:")
    print(e)