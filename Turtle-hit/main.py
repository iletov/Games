import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Race")
screen.tracer(0)

# TODO 1 - create turtle player
mike = Player()

# TODO 2 - create cars(h20/w40) randomly generated (no cars in the top and bottom 50px)
car = CarManager()

# TODO 5 - create a scoreboard
score = Scoreboard()

screen.listen()
screen.onkeypress(mike.move_up, "Up")
screen.onkeypress(mike.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    # TODO 3 - detect collide with car and game over
    for c in car.all_cars:
        if c.distance(mike) < 15:
            game_is_on = False
            score.game_over()

    # TODO 4 - detect when the turtle has reached the top and start from bottom
    if mike.cross():
        mike.start_over()
        car.increase_speed()
        score.leve_up()

screen.exitonclick()