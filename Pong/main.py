from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# TODO 1 Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


# TODO 2 create and move paddle
right_paddle = Paddle((350, 0))

# TODO 3 create second paddle
left_paddle = Paddle((-350, 0))

# TODO 4 create the ball and make it move
ball = Ball()

# TODO 8 create the score board score
score_l = Score((-120, 260))
score_r = Score((120, 260))

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # TODO 5 detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO 6 detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # TODO 7 detect when paddle misses and increase score
    if ball.xcor() > 380:
        score_l.increase_score()
        ball.reset_ball()

    if ball.xcor() < -380:
        score_r.increase_score()
        ball.reset_ball()

screen.exitonclick()