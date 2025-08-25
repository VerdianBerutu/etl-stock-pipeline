
from db_config import get_engine
from sqlalchemy.exc import SQLAlchemyError

engine = get_engine()
try:
    with engine.connect() as conn:
        print("✅ Koneksi ke database berhasil!")
except Exception as e:
    print("❌ Gagal konek ke database:", e)
