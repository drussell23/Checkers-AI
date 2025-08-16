import unittest
import sys
import os

from checkers.checkers.board import Board
from checkers.checkers.constants import RED, WHITE

class TestBoard(unittest.TestCase):

    def test_initial_piece_count(self):
        """Test that the board is created with the correct number of pieces."""
        board = Board()
        self.assertEqual(board.red_left, 12)
        self.assertEqual(board.white_left, 12)

    def test_initial_king_count(self):
        """Test that the board is created with zero kings."""
        board = Board()
        self.assertEqual(board.red_kings, 0)
        self.assertEqual(board.white_kings, 0)

if __name__ == '__main__':
    unittest.main()