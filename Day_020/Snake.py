import turtle as t
import random as r

CASE_SIZE = 20
screen = t.Screen()
screen.bgcolor("#232323")
screen.listen()


def setup_score():
    score = t.Turtle()
    score.penup()
    score.hideturtle()
    score.color("#FAFAFA")
    score.goto(0, screen.window_height()/2 - 40)
    score.write("Score : 0", align="center", font=("Arial Black", 20))
    return score


def game_lost():
    lose = t.Turtle()
    lose.penup()
    lose.color("#FAFAFA")
    lose.hideturtle()
    lose.write(
        arg="You lost! Better luck next time =(",
        align="center",
        font=("Arial Black", 20)
    )


def update_score(score, points):
    score.clear()
    score.write(f"Score : {points}", align="center", font=("Arial Black", 20))


def make_snake():
    snake = []
    for i in range(0, 3):
        snake_part = t.Turtle()
        snake_part.shape("square")
        snake_part.speed(0)
        snake_part.penup()
        snake_part.color("#FAFAFA", "#232323")
        snake_part.setx(snake_part.xcor() - CASE_SIZE * i)
        snake.append(snake_part)
    return snake


def main():
    score = setup_score()
    make_snake()
    # game_lost()
    screen.exitonclick()


if __name__ == "__main__":
    main()
