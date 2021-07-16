from turtle import Turtle, Screen


def main():
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.color("#00FF00")
    for i in range(0, 4):
        timmy.forward(100)
        timmy.right(90)
    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
