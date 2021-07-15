from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 310)
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.write(
            f"Score: {self.score}                            High Score: {self.high_score}",
            align="center",
            font=("Arial", 24, "normal"),
        )

    def increase_score(self):
        self.score += 1
        self.updatescore()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.updatescore()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER :-(", align="center", font=("Arial", 24, "normal"))
