from agents.Agent import Agent
from Action import Action


class TestAgent(Agent):
    def __init__(self):
        super().__init__()
        pass

    def run(self, past):
        return self.follow_day_trend(past)

    @staticmethod
    def follow_day_trend(past):
        record = past[-1]
        diff = record.close - record.open

        if diff > 0:
            return Action.LONG
        else:
            return Action.SHORT
