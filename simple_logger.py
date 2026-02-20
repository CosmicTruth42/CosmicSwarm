from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solders.transaction import Transaction
from solders.message import Message
from solders.system_program import TransferParams, transfer
from solana.rpc.api import Client
from solana.rpc.commitment import Confirmed

WALLET_PUBKEY = "F5wrH3SCFjpH6E9fmfJxrKHMzaywYBNubqG2ubwSPCey"

print("🔄 Starte minimalen Live-Test...")

try:
    # ← HIER DEINEN KEY EINFÜGEN
    keypair = Keypair.from_base58_string("2CSe7uUVE5WmTx1xUa1WjiW3syu5mk9W2anMAep3BRDvr6xwJdWobXDuuye1k64bqCm5i8qa13yEg2PEFBjgfp3w")

    client = Client("https://api.devnet.solana.com")
    recent_blockhash = client.get_latest_blockhash(Confirmed).value.blockhash

    ix = transfer(TransferParams(
        from_pubkey=keypair.pubkey(),
        to_pubkey=Pubkey.from_string(WALLET_PUBKEY),
        lamports=100000
    ))

    message = Message.new_with_blockhash([ix], keypair.pubkey(), recent_blockhash)
    tx = Transaction.new_unsigned(message)
    signed_tx = tx.sign([keypair], recent_blockhash)

    sig = client.send_transaction(signed_tx, keypair)

    print("\n" + "="*70)
    print("🎉 ERSTER LIVE ON-CHAIN LOG ERFOLGREICH!")
    print("="*70)
    print(f"TX Signature: {sig.value}")
    print(f"Explorer: https://explorer.solana.com/tx/{sig.value}?cluster=devnet")
    print("="*70)

except Exception as e:
    print("❌ Fehler:")
    print(e)