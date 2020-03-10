from Portfolio import Portfolio
from Action import Action
from Record import Record


def test_portfolio_add_funds():
    portfolio = Portfolio(100.0)
    funds = portfolio.add_funds(100.5)
    assert funds == 200.5


def test_portfolio_close():
    portfolio = Portfolio(0.0)
    portfolio._position = 10
    funds, position = portfolio.apply_action(Action.CLOSE, 10.0, 0)
    assert funds == 100.0
    assert position == 0


def test_portfolio_long():
    portfolio = Portfolio(100.0)
    funds, position = portfolio.apply_action(Action.LONG, 30.0, 0)
    assert funds == 10.0
    assert position == 3


def test_portfolio_short():
    portfolio = Portfolio(100.0)
    funds, position = portfolio.apply_action(Action.SHORT, 30.0, 0)
    assert funds == 190.0
    assert position == -3


def test_portfolio_mix():
    portfolio = Portfolio(100.0)
    funds, position = portfolio.apply_action(Action.CLOSE, 10.0, 0)
    assert funds == 100.0
    assert position == 0

    funds, position = portfolio.apply_action(Action.LONG, 40.0, 0)
    assert funds == 20.0
    assert position == 2

    funds, position = portfolio.apply_action(Action.LONG, 5.0, 0)
    assert funds == 0.0
    assert position == 6

    funds, position = portfolio.apply_action(Action.CLOSE, 10.0, 0)
    assert funds == 60.0
    assert position == 0

    funds, position = portfolio.apply_action(Action.SHORT, 10.0, 0)
    assert funds == 120.0
    assert position == -6

    failed = False
    try:
        portfolio.apply_action(Action.LONG, 20.0, 0)
    except:
        failed = True
    assert failed
