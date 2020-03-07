

class Record:
    def __init__(self, data: dict):
        keys = tuple(data.keys())
        assert keys == ("c", "h", "l", "o", "t", "v")
        assert isinstance(data["o"], float)
        assert isinstance(data["h"], float)
        assert isinstance(data["l"], float)
        assert isinstance(data["c"], float)
        assert isinstance(data["v"], int)
        assert isinstance(data["t"], int)

        self.open = data["o"]
        self.high = data["h"]
        self.low = data["l"]
        self.close = data["c"]
        self.volume = data["v"]
        self.timestamp = data["t"]
