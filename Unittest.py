'''Explanation:
setUp Method: Initializes a new TicTacToe game before each test.
test_initial_state: Verifies the initial state of the game.
test_play_valid_move: Ensures that a valid move updates the board and switches the player.
test_play_invalid_move: Ensures that attempting to play on an occupied spot does not change the board or the current player.
test_check_winner_row: Tests a winning scenario in a row.
test_check_winner_column: Tests a winning scenario in a column.
test_check_winner_diagonal: Tests a winning scenario on a diagonal.
test_no_winner: Tests a scenario where no one wins after all spots are filled.'''

import unittest
from TicTacToe import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def test_initial_state(self):
        # Test the initial state of the game
        self.assertEqual(self.game.current_player, 'X')
        self.assertFalse(self.game.game_over)
        self.assertEqual(self.game.board, [['', '', ''], ['', '', ''], ['', '', '']])

    def test_play_valid_move(self):
        # Test making a valid move
        self.game.play(0, 0)
        self.assertEqual(self.game.board[0][0], 'X')
        self.assertEqual(self.game.current_player, 'O')

    def test_play_invalid_move(self):
        # Test making a move on an occupied spot
        self.game.play(0, 0)
        self.game.play(0, 0)
        self.assertEqual(self.game.board[0][0], 'X')
        self.assertEqual(self.game.current_player, 'O')

    def test_check_winner_row(self):
        # Test if the game correctly identifies a win in a row
        self.game.play(0, 0)  # X
        self.game.play(1, 0)  # O
        self.game.play(0, 1)  # X
        self.game.play(1, 1)  # O
        self.game.play(0, 2)  # X - this should win
        self.assertTrue(self.game.game_over)

    def test_check_winner_column(self):
        # Test if the game correctly identifies a win in a column
        self.game.play(0, 0)  # X
        self.game.play(0, 1)  # O
        self.game.play(1, 0)  # X
        self.game.play(1, 1)  # O
        self.game.play(2, 0)  # X - this should win
        self.assertTrue(self.game.game_over)

    def test_check_winner_diagonal(self):
        # Test if the game correctly identifies a win in a diagonal
        self.game.play(0, 0)  # X
        self.game.play(0, 1)  # O
        self.game.play(1, 1)  # X
        self.game.play(0, 2)  # O
        self.game.play(2, 2)  # X - this should win
        self.assertTrue(self.game.game_over)

    def test_no_winner(self):
        # Test if the game correctly identifies that there's no winner
        self.game.play(0, 0)  # X
        self.game.play(0, 1)  # O
        self.game.play(0, 2)  # X
        self.game.play(1, 1)  # O
        self.game.play(1, 0)  # X
        self.game.play(2, 0)  # O
        self.game.play(1, 2)  # X
        self.game.play(2, 2)  # O
        self.game.play(2, 1)  # X
        self.assertFalse(self.game.game_over)
        self.assertEqual(self.game.current_player, 'X')

if __name__ == '__main__':
    unittest.main()

    
