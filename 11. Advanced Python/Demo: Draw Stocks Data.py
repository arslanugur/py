# Borsa verileri çekme
# Library
# pip install yfinance

import yfinance as yf

stock = yf.Ticker('AMZN')   # 'AMZN' - Stock Code

data = stcok.history(period = '1d', start = '2020-1-1', end = '2020-12-24') # Yine de, Anlık verileri çekmek daha önemli 

print(data)

