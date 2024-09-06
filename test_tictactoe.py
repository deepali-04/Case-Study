import unittest
from tictactoe import check_winner  # Import the function from your main file

class TestTicTacToe(unittest.TestCase):
    def test_check_winner(self):
        board = [
            ["X", "X", "X"],
            [" ", "O", " "],
            ["O", " ", " "]
        ]
        self.assertTrue(check_winner(board, "X"))
        self.assertFalse(check_winner(board, "O"))

    def test_draw(self):
        board = [
            ["X", "O", "X"],
            ["X", "X", "O"],
            ["O", "X", "O"]
        ]
        self.assertFalse(check_winner(board, "X"))
        self.assertFalse(check_winner(board, "O"))

if __name__ == "__main__":
    unittest.main()
