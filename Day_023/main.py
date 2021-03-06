import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
player.set_listener(screen=screen)
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()

while not car_manager.has_accident_happened(turtle=player):
    if randint(0, 7) == 7:
        car_manager.make_car()
    car_manager.move_cars()
    if player.has_crossed_finishline():
        scoreboard.update_score()
        car_manager.increase_car_speed()
        player.reset()
    time.sleep(0.1)
    screen.update()
scoreboard.game_over()
screen.exitonclick()
