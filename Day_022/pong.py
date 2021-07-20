from ball import Ball
from bar import Bar
from turtle import Turtle, Screen, distance, forward
from score import Score


class Pong():
    def __init__(self):
        self.screen_height = 600
        self.screen_width = 600
        self.bar_offset = 40
        self.score_offset = 50
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.screen.setup(height=self.screen_height, width=self.screen_width)
        self.ball = Ball()
        self.player_bar = Bar(-self.screen_width/2 + self.bar_offset)
        self.player_bar.set_player_listeners(self.screen)
        self.computer_bar = Bar(self.screen_width/2 - self.bar_offset)
        self.screen.listen()
        self.player_score = Score(-self.score_offset)
        self.computer_score = Score(self.score_offset)
        self.paint_the_field()

    def game_on(self):
        return self.player_score.score < 10 and self.computer_score.score < 10

    def ball_hits_bar(self):
        x_to_pbar = abs(self.ball.xcor() - self.player_bar.xcor())
        y_to_pbar = abs(self.ball.ycor() - self.player_bar.ycor())
        x_to_cbar = abs(self.ball.xcor() - self.computer_bar.xcor())
        y_to_cbar = abs(self.ball.ycor() - self.computer_bar.ycor())
        hits_pbar = x_to_pbar < 15 and y_to_pbar < 25
        hits_cbar = x_to_cbar < 15 and y_to_cbar < 25
        return hits_cbar or hits_pbar

    def ball_hits_top_or_bot(self):
        y_to_top = abs(self.ball.ycor() - 200)
        y_to_bot = self.ball.ycor() + 200
        hits_top = y_to_top < 10
        hits_bot = y_to_bot < 10
        return hits_top or hits_bot

    def computer_marks(self):
        return self.ball.xcor() < -280

    def player_marks(self):
        return self.ball.xcor() > 280

    def paint_the_field(self):
        brush = Turtle()
        brush.penup()
        brush.hideturtle()
        brush.speed("fastest")
        brush.goto(0, -200)
        brush.pendown()
        brush.pensize(5)
        brush.pencolor("white")
        brush.setheading(90)
        for _ in range(0, 11):
            brush.forward(19)
            brush.penup()
            brush.forward(19)
            brush.pendown()
        brush.penup()
        brush.goto(-280, 210)
        brush.pendown()
        brush.goto(280, 210)
        brush.penup()
        brush.goto(280, -210)
        brush.pendown()
        brush.goto(-280, -210)
        brush.penup()
