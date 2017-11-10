# -*- coding: UTF-8 -*-
from checkers.player import HumanPlayer, RandomPlayer
from checkers.board import GameBoard

game_board = GameBoard(3)
game_board.move(0, 0, GameBoard.BLACK)
game_board.move(0, 1, GameBoard.WHITE)

name = 'James'
a_player = HumanPlayer(name)
r_player = RandomPlayer('Random')


def test_human_player():
    assert a_player.name == 'James'
    assert r_player.name == 'Random'

    # i, j = a_player.next_move(game_board)
    # """input 1, 2"""
    # assert (i, j) == (1, 2)
