from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_CAR_XCOR = 310
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(1, 2)
        car.color(choice(COLORS))
        car.penup()
        starting_y = randint(-260, 260)
        car.goto(STARTING_CAR_XCOR, starting_y)
        self.cars.append(car)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT

    def move_car(self, car):
        car.goto(car.xcor() - self.car_speed, car.ycor())

    def move_cars(self):
        for car in self.cars:
            self.move_car(car)

    def has_accident_happened(self, turtle):
        if not self.cars == []:
            for car in self.cars:
                x_distance = abs(turtle.xcor() - car.xcor())
                y_distance = abs(turtle.ycor() - car.ycor())
                if x_distance < 40 and y_distance < 20:
                    return True
        return False
