# -*- coding: utf-8 -*-

from checkers.board import Board
import numpy as np


def test_board():
    """test init"""
    board = Board(3)
    zero_field = np.zeros((3, 3), dtype='int8')
    game_field = board.field

    assert board
    assert (zero_field == game_field).all()
    assert board.check_state() is None

    """test function move"""
    board.move(0, 0, Board.BLACK)
    board.move(0, 1, Board.WHITE)
    game_field = board.field
    assert game_field[0, 0] == Board.BLACK
    assert game_field[0, 1] == Board.WHITE

    try:
        board.move(0, 1, Board.WHITE)
    except AssertionError:
        pass

    try:
        board.move(2, 2, 0)
    except AssertionError:
        pass

    """test function check_win"""
    board.remove_all()
    board.move(2, 0, Board.BLACK)
    board.move(0, 2, Board.WHITE)
    board.move(1, 2, Board.BLACK)
    board.move(2, 1, Board.WHITE)
    board.move(0, 0, Board.BLACK)
    board.move(1, 1, Board.WHITE)
    assert board.check_state() != Board.WHITE

    """test function remove"""
    board.remove(0, 2)
    board.remove(1, 1)
    board.remove(2, 0)
    game_field = board.field
    assert game_field[0, 2] == 0
    assert game_field[1, 1] == 0
    assert game_field[2, 0] == 0

    """test function remove_all"""
    board.remove_all()
    game_field = board.field
    assert (zero_field == game_field).all()

    """test function legal_moves"""
    board.move(0, 0, Board.BLACK)
    board.move(0, 1, Board.WHITE)
    board.move(0, 2, Board.BLACK)
    board.move(1, 0, Board.BLACK)
    board.move(1, 1, Board.WHITE)
    board.move(1, 2, Board.BLACK)
    moves = set([(2, 0), (2, 1), (2, 2)])
    assert board.legal_moves() == moves
