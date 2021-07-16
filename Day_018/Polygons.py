from turtle import Turtle, Screen


def main():
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.color("#00FF00")
    colors = [
        "#001100",
        "#002200",
        "#003300",
        "#004400",
        "#005500",
        "#006600",
        "#007700",
        "#008800",
        "#009900",
        "#00AA00"
    ]

    n_sides = 3
    for _ in range(3, 11):
        for _ in range(0, n_sides):
            timmy.forward(100)
            timmy.right(360/n_sides)
        timmy.color(colors[n_sides-3])
        n_sides += 1

    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
