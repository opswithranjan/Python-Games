from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_on = True

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect Collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with boundary
    if (
        snake.head.xcor() > 350
        or snake.head.xcor() < -350
        or snake.head.ycor() > 320
        or snake.head.ycor() < -320
    ):
        score.reset()
        snake.reset()

    # Detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()

screen.exitonclick()
