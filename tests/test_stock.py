from Stock import Stock
from Record import Record


def test_append_record():
    record = Record({"c": .0, "h": .0, "l": .0, "o": .0, "t": 0, "v": 0})
    stock = Stock("SYMBOL")
    assert len(stock.records) == 0
    stock.append_record(record)
    assert len(stock.records) == 1
    stock.append_record(record)
    assert len(stock.records) == 2


def test_random_split():
    record = Record({"c": .0, "h": .0, "l": .0, "o": .0, "t": 0, "v": 0})
    stock = Stock("SYMBOL")
    for i in range(10):
        stock.append_record(record)

    for i in range(1000):
        future_size = stock.random_split(2, 3)
        assert future_size >= 3
        assert stock.split_idx >= 2




