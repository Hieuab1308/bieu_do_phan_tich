import yfinance as yf
import pandas as pd 
import mplfinance as mpf

symbol = 'BTC-USD'
start_data = '2022-10-01'
end_data = '2023-10-01'
data = yf.download(symbol, start = start_data, end= end_data)
data.to_csv('stock_data.csv')

data = pd.read_csv("stock_data.csv", index_col=0, parse_dates=True)
mpf.plot(data, type = "line", style = "yahoo", title = "bieu do gia", ylabel = "gia")