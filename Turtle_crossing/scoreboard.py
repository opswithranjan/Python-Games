from turtle import Turtle, write

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(
            f"Score: {self.score}", align="center", font=("Couries", 30, "normal")
        )
        self.goto(0, 0)

    def point(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.write("Game Over", align="center", font=("Couries", 80, "normal"))
