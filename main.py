import os
import json
from solana.rpc.api import Client
from solana.keypair import Keypair
from solana.system_program import transfer, TransferParams
from solana.transaction import Transaction

def create_new_wallet():
    new_keypair = Keypair.generate()
    
    private_key_str = json.dumps(list(new_keypair.secret_key))
    
    print(f"New Solana Wallet Generated:\nPublic Key: {new_keypair.public_key}\nPrivate Key: {private_key_str}")
    return private_key_str

def main():
    privatekey = os.environ.get("WALLET_PRIVATE_KEY")
    if not privatekey:
        privatekey = create_new_wallet()

    wallet_private_key_bytes = json.loads(privatekey)
    sender_keypair = Keypair.from_secret_key(bytes(wallet_private_key_bytes))

    recipient_pubkey = "RecipientPublicKeyHere"

    client = Client("https://api.mainnet-beta.solana.com")

    amount_lamports = 1000000 

    transfer_ix = transfer(TransferParams(from_pubkey=sender_keypair.public_key,
                                          to_pubkey=recipient_pubkey,
                                          lamports=amount_lamports))

    transaction = Transaction().add(transfer_ix)

    response = client.send_transaction(transaction, sender_keypair)
    print("Transaction response:", response)

if __name__ == "__main__":
    main()