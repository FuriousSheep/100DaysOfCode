from pong import Pong
from turtle import Screen, Turtle, reset
from ball import Ball
from time import sleep
from bar import Bar


def main():
    pong = Pong()

    while pong.game_on():
        # Check if the ball hits anything, and flip its direction if it does
        if pong.ball_hits_bar():
            pong.ball.bar_bounce()
        if pong.ball_hits_top_or_bot():
            pong.ball.tob_bounce()
        # move the ball
        pong.ball.move()
        # move the computer bar to block the ball
        pong.computer_bar.update_direction(pong.ball)
        pong.computer_bar.computer_move()
        # score points if there is one
        # reset the ball if there is a point
        if pong.player_marks():
            pong.player_score.update_score()
            pong.ball.reset()
        elif pong.computer_marks():
            pong.computer_score.update_score()
            pong.ball.reset()
        # show what happened
        pong.screen.update()
        sleep(0.04)
    # Show the winner

    pong.screen.exitonclick()


if __name__ == "__main__":
    main()
