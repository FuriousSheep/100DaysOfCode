from turtle import Turtle, Screen, colormode
from random import randint, choice


def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def main():
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.speed(0)
    timmy.pensize(20)
    colormode(255)
    timmy.color(random_color())
    for _ in range(0, 100):
        timmy.forward(20)
        timmy.right(choice([0, 90, 180, 270]))
        timmy.color(random_color())

    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
