from turtle import Turtle, Screen
import turtle

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwords():
    tim.backward(10)


def move_right():
    tim.right(10)


def move_left():
    tim.left(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwords)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(clear, "q")
screen.exitonclick()
