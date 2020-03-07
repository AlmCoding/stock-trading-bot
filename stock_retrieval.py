import time
import csv

from finnhub import client as Finnhub
from api_key import API_KEY


dow = ["MMM", "AXP", "AAPL", "BA", "CAT", "CVX", "CSCO", "KO", "DIS", "DOW", "XOM", "GS", "HD", "IBM", "INTC",
       "JNJ", "JPM", "MCD", "MRK", "MSFT", "NKE", "PFE", "PG", "TRV", "UTX", "UNH", "VZ", "V", "WBA", "WMT", "GOOG"]

client = Finnhub.Client(api_key=API_KEY)
for symbol in dow:
    stock_candle = client.stock_candle(symbol=symbol, resolution="D", count=3650)
    if stock_candle["s"] != "ok":
        continue

    file_path = "data/Dow_{}.csv".format(symbol)
    with open(file_path, "w", newline='') as fobj:
        field_names = [key for key in stock_candle.keys() if key != "s"]
        writer = csv.DictWriter(fobj, fieldnames=field_names)
        writer.writeheader()
        for i in range(len(stock_candle[field_names[0]])):
            obj = {key: stock_candle[key][i] for key in field_names}
            writer.writerow(obj)

    time.sleep(1)


#supported_stocks = client.stock_symbol(exchange="US")
#supported_cryptos = client.crypto_symbol(exchange="binance")
#stock_candle = client.stock_candle(symbol="NFLX", resolution="D", count=20)
#stock_candle = client.stock_candle(symbol="AAPL", resolution="D", count=365)
#client.crypto_candle(symbol="BINANCE:BTCUSDT", resolution="D", count=200)
