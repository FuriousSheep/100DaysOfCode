import turtle as t

jim = t.Turtle()
jim.shape("turtle")
screen = t.Screen()


def go_fd():
    jim.forward(5)


def go_bw():
    jim.backward(5)


def turn_right():
    jim.right(5)


def turn_left():
    jim.left(5)


def clear():
    screen.reset()


def main():
    screen.listen()
    screen.onkey(go_fd, "w")
    screen.onkey(go_bw, "s")
    screen.onkey(turn_left, "a")
    screen.onkey(turn_right, "d")
    screen.onkey(clear, 'c')
    screen.exitonclick()


if __name__ == "__main__":
    main()
