from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 350)
        self.scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def print_game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))

    def scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
