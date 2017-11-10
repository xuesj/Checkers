# -*- codding: UTF-8 -*-

import numpy as np


class GameBoard(object):
    """Define the board of game."""
    WHITE = 1
    BLACK = -1

    def __init__(self, x):
        self._x = x
        self._field = np.zeros((x, x), dtype='int8')

    @property
    def field(self):
        return self._field

    @property
    def width(self):
        return self._x

    def check_state(self):
        """board is dict of positon of white and black"""
        if self.check_value(GameBoard.WHITE):
            return GameBoard.WHITE

        if self.check_value(GameBoard.BLACK):
            return GameBoard.BLACK

        return None

    def check_value(self, value):
        for j in range(self._x):
            if all(self._field[i, j] == value for i in range(self._x)):
                return True

        for i in range(self._x):
            if all(self._field[i, j] == value for j in range(self._x)):
                return True

        if all(self._field[i, i] == value for i in range(self._x)):
            return True

        if all(self._field[i, self._x - 1 - i] for i in range(self._x)):
            return True

        return False

    def move(self, i, j, value):
        assert i in range(self._x)
        assert j in range(self._x)
        assert self._field[i, j] == 0
        assert value is GameBoard.WHITE or value is GameBoard.BLACK
        self._field[i, j] = value

    def remove(self, i, j):
        assert i in range(self._x)
        assert j in range(self._x)
        assert self._field[i, j] != 0
        self._field[i, j] = 0

    def remove_all(self):
        self._field = np.zeros((self._x, self._x), dtype='int8')

    def legal_moves(self):
        return set([(i, j) for i in range(self._x)
                           for j in range(self._x)
                           if self._field[i, j] == 0])


if __name__ == '__main__':
    game_board = GameBoard(3)
    game_board.remove_all()
    game_board.move(2, 0, GameBoard.BLACK)
    game_board.move(0, 2, GameBoard.WHITE)
    game_board.move(1, 2, GameBoard.BLACK)
    game_board.move(2, 1, GameBoard.WHITE)
    game_board.move(0, 0, GameBoard.BLACK)
    game_board.move(1, 1, GameBoard.WHITE)
    assert game_board.check_state() != GameBoard.WHITE
