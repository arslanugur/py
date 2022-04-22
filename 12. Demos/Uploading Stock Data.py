# pip install yfinance     # Kütüphane kurulumu
import yfinance as yf

stock = yf.Ticker('AMZN')

data = stock.history(period='1d', start='2020-1-1', end='2020-12-24')

print(data)



