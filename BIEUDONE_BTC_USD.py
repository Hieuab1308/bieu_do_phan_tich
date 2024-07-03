import yfinance as yf
import mplfinance as mpf

symol = 'BTC-USD'
start_date = '2023-01-01'
end_date = '2023-10-01'
data = yf.download(symol, start=start_date, end=end_date)
data.to_csv('stock_data.csv')
mpf.plot(data, type="candle", style="yahoo", title="bieu do nen BTC-USD", ylabel="gia")      