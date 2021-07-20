from turtle import Turtle
from random import choice


BALL_SPEED = 14
UP_RIGHT = 45
UP_LEFT = 135
DOWN_RIGHT = -45
DOWN_LEFT = -135
ANGLES = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.real_heading = self.reset_heading()

    def reset_heading(self):
        headings = ANGLES
        return choice(headings)

    def bar_bounce(self):
        bounces = {UP_RIGHT: UP_LEFT, UP_LEFT: UP_RIGHT,
                   DOWN_RIGHT: DOWN_LEFT, DOWN_LEFT: DOWN_RIGHT}
        self.real_heading = bounces[self.real_heading]

    def tob_bounce(self):
        bounces = {UP_RIGHT: DOWN_RIGHT, UP_LEFT: DOWN_LEFT,
                   DOWN_RIGHT: UP_RIGHT, DOWN_LEFT: UP_LEFT}
        self.real_heading = bounces[self.real_heading]

    def move(self):
        self.setheading(self.real_heading)
        self.forward(BALL_SPEED)
        self.setheading(0)

    def reset(self):
        self.setpos(0, 0)
        self.real_heading = (self.reset_heading())
