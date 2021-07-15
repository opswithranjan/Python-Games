import time
from turtle import Turtle, Screen, position
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


rpaddle = Paddle((-360, 0))
lpaddle = Paddle((360, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(rpaddle.up, "w")
screen.onkey(rpaddle.down, "s")
screen.onkey(lpaddle.up, "Up")
screen.onkey(lpaddle.down, "Down")


game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # When ball touches uper or lower boundary
    if ball.ycor() == -290 or ball.ycor() == 290:
        ball.bounce_y()

    # when ball touches paddle
    if (
        ball.distance(rpaddle) < 30
        and ball.xcor() < 360
        or ball.distance(lpaddle) < 30
        and ball.xcor() > -360
    ):
        ball.bounce_x()

    # rpaddle misses ball
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.resetposition()

    # lpaddle misses ball
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.resetposition()


screen.exitonclick()
