import pandas as pd

def transform_stock_data(df: pd.DataFrame, ticker: str) -> pd.DataFrame:
    df = df.copy()

    # Kalau kolom MultiIndex (misalnya ada "Adj Close"), ambil level pertama
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Mapping nama kolom biar lebih konsisten
    rename_map = {
        "Date": "date",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Adj Close": "adj_close",
        "Volume": "volume"
    }
    df.rename(columns=rename_map, inplace=True)

    # Kalau tidak ada adj_close (karena auto_adjust=True di yfinance), buat kolom kosong
    if "adj_close" not in df.columns:
        df["adj_close"] = None

    # Hitung daily return
    if "close" in df.columns:
        df["daily_return"] = df["close"].pct_change()
    else:
        df["daily_return"] = None

    # Tambahkan ticker untuk identifikasi
    df["ticker"] = ticker

    # Konversi tanggal ke datetime
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    # Pastikan urutan kolom rapi
    return df[[
        "date", "open", "high", "low", "close",
        "adj_close", "volume", "daily_return", "ticker"
    ]]
