from turtle import Turtle
import scoreboard as sb
import random as r

DETECTION = 20
X_COR_FOOD_START = -(sb.X_COR/2) + sb.X_PADDING + DETECTION
X_COR_FOOD_STOP = (sb.X_COR/2) - sb.X_PADDING - DETECTION
Y_COR_FOOD_START = -int(sb.Y_COR/2) + 20 + DETECTION
Y_COR_FOOD_STOP = (sb.Y_COR/2) - sb.Y_PADDING - DETECTION


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.goto(r.randint(X_COR_FOOD_START, X_COR_FOOD_STOP), r.randint(Y_COR_FOOD_START, Y_COR_FOOD_STOP))
        print(self.pos())

    def food_collision(self):
        self.goto(r.randint(X_COR_FOOD_START, X_COR_FOOD_STOP), r.randint(Y_COR_FOOD_START, Y_COR_FOOD_STOP))
        print(self.pos())
