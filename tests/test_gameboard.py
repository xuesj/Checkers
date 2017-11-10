# -*- coding: utf-8 -*-

from checkers.board import GameBoard
import numpy as np


def test_game_board():
    """test init"""
    game_board = GameBoard(3)
    zero_field = np.zeros((3, 3))
    game_field = game_board.field

    assert game_board
    assert (zero_field == game_field).all()
    assert game_board.check_state() is None

    """test function move"""
    game_board.move(0, 0, GameBoard.BLACK)
    game_board.move(0, 1, GameBoard.WHITE)
    game_field = game_board.field
    assert game_field[0, 0] == GameBoard.BLACK
    assert game_field[0, 1] == GameBoard.WHITE

    try:
        game_board.move(0, 1, GameBoard.WHITE)
    except AssertionError:
        pass

    try:
        game_board.move(2, 2, 0)
    except AssertionError:
        pass

    """test function check_win"""
    game_board.remove_all()
    game_board.move(2, 0, GameBoard.BLACK)
    game_board.move(0, 2, GameBoard.WHITE)
    game_board.move(1, 2, GameBoard.BLACK)
    game_board.move(2, 1, GameBoard.WHITE)
    game_board.move(0, 0, GameBoard.BLACK)
    game_board.move(1, 1, GameBoard.WHITE)
    assert game_board.check_state() != GameBoard.WHITE

    """test function remove"""
    game_board.remove(0, 2)
    game_board.remove(1, 1)
    game_board.remove(2, 0)
    game_field = game_board.field
    assert game_field[0, 2] == 0
    assert game_field[1, 1] == 0
    assert game_field[2, 0] == 0

    """test function remove_all"""
    game_board.remove_all()
    game_field = game_board.field
    assert (zero_field == game_field).all()

    """test function legal_moves"""
    game_board.move(0, 0, GameBoard.BLACK)
    game_board.move(0, 1, GameBoard.WHITE)
    game_board.move(0, 2, GameBoard.BLACK)
    game_board.move(1, 0, GameBoard.BLACK)
    game_board.move(1, 1, GameBoard.WHITE)
    game_board.move(1, 2, GameBoard.BLACK)
    moves = set([(2, 0), (2, 1), (2, 2)])
    assert game_board.legal_moves() == moves
