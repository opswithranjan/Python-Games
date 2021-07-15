from turtle import Turtle, Screen, forward, numinput, right
import turtle
import random

tim = Turtle()
tim.shape("arrow")
colours = ["red", "blue", "yellow", "black", "green", "grey", "brown", "maroon", "red"]


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side)
