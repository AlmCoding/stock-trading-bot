import math
from Action import Action


class State:
    def __init__(self, funds):
        self._funds = funds
        self._position = 0
        self._price = .0
    
    def add_funds(self, funds):
        if funds >= .0:
            self._funds += funds
        else:
            raise Exception("Unable to add negative funds!")
        return self._funds

    def apply(self, action: Action, price: float):
        self._price = price
        self._close()
        if action is Action.LONG:
            self._long()
        elif action == Action.SHORT:
            self._short()
        return self._funds, self._position

    def _close(self):
        self._funds += self._position * self._price
        self._position = 0
        return self._funds

    def _long(self):
        self._position = int(self._funds // self._price)
        self._funds -= self._position * self._price

    def _short(self):
        self._position = -int(self._funds // self._price)
        self._funds -= self._position * self._price


if __name__ == "__main__":
    state = State(100.0)

    state.apply(Action.SHORT, 20)
    state.apply(Action.LONG, 10)
    state.apply(Action.OUT, 20)

    state.apply(Action.LONG, 30.0)
    state.add_funds(20.0)
    state.apply(Action.LONG, 30.0)
    state.add_funds(10.0)
    state.apply(Action.LONG, 9.0)

    state.apply(Action.OUT, 10.0)
    state.apply(Action.SHORT, 20)
