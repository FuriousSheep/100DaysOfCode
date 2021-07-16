from turtle import Turtle, Screen


def main():
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.color("#00FF00")
    for i in range(0, 50):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()
    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
