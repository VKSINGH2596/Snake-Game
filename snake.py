from turtle import Turtle, Screen
import time


class MySnake:
    def __init__(self):
        """Setting up the game screen and initial snake body."""
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake-Game")
        # Creating the Snake body
        x_value = 0
        y_value = 0
        self.screen.tracer(1)
        for _ in range(3):
            new_part = Turtle("square")
            new_part.color("white")
            new_part.penup()
            new_part.setpos(x_value, y_value)
            x_value -= 20

    def move_up(self):
        """To turn the set the heading head part to north."""
        self.screen.turtles()[0].setheading(90)

    def move_down(self):
        """To turn the set the heading head part to south."""
        self.screen.turtles()[0].setheading(270)

    def move_left(self):
        """To turn the set the heading head part to east."""
        self.screen.turtles()[0].setheading(180)

    def move_right(self):
        """To turn the set the heading head part to west."""
        self.screen.turtles()[0].setheading(0)

    def snake_movement(self):
        """Method responsible for snake body movement."""
        self.screen.listen()
        head_part = self.screen.turtles()[0]
        self.screen.onkeypress(self.move_up, "Up")
        self.screen.onkeypress(self.move_down, "Down")
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_right, "Right")
        while True:
            if head_part.xcor() >= 300 or head_part.xcor() <= -300 \
                    or head_part.ycor() >= 300 or head_part.ycor() <= -300:
                break
            self.screen.update()
            time.sleep(0.1)
            turtle_list = self.screen.turtles()
            for index in range(len(turtle_list) - 1, 0, -1):
                pos_of_next_element = turtle_list[index - 1].pos()
                turtle_list[index].setpos(pos_of_next_element)
            turtle_list[0].forward(20)

        self.screen.bye()

