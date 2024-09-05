# Overview

This project is a simple implementation of the classic TicTacToe game using Python's tkinter library for the graphical user interface (GUI). The game allows two players to play against each other on a 3x3 grid, where one player is 'X' and the other is 'O'. The objective of the game is to get three of your marks in a row (horizontally, vertically, or diagonally) before your opponent does.

## Installation

To run this project, you need Python installed on your system. The project has no external dependencies, but uses Python's standard libraries, including unittest for testing.

#### Clone the Repository
```bash
git clone https://github.com/deepali-04/Case-Study.git
cd Case-Study
```
#### Run the Game
```bash
python TicTacToe.py
```

#### Run Unit Tests
```bash
python -m unittest test_tictactoe.py
```

## Files

TicTacToe.py: Contains the main game logic and GUI implementation.


test_tictactoe.py: Contains the unit tests for the TicTacToe class.

## Unit Tests

The project includes a set of unit tests to verify the core game logic:

test_initial_state: Verifies the initial state of the game.

test_play_valid_move: Ensures that a valid move updates the board and switches the player.

test_play_invalid_move: Ensures that attempting to play on an occupied spot does not change the board or the current player.

test_check_winner_row: Tests a winning scenario in a row.

test_check_winner_column: Tests a winning scenario in a column.

test_check_winner_diagonal: Tests a winning scenario on a diagonal.

test_no_winner: Tests a scenario where no one wins after all spots are filled.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
