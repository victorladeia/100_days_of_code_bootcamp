from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 24, "normal")


class Scoreboard(Turtle):

    def __int__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_player1 = 0
        self.score_player2 = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_player1, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_player2, align="center", font=("Courier", 80, "normal"))

    def player1_point(self):
        self.score_player1 += 1
        self.update_scoreboard()

    def player2_point(self):
        self.score_player2 += 1
        self.update_scoreboard()
