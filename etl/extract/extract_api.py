import yfinance as yf
import pandas as pd
import logging

def extract_from_yahoo(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Ambil data saham dari Yahoo Finance
    """
    logging.info(f"Memulai download data {ticker}")
    stock = yf.download(ticker, start=start, end=end)
    stock.reset_index(inplace=True)
    logging.info(f"Data {ticker} berhasil di-download, total {len(stock)} baris")
    return stock
