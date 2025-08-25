# Stock Market ETL Pipeline with PostgreSQL

## 📌 Deskripsi
Project ini adalah implementasi **ETL (Extract, Transform, Load) Pipeline** untuk data saham.  
Pipeline mengambil data historis saham dari **Yahoo Finance** menggunakan library `yfinance`, melakukan transformasi data dengan `pandas`, lalu menyimpannya ke dalam **PostgreSQL** untuk kebutuhan analisis lebih lanjut.

## 🛠️ Tech Stack
- **Python 3.x**
- **yfinance** → untuk mengambil data saham
- **Pandas** → transformasi data
- **SQLAlchemy / psycopg2** → koneksi ke PostgreSQL
- **PostgreSQL** → database penyimpanan

## 🚀 Fitur
- Extract: Mengambil data historis saham dari Yahoo Finance.
- Transform: Membersihkan data, reset index, serta menambahkan kolom perhitungan log return.
- Load: Menyimpan data hasil transformasi ke PostgreSQL.
- Modular: Struktur kode terpisah (extract, transform, load) sehingga mudah dikembangkan.

## 📂 Struktur Project
