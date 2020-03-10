from copy import copy

from agents.Agent import Agent
from Stock import Stock
from Portfolio import Portfolio


class Simulator:
    def __init__(self, agent: Agent, stocks: list, portfolio: Portfolio, min_past_steps=300, min_eval_steps=300):
        self._agent = agent
        self._stocks = stocks
        self._portfolio = portfolio
        self._min_past_steps = min_past_steps
        self._min_eval_steps = min_eval_steps

    def run(self, iterations=10):
        for stock in self._stocks:
            portfolio_histories = []
            for _ in range(iterations):
                portfolio_history = self.apply(self._agent, stock)
                portfolio_histories.append(portfolio_history)
            # stock.portfolio_histories = portfolio_histories

    def apply(self, agent: Agent, stock: Stock):
        portfolio_history = [copy(self._portfolio)]
        evaluation_steps = stock.random_split(self._min_past_steps, self._min_eval_steps)
        try:
            for step in range(evaluation_steps):
                past = stock.get_past(step)
                print(past[-1].close)
                #action = agent.run(past)
                #current_state = copy(portfolio_history[-1])
                #new_portfolio = current_state.apply_action(action, past[-1].close)
                #portfolio_history.append(new_portfolio)
        except:
            print("Agent failed to survive!")

        return portfolio_history
