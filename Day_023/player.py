from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.color("green")
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def has_crossed_finishline(self):
        return self.ycor() > FINISH_LINE_Y

    def reset(self):
        self.goto(STARTING_POSITION)

    def set_listener(self, screen):
        screen.onkey(key="Up", fun=self.move)
