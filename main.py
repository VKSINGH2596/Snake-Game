from turtle import Screen
import time

import food
import snake as s
import food as f
import scoreboard as sb

screen = Screen()
GAME_RUN = True
screen.setup(width=sb.X_COR, height=sb.Y_COR)
screen.bgcolor("black")
screen.title("Snake-Game")
# Calling the snake game main function for execution
new_snake = s.MySnake(screen)
head_part = screen.turtles()[0]
my_food = f.Food()

game_speed = 0.3
scoreboard = sb.ScoreBoard()

while GAME_RUN:
    if head_part.xcor() >= (sb.X_COR / 2) - sb.X_PADDING or head_part.xcor() <= -(sb.X_COR / 2) + sb.X_PADDING\
            or head_part.ycor() >= (sb.Y_COR / 2) - sb.Y_PADDING \
            or head_part.ycor() <= -(sb.Y_COR / 2) + 20 + food.DETECTION:
        scoreboard.game_over()  # Wall collision
        GAME_RUN = False
        continue

    screen.update()
    time.sleep(game_speed)  # Used to make the loop sleep i.e. make snake movement slow

    if head_part.distance(my_food) < food.DETECTION:    # Point of collision with food
        my_food.food_collision()            # To randomize the food object again
        new_snake.add_part()
        scoreboard.score_increase()

        if game_speed > 0.1:
            game_speed -= 0.1
    else:
        new_snake.snake_movement()

    for part in new_snake.fetch_snake():                # Tail collision
        if part == head_part:
            pass
        elif head_part.distance(part) < 10:
            scoreboard.game_over()
            GAME_RUN = False
            break

screen.exitonclick()
