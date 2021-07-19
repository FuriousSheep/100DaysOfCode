from turtle import Turtle
from random import randint

CASE_SIZE = 20


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green", "green")
        self.shape("circle")
        self.place_food()

    def place_food(self):
        self.setx(randint(-13, 13) * CASE_SIZE)
        self.sety(randint(-13, 13) * CASE_SIZE)
