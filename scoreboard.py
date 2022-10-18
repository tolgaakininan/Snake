from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open ("highscoredata.txt") as data:
            self.highscore=int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 350)
        self.scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscoredata.txt",mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0

        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, Highscore: {self.highscore}", align="center", font=("Arial", 24, "normal"))
