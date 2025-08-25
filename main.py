import logging
import datetime
from etl.extract.extract_api import extract_from_yahoo
from etl.transform.transform_data import transform_stock_data
from etl.load.load_db import save_to_db

# 🔹 Config logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 🔹 Konfigurasi Database
db_config = {
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432",
    "database": "finance_db"
}

# 🔹 Daftar saham (5 perusahaan besar)
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

# 🔹 Range tanggal (default: 2025-01-01 sampai hari ini)
start_date = "2025-01-01"
end_date = datetime.date.today().strftime("%Y-%m-%d")

def run_etl():
    for ticker in tickers:
        try:
            logging.info(f"🚀 Mulai proses ETL untuk {ticker}")

            # Extract
            df = extract_from_yahoo(ticker, start_date, end_date)
            logging.info(f"✅ Extract {ticker} berhasil, total {len(df)} baris")

            # Transform
            df_transformed = transform_stock_data(df)
            logging.info(f"✅ Transform {ticker} berhasil")

            # Load
            save_to_db(df_transformed, f"{ticker}_stock", db_config)
            logging.info(f"✅ Load {ticker} ke tabel {ticker}_stock berhasil")

        except Exception as e:
            logging.error(f"❌ Error memproses {ticker}: {e}")

    logging.info("🎉 ETL pipeline selesai untuk semua ticker")

if __name__ == "__main__":
    run_etl()
