import time
import csv
import os

from finnhub import client as Finnhub
from api_key import API_KEY
from Stock import Stock
from Record import Record


def load_stock_data(index):
    stocks = []
    directory = os.path.join(os.curdir, "data", index)
    file_paths = [os.path.join(directory, name) for name in os.listdir(directory)]
    for file_path in file_paths:
        symbol = os.path.basename(file_path).split(".")[0]
        stock = Stock(symbol)
        with open(file_path, "r", newline='') as fobj:
            reader = csv.DictReader(fobj)
            for row in reader:
                stock.append_record(Record(row))
        stocks.append(stock)
    return stocks


def download_stock_data(index: str, symbols: list, count: int, resolution="D"):
    client = Finnhub.Client(api_key=API_KEY)
    for symbol in symbols:
        stock_candle = client.stock_candle(symbol=symbol, resolution=resolution, count=count)
        if stock_candle["s"] != "ok":
            continue

        directory = os.path.join(os.curdir, "data", index)
        if not os.path.exists(directory):
            os.mkdir(directory)
        file_path = os.path.join(directory, "{}.csv".format(symbol))
        with open(file_path, "w", newline='') as fobj:
            field_names = [key for key in stock_candle.keys() if key != "s"]
            writer = csv.DictWriter(fobj, fieldnames=field_names)
            writer.writeheader()
            for i in range(len(stock_candle[field_names[0]])):
                obj = {key: stock_candle[key][i] for key in field_names}
                writer.writerow(obj)
        time.sleep(1)


if __name__ == "__main__":
    dow = ["MMM", "AXP", "AAPL", "BA", "CAT", "CVX", "CSCO", "KO", "DIS", "DOW", "XOM", "GS", "HD", "IBM", "INTC",
           "JNJ", "JPM", "MCD", "MRK", "MSFT", "NKE", "PFE", "PG", "TRV", "UTX", "UNH", "VZ", "V", "WBA", "WMT", "GOOG"]
    # download_stock_data("Dow", dow, count=3650)

    load_stock_data("Dow")
