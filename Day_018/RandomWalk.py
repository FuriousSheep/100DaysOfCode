from turtle import Turtle, Screen
from random import choice


def main():
    teddy = Turtle()
    teddy.shape("turtle")
    teddy.color("#00FF00")

    timmy = Turtle()
    timmy.shape("turtle")
    timmy.color("#0000FF")

    terry = Turtle()
    terry.shape("turtle")
    terry.color("#FF0000")

    timmy.speed(0)
    teddy.speed(0)
    terry.speed(0)

    moves = [0, 90, 180, 270]
    for _ in range(0, 100):
        timmy.forward(10)
        timmy.right(choice(moves))
        teddy.forward(10)
        teddy.right(choice(moves))
        terry.forward(10)
        terry.right(choice(moves))
    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
