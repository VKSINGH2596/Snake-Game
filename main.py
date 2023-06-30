from turtle import Turtle, Screen

# Setting up the game screen
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake-Game")

class Snake:
    def __init__(self, current_screen, current_turtle):
        self.current_screen = current_screen
        self.my_turtle = current_turtle

    def move_left(self):
        self.my_turtle.tiltangle(90)

    def move_right(self):
        """Ti the turtle back by 10 steps"""
        self.my_turtle.tiltangle(-90)

    def snake_body(self):
        # Creating the Snake body
        initial_length = 3
        x_value = 0
        y_value = 0
        for _ in range(initial_length):
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.setpos(x_value, y_value)
            x_value -= 20


my_screen.exitonclick()