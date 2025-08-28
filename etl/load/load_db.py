import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import logging

def save_to_db(df: pd.DataFrame, db_config: dict, table_name: str = "stock_prices"):
    """
    Simpan DataFrame ke PostgreSQL dalam tabel tunggal stock_prices.
    Jika tabel belum ada → otomatis dibuat.
    """

    try:
        engine = create_engine(
            f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@"
            f"{db_config['host']}:{db_config['port']}/{db_config['database']}"
        )

        # Normalisasi nama kolom biar aman (lowercase semua)
        df.columns = df.columns.str.lower()

        # Pastikan hanya kolom yang dibutuhkan
        expected_columns = ["date", "open", "high", "low", "close", "volume", "ticker"]
        df = df[expected_columns]

        # Simpan ke tabel stock_prices
        df.to_sql(table_name, engine, if_exists="append", index=False)

        logging.info(f"✅ Data {len(df)} baris berhasil disimpan ke tabel {table_name}")

    except SQLAlchemyError as e:
        logging.error(f"❌ Error saat menyimpan ke {table_name}: {e}")
        raise
