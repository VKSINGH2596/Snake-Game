from turtle import Turtle
X_COR = 600
Y_COR = 750
X_PADDING = 20
Y_PADDING = 150
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.boundary()
        self.penup()
        self.hideturtle()
        self.display_score()

    def boundary(self):
        self.penup()
        self.goto(-(X_COR/2) + X_PADDING, (Y_COR/2) - Y_PADDING)
        self.pendown()
        self.setheading(RIGHT)
        self.forward(X_COR - 2 * X_PADDING)
        self.setheading(DOWN)
        self.forward(Y_COR - Y_PADDING - 20)
        self.setheading(LEFT)
        self.forward(X_COR - 2 * X_PADDING)
        self.setheading(UP)
        self.forward(Y_COR - Y_PADDING - 20)
        self.penup()

    def display_score(self):
        """Displays score"""
        self.goto(0, (Y_COR / 2) - (Y_PADDING / 2))
        self.write(f"Score = {self.score} 🐢", align="center", font=('Courier', 24, 'normal'))

    def score_increase(self):
        """Increases the score"""
        self.score += 1
        self.clear()
        self.boundary()
        self.display_score()

    def game_over(self):
        """Display's Game over message"""
        self.goto(0, 0)
        self.write(f"GAME OVER! 🐍", align="center", font=('Courier', 24, 'normal'))
        self.goto(0, -30)
        self.write(f"Click anywhere on the screen to exit.", align="center", font=('Courier', 8, 'normal'))
