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
python main.py
```

Masukkan:
- Jumlah MON per swap (misalnya: `0.001`)
- Berapa kali swap per wallet (misalnya: `2`)

Script akan:
1. Swap MON ke masing-masing token target.
2. Swap kembali 50% dari token tersebut ke MON.
3. Lanjut ke wallet berikutnya.
4. Setelah selesai semua wallet, script **pause 6 jam** dan mengulang otomatis jika saldo cukup.

## ❗Catatan

- Bot ini digunakan untuk eksperimen di jaringan **testnet Monad**.
- Pastikan setiap wallet memiliki cukup saldo MON untuk biaya gas dan swap.
