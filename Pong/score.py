from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGN = "center"


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.score_update()
        # self.score_update_r()

    def score_update(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_update()


