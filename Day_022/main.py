from pong import Pong
from turtle import Screen, Turtle, reset
from ball import Ball
from time import sleep
from bar import Bar


def main():
    pong = Pong()
    game_on = True

    while game_on:
        pong.ball.move()
        pong.screen.update()
        pong.computer_bar.update_direction(pong.ball)
        pong.computer_bar.computer_move()
        if pong.ball.is_out_of_bounds():
            pong.player_score.update_score()
            pong.ball.reset()
        sleep(0.1)

    pong.screen.exitonclick()


if __name__ == "__main__":
    main()
