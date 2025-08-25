import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import logging

def save_to_db(df: pd.DataFrame, table_name: str, db_config: dict):
    """Simpan DataFrame ke PostgreSQL, append data jika tabel sudah ada"""
    try:
        engine = create_engine(
            f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
        )
        df.to_sql(table_name, engine, if_exists='append', index=False)
        logging.info(f"Data {table_name} berhasil disimpan/diappend ke PostgreSQL")
    except SQLAlchemyError as e:
        logging.error(f"Error saat menyimpan {table_name}: {e}")
        raise
