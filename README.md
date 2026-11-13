# Mr. Mantis’s Garden Game

A garden-themed tic-tac-toe game built with Python and Pygame. You play as the ladybugs against a computer opponent that plays as the scarabs.

## Run locally

From the project folder, run:

```bash
python -m pip install pygame
python main.py
```

## How it works

- `main.py` handles mouse input and displays the board, sprites, and scoreboard.
- `TTTbackend.py` manages the board state, validates moves, and checks for wins and ties.
- The computer looks for a winning move first, then tries to block the player. Otherwise, it favors the center or picks an open square.
