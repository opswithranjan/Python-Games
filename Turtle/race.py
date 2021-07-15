from turtle import Turtle, Screen
import random
import turtle

screen = Screen()
screen.setup(width=500, height=400)
userbet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race?"
)
colors = ["red", "blue", "black", "green", "pink", "orange"]
all_turtle = []
y = -80
is_race_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-240, y)
    new_turtle.pendown()
    all_turtle.append(new_turtle)
    y += 40

if userbet:
    is_race_on = True

while is_race_on:
    for t in all_turtle:
        if t.xcor() > 230:
            winning_color = t.pencolor()
            if userbet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost ! The {winning_color} turtle is the winner!")
            is_race_on = False
        rand_distance = random.randint(1, 10)
        t.forward(rand_distance)

screen.listen()

screen.exitonclick()
