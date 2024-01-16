pip install yfinance
pip install pandas_datareader

import yfinance as yf
import pandas as pd

def get_stock_info(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        # Extract the relevant information
        market_cap = info.get("marketCap", "N/A")
        roe = info.get("returnOnEquity", "N/A")
        eps = info.get("trailingEps", "N/A")
        pe_ratio = info.get("trailingPE", "N/A")

        return {
            "Symbol": symbol,
            "Market Cap": market_cap,
            "ROE": roe,
            "EPS": eps,
            "P/E Ratio": pe_ratio
        }
