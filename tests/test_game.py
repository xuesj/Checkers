# -*- coding: UTF-8 -*-

from checkers.board import GameBoard
from checkers.player import HumanPlayer, RandomPlayer
from checkers.game import Game


def test_game():
    james = RandomPlayer('James')
    peter = RandomPlayer('Peter')
    a_game = Game(james, peter)
    assert a_game.winner == 'Nobody'

    a_game.play()
    print('The winner is {}'.format(a_game.winner))
    for i, j, val in a_game.moves:
        print('{i}, {j} : {val}'.format(i=i, j=j, val=val))
