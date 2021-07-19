from turtle import Turtle


class Bar(Turtle):
    def __init__(self, xpos=-260):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(4, 1)
        self.setx(xpos)
        self.direction = "up"

    def up(self):
        self.sety(self.ycor() + 10)

    def down(self):
        self.sety(self.ycor() - 10)

    def set_player_listeners(self, screen):
        screen.onkey(key="Up", fun=self.up)
        screen.onkey(key="Down", fun=self.down)

    def computer_move(self):
        moves = {
            'up': self.up,
            'down': self.down
        }
        moves[self.direction]()

    def update_direction(self, ball):
        if ball.ycor() > self.ycor():
            self.direction = 'up'
        else:
            self.direction = 'down'
