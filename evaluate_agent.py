from stock_loader import load_stock_data
from Portfolio import Portfolio
from Simulator import Simulator

from agents.TestAgent import TestAgent


funds = 10.0e3


if __name__ == "__main__":

    # Init Portfolio
    portfolio = Portfolio(funds)

    # Load Stock Data
    stocks = load_stock_data("Dow")

    # Select Agent
    agent = TestAgent()

    # Run simulation
    simulator = Simulator(agent, stocks, portfolio)
    simulator.run()
