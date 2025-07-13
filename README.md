# 🔄 Auto Swap Bot for Monad (via DZap)

Script Python ini menjalankan **swap otomatis token MON** ke beberapa token lain (WSOL, DAK, ETH, YAKI, CHOG) dan **swap kembali 50% ke MON**, secara berulang setiap **6 jam**, menggunakan **DZap Router** di jaringan **Monad Testnet**.

## 🚀 Fitur

- ✅ Swap token **MON → WSOL, DAK, ETH, YAKI, CHOG**
- 🔁 Swap balik **50% token tersebut ke MON**
- 🧠 Loop swap sesuai jumlah yang diinput user
- 📁 Mendukung **multi-wallet** dari `wallets.txt`
- ⏱️ Ulang otomatis **setiap 6 jam**
- 📡 Menggunakan **RPC Monad Testnet** dan **DZap Router**

## ⚙️ Instalasi

1. Install Python package yang dibutuhkan:
   ```bash
   pip install web3
   ```

2. Siapkan file `wallets.txt` berisi private key, satu per baris:
   ```
   0xPRIVATE_KEY_1
   0xPRIVATE_KEY_2
   ...
   ```

## 💻 Cara Menjalankan

Jalankan script:
```bash
python tai.py
```

Masukkan:
- Jumlah MON per swap (misalnya: `0.001`)
- Berapa kali swap per wallet (misalnya: `2`)

Script akan:
1. Swap MON ke masing-masing token target.
2. Swap kembali 50% dari token tersebut ke MON.
3. Lanjut ke wallet berikutnya.
4. Setelah selesai semua wallet, script **pause 6 jam** dan mengulang otomatis jika saldo cukup.

## 📦 Token Address

| Token | Address |
|-------|---------|
| MON (native) | `0x0000000000000000000000000000000000000000` |
| WSOL | `0x5387C85A4965769f6B0Df430638a1388493486F1` |
| DAK  | `0x0F0BDEbF0F83cD1EE3974779Bcb7315f9808c714` |
| ETH  | `0x836047a99e11F376522B447bffb6e3495Dd0637c` |
| YAKI | `0xfe140e1dCe99Be9F4F15d657CD9b7BF622270C50` |
| CHOG | `0xE0590015A873bF326bd645c3E1266d4db41C4E6B` |

## 🔗 Jaringan & Router

- **RPC Monad Testnet:**  
  `https://testnet-rpc.monad.xyz`

- **DZap Router Address:**  
  `0x00000000009726632680FB07Ddc7c4D5793BfE4F`

## ❗Catatan

- Bot ini digunakan untuk eksperimen di jaringan **testnet Monad**.
- Pastikan setiap wallet memiliki cukup saldo MON untuk biaya gas dan swap.
