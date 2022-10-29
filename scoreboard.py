from turtle import Turtle

POSITIONS = [(40, 270), (-40, 270)]


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('White')
        self.hideturtle()
        self.up()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-40, 250)
        self.write(f"{self.l_score} ", align="center", font=("Arial", 34, "normal"))
        self.goto(40, 250)
        self.write(f"{self.r_score} ", align="center", font=("Arial", 34, "normal"))

    def l_score_update(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_score_update(self):
        self.r_score += 1
        self.update_scoreboard()
