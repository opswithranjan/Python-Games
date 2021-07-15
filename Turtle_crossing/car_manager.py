from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
Y = [200, 170, 140, 110, 80, 50, 20, -10, -40, -70, -100, -130, -160, -190]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.generate_car()

    def generate_car(self):
        rand_num = random.randint(0, 6)
        if rand_num == 6:
            rand_y = random.choice(Y)
            car = Turtle("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(280, rand_y)
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.ycor())
            if car.xcor() == -280:
                car.goto(280, car.ycor())
            # or you can use car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
