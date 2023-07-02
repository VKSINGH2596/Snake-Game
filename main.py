from turtle import Screen
import time
import snake as s
import food as f

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake-Game")
# Calling the snake game main function for execution
new_snake = s.MySnake(screen)
head_part = screen.turtles()[0]
my_food = f.Food()

game_speed = 0.3
current_score = 0

while True:
    if head_part.xcor() >= 300 or head_part.xcor() <= -300 \
            or head_part.ycor() >= 300 or head_part.ycor() <= -300:
        break
    screen.update()
    time.sleep(game_speed)  # Used to make the loop sleep i.e. make snake movement slow
    if my_food.pos() == head_part.pos():    # Point of collision with food
        my_food.food_collision()            # To randomize the food object again
        new_snake.add_part()

        if game_speed != 0.1:
            game_speed -= 0.1
    else:
        new_snake.snake_movement()

screen.bye()
