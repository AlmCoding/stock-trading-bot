

class Record:
    def __init__(self, data: dict):
        keys = tuple(data.keys())
        assert keys == ("c", "h", "l", "o", "t", "v")

        self.open = float(data["o"])
        self.high = float(data["h"])
        self.low = float(data["l"])
        self.close = float(data["c"])
        self.volume = int(data["v"])
        self.timestamp = int(data["t"])
