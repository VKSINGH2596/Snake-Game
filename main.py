from turtle import Turtle, Screen

# Setting up the game screen
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake-Game")

# Creating the Snake body
initial_length = 3
body_pieces = [Turtle("square") for _ in range(initial_length)]

my_screen.exitonclick()