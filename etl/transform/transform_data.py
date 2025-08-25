import pandas as pd

def transform_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Versi awal transformasi: hanya hitung Daily_Return
    """
    df = df.copy()

    # Jika ada 'Adj Close', gunakan sebagai Close
    if 'Adj Close' in df.columns:
        df['Close'] = df['Adj Close']

    # Hitung Daily_Return
    df['Daily_Return'] = df['Close'].pct_change()

    # Pastikan kolom Date ada
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])

    return df
