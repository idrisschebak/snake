# Snake Game
This is a simple implementation of the classic Snake game in Python using the curses library. The game window has a border, and the snake is represented by a solid block for the head and hollow blocks for the body segments. The game continues indefinitely, with no limit on the score.

### 🃏 How to Play
The player controls a snake that moves around the game window, eating food and growing longer with each food pellet consumed. The goal is to score as many points as possible without running into the walls or the snake's own body.

The game can be played using the arrow keys: up, down, left, and right. The snake moves in the direction of the last arrow key pressed. If a new arrow key is pressed that is the opposite of the current direction (e.g., left when the snake is moving right), the snake will not change direction until a valid key is pressed.

Each food pellet eaten by the snake increases the player's score by one point. The snake also gets longer with each pellet consumed. Once the score reaches a certain threshold, the player advances to the next level, and the snake length is reduced by one segment.

If the snake collides with a wall or its own body, the game is over, and the final score is displayed.

### 🕹️ Controls

Up arrow key: move the snake up

Down arrow key: move the snake down

Left arrow key: move the snake left

Right arrow key: move the snake right

### 💾 Installation

Clone this repository to your local machine.

Install the curses library if you don't already have it installed. In a terminal window, run `pip install windows-curses` on Windows or `pip install curses on Linux/Mac`.

Navigate to the cloned repository in the terminal window.

Run the game with the command python `snake_game.py`.