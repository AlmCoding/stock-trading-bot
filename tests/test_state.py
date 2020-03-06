from State import State
from Action import Action


def test_state_add_funds():
    state = State(100.0)
    funds = state.add_funds(100.5)
    assert funds == 200.5


def test_state_close():
    state = State(0.0)
    state._position = 10
    funds, position = state.apply(Action.CLOSE, 10.0)
    assert funds == 100.0
    assert position == 0


def test_state_long():
    state = State(100.0)
    funds, position = state.apply(Action.LONG, 30.0)
    assert funds == 10.0
    assert position == 3


def test_state_short():
    state = State(100.0)
    funds, position = state.apply(Action.SHORT, 30.0)
    assert funds == 190.0
    assert position == -3


def test_state_mix():
    state = State(100.0)
    funds, position = state.apply(Action.CLOSE, 10.0)
    assert funds == 100.0
    assert position == 0

    funds, position = state.apply(Action.LONG, 40.0)
    assert funds == 20.0
    assert position == 2

    funds, position = state.apply(Action.LONG, 5.0)
    assert funds == 0.0
    assert position == 6

    funds, position = state.apply(Action.CLOSE, 10.0)
    assert funds == 60.0
    assert position == 0

    funds, position = state.apply(Action.SHORT, 10.0)
    assert funds == 120.0
    assert position == -6

    funds, position = state.apply(Action.LONG, 20.0)
    assert funds == 0.0
    assert position == 0
