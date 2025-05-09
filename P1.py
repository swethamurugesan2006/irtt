import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock ticker symbol and the period for analysis
ticker_symbol = 'SPY'  # S&P 500 ETF as a proxy for the market
start_date = '2010-01-01'
end_date = '2025-01-01'

# Fetch historical stock data
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Calculate the 50-day and 200-day moving averages
stock_data['50_MA'] = stock_data['Close'].rolling(window=50).mean()
stock_data['200_MA'] = stock_data['Close'].rolling(window=200).mean()

# Plot the closing price along with the moving averages
plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label='Closing Price', color='blue')
plt.plot(stock_data['50_MA'], label='50-Day MA', color='red')
plt.plot(stock_data['200_MA'], label='200-Day MA', color='green')
plt.title(f'{ticker_symbol} Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
