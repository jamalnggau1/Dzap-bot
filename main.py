from web3 import Web3
import time

# === SETUP ===
RPC_URL = "https://testnet-rpc.monad.xyz"
ROUTER_ADDRESS = Web3.to_checksum_address("0x00000000009726632680FB07Ddc7c4D5793BfE4F")
MON_TOKEN = "0x0000000000000000000000000000000000000000"
TOKENS = {
    "WSOL": "0x5387C85A4965769f6B0Df430638a1388493486F1",
    "DAK":  "0x0F0BDEbF0F83cD1EE3974779Bcb7315f9808c714",
    "ETH":  "0x836047a99e11F376522B447bffb6e3495Dd0637c",
    "YAKI": "0xfe140e1dCe99Be9F4F15d657CD9b7BF622270C50",
    "CHOG": "0xE0590015A873bF326bd645c3E1266d4db41C4E6B",
}

# === INPUT USER ===
amount_mon = float(input("Jumlah MON per token (dalam MON): "))
loop_count = int(input("Berapa kali ingin melakukan swap?: "))

# === BACA WALLET ===
with open("wallets.txt", "r") as f:
    private_keys = [line.strip() for line in f if line.strip()]

# === FUNGSI ===
def build_data(method_id, from_token, to_token, amount_in_wei, min_out, deadline, user_address, fee=0):
    return (
        method_id +
        bytes.fromhex(from_token[2:]).rjust(32, b'\x00').hex() +
        bytes.fromhex(to_token[2:]).rjust(32, b'\x00').hex() +
        int(amount_in_wei).to_bytes(32, "big").hex() +
        int(min_out).to_bytes(32, "big").hex() +
        int(deadline).to_bytes(32, "big").hex() +
        bytes.fromhex(user_address[2:]).rjust(32, b'\x00').hex() +
        int(fee).to_bytes(32, "big").hex()
    )

def send_swap(w3, account, from_token, to_token, amount_in_wei, is_mon_in=False):
    sender = account.address
    nonce = w3.eth.get_transaction_count(sender, "pending")
    deadline = int(time.time()) + 1800
    method_id = "0x2e4586c4"
    tx_value = amount_in_wei if is_mon_in else 0

    tx = {
        "from": sender,
        "to": ROUTER_ADDRESS,
        "value": tx_value,
        "gas": 500_000,
        "gasPrice": w3.eth.gas_price,
        "nonce": nonce,
        "chainId": w3.eth.chain_id,
        "data": build_data(method_id, from_token, to_token, amount_in_wei, 0, deadline, sender),
    }

    signed_tx = w3.eth.account.sign_transaction(tx, account.key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(f"🚀 Tx terkirim: {w3.to_hex(tx_hash)}")
    try:
        print("⏳ Menunggu konfirmasi...")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=300, poll_latency=5)
        print(f"✅ Terkonfirmasi di block {receipt.blockNumber}")
    except Exception as e:
        print(f"⚠️ Gagal konfirmasi: {e}")

# === PROSES UTAMA ===
w3 = Web3(Web3.HTTPProvider(RPC_URL))

while True:
    try:
        for pk in private_keys:
            account = w3.eth.account.from_key(pk)
            sender = account.address
            balance = w3.from_wei(w3.eth.get_balance(sender), "ether")
            print(f"\n🧾 Wallet: {sender} | Balance: {balance} MON")

            amount_in_wei = w3.to_wei(amount_mon, "ether")
            half_in_wei = int(amount_in_wei // 2)

            for i in range(loop_count):
                print(f"\n🔁 Swap {i+1}/{loop_count} - Wallet: {sender}")

                for name, token_address in TOKENS.items():
                    print(f"🔄 Swap MON → {name}")
                    send_swap(w3, account, MON_TOKEN, token_address, amount_in_wei, is_mon_in=True)
                    time.sleep(2)

                    print(f"🔁 Swap {name} → MON (50%)")
                    send_swap(w3, account, token_address, MON_TOKEN, half_in_wei, is_mon_in=False)
                    time.sleep(2)

        print("\n✅ Semua swap selesai! Menunggu 6 jam...\n")
        time.sleep(21600)  # 6 jam

    except KeyboardInterrupt:
        print("🛑 Dihentikan oleh pengguna.")
        break
    except Exception as e:
        print(f"⚠️ Error: {e}")
        print("🔄 Menunggu 10 detik dan coba lagi...")
        time.sleep(10)
