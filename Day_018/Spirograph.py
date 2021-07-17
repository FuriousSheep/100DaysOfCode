from turtle import Turtle, Screen, colormode
from random import randint


def random_color():
    return (
        randint(0, 255),
        randint(0, 255),
        randint(0, 255)
    )


def main():
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.speed(0)
    colormode(255)
    for _ in range(0, 120):
        timmy.color(random_color())
        timmy.circle(50)
        timmy.left(3)
    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
