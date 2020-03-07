from copy import copy

from Agent import Agent
from Stock import Stock
from State import State


class Simulator:
    def __init__(self, agent: Agent, stocks: list, state: State):
        self._agent = agent
        self._stocks = stocks
        self._state = state

        self._state_history = []
        self._state_histories = []
 
    def simulate(self, iterations=100):
        for stock in self._stocks:
            state_histories = []
            for _ in range(iterations):
                state_history = self.apply(self._agent, stock)
                state_histories.append(state_history)
            stock.state_histories = state_histories
    
    def apply(self, agent: Agent, stock: Stock):
        state_history = [copy(self._state)]
        steps = stock.random_split()
        try:
            for step in range(steps): 
                past = stock.get_past(step)
                action = agent.run(past)
                current_state = copy(state_history[-1])
                new_state = current_state.apply_action(action, past[-1])
                state_history.append(new_state)
        except:
            print("Agent failed to survive!")

        return state_history
