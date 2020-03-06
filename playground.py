from finnhub import client as Finnhub
from api_key import API_KEY

client = Finnhub.Client(api_key=API_KEY)

#supported_stocks = client.stock_symbol(exchange="US")
#supported_cryptos = client.crypto_symbol(exchange="binance")

#stock_candle = client.stock_candle(symbol="NFLX", resolution="D", count=20)


stock_candle = client.stock_candle(symbol="AAPL", resolution="D", count=30)


#client.crypto_candle(symbol="BINANCE:BTCUSDT", resolution="D", count=200)

a = 12
