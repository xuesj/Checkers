# -*- coding: UTF-8 -*-

from checkers.board import Board
import random


class Player(object):
    """Player"""

    def __init__(self, name):
        self._name = name
        self._win_rate = 0.0

    @property
    def name(self):
        return self._name

    def next_move(self, game):
        pass


class HumanPlayer(Player):

    def __init__(self, name):
        super(HumanPlayer, self).__init__(name)

    def next_move(self, board):
        """
        get next legal move for board of GameBoard
        :param board: GameBoard
        :param value: GameBoard.WHITE or GameBoard.BLACK
        :return: i, j
        """
        board.print_board()
        move_str = input('x, y: ')
        i, j = map(lambda x: int(x.strip()), move_str.split(','))
        assert i in range(board.width)
        assert j in range(board.width)
        assert (i, j) in board.legal_moves()
        return i, j


class RandomPlayer(Player):

    def __init__(self, name):
        super(RandomPlayer, self).__init__(name)

    def next_move(self, board):
        """
        get next legal move for board of GameBoard
        :param board: GameBoard
        :param value: GameBoard.WHITE or GameBoard.BLACK
        :return: i, j
        """
        i, j = random.choice(list(board.legal_moves()))
        return i, j


if __name__ == '__main__':
    game_board = Board(3)
    game_board.move(0, 0, Board.BLACK)
    game_board.move(0, 1, Board.WHITE)

    name = 'James'
    a_player = HumanPlayer(name)
    r_player = RandomPlayer('Random')

    assert a_player.name == 'James'
    assert r_player.name == 'Random'

    i, j = a_player.next_move(game_board)
    print('({i}, {j})'.format(i=i, j=j))

    i, j = r_player.next_move(game_board)
    print('({i}, {j})'.format(i=i, j=j))