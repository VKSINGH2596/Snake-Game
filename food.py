from turtle import Turtle
import random as r


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.goto(r.randint(-280, 280), r.randint(-280, 280))
