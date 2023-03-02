import random
import curses

# initialize the game window
screen = curses.initscr()
curses.curs_set(0)
screen_height, screen_width = screen.getmaxyx()
game_window = curses.newwin(screen_height, screen_width, 0, 0)
game_window.keypad(1)
game_window.timeout(100)

# initialize the snake and the food
snake_x = screen_width // 4
snake_y = screen_height // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2],
]
food = [screen_height // 2, screen_width // 2]
game_window.addch(food[0], food[1], curses.ACS_PI)

# initialize the game variables
direction = curses.KEY_RIGHT
score = 0
level = 1
snake_length = 3
level_score = 5

# main game loop
while True:
    next_direction = game_window.getch()
    if next_direction == curses.KEY_RIGHT and direction != curses.KEY_LEFT:
        direction = next_direction
    elif next_direction == curses.KEY_LEFT and direction != curses.KEY_RIGHT:
        direction = next_direction
    elif next_direction == curses.KEY_UP and direction != curses.KEY_DOWN:
        direction = next_direction
    elif next_direction == curses.KEY_DOWN and direction != curses.KEY_UP:
        direction = next_direction

    # move the snake
    new_head = [snake[0][0], snake[0][1]]
    if direction == curses.KEY_RIGHT:
        new_head[1] += 1
    elif direction == curses.KEY_LEFT:
        new_head[1] -= 1
    elif direction == curses.KEY_UP:
        new_head[0] -= 1
    elif direction == curses.KEY_DOWN:
        new_head[0] += 1
    snake.insert(0, new_head)

    # check if the snake hit the wall or itself
    if (
        new_head[0] == 0
        or new_head[0] == screen_height - 1
        or new_head[1] == 0
        or new_head[1] == screen_width - 1
        or new_head in snake[1:]
    ):
        curses.endwin()
        print("Game Over!")
        print(f"Final Score: {score}")
        break

    # check if the snake ate the food
    if new_head == food:
        food = None
        score += 1
        snake_length += 1
        if score >= level_score:
            level += 1
            level_score += 5
            snake_length -= 1
        while food is None:
            new_food = [random.randint(1, screen_height - 2), random.randint(1, screen_width - 2)]
            food = new_food if new_food not in snake else None
        game_window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        game_window.addch(tail[0], tail[1], ' ')

    # update the screen
    game_window.clear()
    game_window.border(0)
    game_window.addstr(0, 2, f"Level: {level}  Score: {score}")
    game_window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
    for i in range(1, len(snake)):
        game_window.addch(snake[i][0], snake[i][1], curses.ACS_BOARD)
    game_window.addch(food[0], food[1], curses.ACS_PI)
    game_window.refresh()

    # level up
    if level == 11:
        curses.endwin()