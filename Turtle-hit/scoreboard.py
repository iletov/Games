from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto((-260, 250))
        self.written()

    def written(self):
        self.write(f"Leve: {self.level}", align="left", font=FONT)

    def leve_up(self):
        self.clear()
        self.level += 1
        self.written()

    def game_over(self):
        self.goto((0,0))
        self.write("GAME OVER", align="center", font=FONT)


