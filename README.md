# Snake Game
This is a simple implementation of the classic Snake game in Python using the curses library. The game window has a border, and the snake is represented by a solid block for the head and hollow blocks for the body segments. The game continues indefinitely, with no limit on the score.

[![Demo Video](https://raw.githubusercontent.com/idrisschebak/snake/main/assets/demo.gif)](https://raw.githubusercontent.com/idrisschebak/snake/main/assets/demo.gif)


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

clone this repo to your local machine using
    
 ``` git clone https://github.com/idrisschebak/snake ```

Navigate to the cloned repository in the terminal window using the cd command.

Run the game with the command python `python snake_game.py`.

### 💡 Reporting Bugs and Contributing
If you encounter any bugs or would like to suggest new features, please create an issue on the GitHub repository. Contributions are also welcome! If you would like to contribute to Kitsec, please create a pull request on the GitHub repository.

### 🔖 License
Kitsec is licensed under the MIT License.