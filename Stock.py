from Record import Record
import random


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.records = []
        self.split_idx = None   # first future element index

    def append_record(self, record: Record):
        self.records.append(record)

    def random_split(self, min_past_steps: int, min_eval_steps: int) -> int:
        assert min_eval_steps > 0
        assert min_past_steps + min_eval_steps <= len(self.records)
        self.split_idx = random.randint(min_past_steps, len(self.records)-min_eval_steps)
        # return number of future steps
        return len(self.records) - self.split_idx

    def get_past(self, step: int) -> list:
        return self.records[:self.split_idx+step]

    def get_future(self, step: int) -> list:
        return self.records[self.split_idx+step:]
