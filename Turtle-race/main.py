import random
import turtle
from turtle import Turtle, Screen
import random

is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make your bet",
                 prompt="Which turtle will win the race? Enter your bet: ")
colors = ["green", "blue", "red", "purple", "yellow", "orange"]
y_pos = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for t in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[t])
    new_turtle.color(colors[t])
    all_turtles.append(new_turtle)


if user_bet:
    is_on = True

while is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_on = False
            winer = turtle.pencolor()
            if winer == user_bet:
                print(f"You won! The winner is {winer} turtle")
            else:
                print(f"You lost! The winner is {winer} turtle")

        random_fwd = random.randint(0, 12)
        turtle.forward(random_fwd)

screen.exitonclick()
