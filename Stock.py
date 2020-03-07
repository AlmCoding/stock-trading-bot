from Record import Record


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.records = []

    def append_record(self, record: Record):
        self.records.append(record)
