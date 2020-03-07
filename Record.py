

class Record:
    def __init__(self, data: dict):
        keys = tuple(data.keys())
        assert keys == ("c", "h", "l", "o", "t", "v")
        self.open = data["o"]
        self.high = data["h"]
        self.low = data["l"]
        self.close = data["c"]
        self.volume = data["v"]
        self.timestamp = data["t"]
