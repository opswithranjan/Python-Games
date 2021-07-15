import turtle as t
import random

screen = t.Screen

t.colormode(255)
tim = t.Turtle()
tim.speed("fast")
while True:
    tim.hideturtle()
    tim.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    tim.circle(100)
    tim.tilt(45)
    tim.tiltangle()
