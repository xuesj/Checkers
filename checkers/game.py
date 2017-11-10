# -*- coding: UTF-8 -*-

from checkers.board import GameBoard
from checkers.player import HumanPlayer, RandomPlayer


class Game(object):
    """Playing a game"""
    BEGIN = 0
    END = 1
    PROGRESS = 2

    def __init__(self, black_player, white_player):
        self._width = 3
        self._board = GameBoard(self._width)
        self._black_player = black_player
        self._white_player = white_player
        self._current_player = self._black_player
        self._moves = []
        self._steps = 0
        self._state = Game.BEGIN
        self._winner = None

    @property
    def moves(self):
        return self._moves

    @property
    def steps(self):
        return self._steps

    def play(self):
        while self._state != Game.END:
            i, j = self._current_player.next_move(self._board)
            if self._current_player == self._black_player:
                self._board.move(i, j, GameBoard.BLACK)
                self._current_player = self._white_player
                self._moves.append((i, j, GameBoard.BLACK))
            else:
                self._board.move(i, j, GameBoard.WHITE)
                self._current_player = self._black_player
                self._moves.append((i, j, GameBoard.WHITE))
            if self._state == Game.BEGIN:
                self._state = Game.PROGRESS
            self._steps += 1

            if self._board.check_state() == GameBoard.WHITE:
                self._winner = self._white_player
                self._state = Game.END

            if self._board.check_state() == GameBoard.BLACK:
                self._winner = self._black_player
                self._state = Game.END

    @property
    def winner(self):
        if self._winner == self._white_player:
            return 'WHITE'
        elif self._winner == self._black_player:
            return 'BLACK'
        else:
            return 'Nobody'


if __name__ == '__main__':
    James = RandomPlayer('James')
    Peter = RandomPlayer('Peter')
    a_game = Game(James, Peter)
    assert a_game.winner == 'Nobody'

    a_game.play()
    print('The steps is {s}'.format(s=a_game.steps))
    print('The winner is {}'.format(a_game.winner))
    for i, j, val in a_game.moves:
        print('{i}, {j} : {val}'.format(i=i, j=j, val=val))
