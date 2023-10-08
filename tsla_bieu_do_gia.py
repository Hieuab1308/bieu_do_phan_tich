import pandas as pd
import yfinance as yf
import mplfinance as mpf

symplol = 'TSLA'
start_date ='2023-01-01'
end_date ='2023-10-01'
data = yf.download(symplol, start=start_date,end= end_date)
data.to_csv('stock_data.csv')

data = pd.read_csv("stock_data.csv" ,index_col = 0 , parse_dates = True)
mpf.plot(data, type = "line" ,style = "yahoo", title ="bieu do gia TSLA", ylabel ="gia")