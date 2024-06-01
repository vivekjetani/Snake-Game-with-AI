# Snake Game with AI

This is a classic Snake Game implemented in Python using the `tkinter` library for the graphical user interface. The game includes a toggleable AI mode that allows the snake to play by itself using the A* pathfinding algorithm.

## Features

- Classic snake gameplay
- Dark and light mode toggle
- AI mode toggle
- Keeps track of the highest score

## Requirements

- Python 3
- `Pillow` library for image handling

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/vivekjetani/Snake-Game-with-AI.git
    cd Snake-Game-with-AI
    ```

2. Install the required Python packages:

    ```bash
    pip install pillow
    ```

## Usage

1. Run the game:

    ```bash
    python main.py
    ```

2. Use the arrow keys to control the snake.

3. Toggle dark/light mode by clicking the "Toggle Dark/Light Mode" button.

4. Toggle AI mode by clicking the "Toggle AI" button. In AI mode, the snake will automatically find the shortest path to the food while avoiding its own body.

## How to Play

- The objective of the game is to eat as much food as possible without colliding with the walls or the snake's own body.
- The snake grows longer each time it eats food.
- The game ends if the snake collides with the walls or its own body.
- Use the arrow keys to control the direction of the snake.

## AI Mode

- The AI uses the A* algorithm to find the shortest path to the food.
- The AI mode can be toggled on and off using the "Toggle AI" button.

## Code Overview

- `SnakeGame` class: Main class for the game logic and UI.
- `create_ui`: Sets up the game interface.
- `reset_game`: Resets the game state.
- `place_food`: Places the food at a random location on the grid.
- `handle_keypress`: Handles keypress events for controlling the snake and restarting the game.
- `change_direction`: Changes the direction of the snake based on keypress events.
- `move_snake`: Moves the snake in the current direction and handles game over conditions.
- `update`: Updates the game state and UI.
- `draw_snake`: Draws the snake on the canvas.
- `draw_food`: Draws the food on the canvas.
- `end_game`: Displays the game over message.
- `toggle_mode`: Toggles between dark and light mode.
- `toggle_ai_mode`: Toggles AI mode on and off.
- `ai_move`: Calculates the next move for the snake using the A* algorithm.
- `a_star_search`: Implements the A* pathfinding algorithm.


## Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html): The standard GUI library for Python.
- [Pillow](https://python-pillow.org/): The Python Imaging Library fork used for handling images.
