import matplotlib
matplotlib.use('Agg')

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

ticker_symbol = 'SPY'
start_date = '2010-01-01'
end_date = '2025-01-01'

stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

stock_data['50_MA'] = stock_data['Close'].rolling(window=50).mean()
stock_data['200_MA'] = stock_data['Close'].rolling(window=200).mean()

plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label='Closing Price')
plt.plot(stock_data['50_MA'], label='50-Day MA')
plt.plot(stock_data['200_MA'], label='200-Day MA')

plt.legend()
plt.grid(True)

import os
os.makedirs("output", exist_ok=True)
plt.savefig("output/plot.png")
