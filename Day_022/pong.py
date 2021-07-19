from ball import Ball
from bar import Bar
from turtle import Turtle, Screen
from score import Score


class Pong():
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.screen.setup(height=600, width=600)
        self.ball = Ball()
        self.player_bar = Bar(-260)
        self.player_bar.set_player_listeners(self.screen)
        self.computer_bar = Bar(260)
        self.screen.listen()
        self.player_score = Score(-50)
        self.computer_score = Score(50)
        self.game_on = True
