import turtle as t
import random as r
import time

CASE_SIZE = 20
screen = t.Screen()
screen.bgcolor("#232323")
screen.setup(width=600, height=600)
screen.title("Snake! The Game!")
screen.tracer(0)
# screen.listen()

#### TEXT ####


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


#### SNAKE CONTROL ####


def make_snake_part():
    snake_part = t.Turtle()
    snake_part.shape("square")
    # snake_part.speed(0)
    snake_part.penup()
    snake_part.color("#FAFAFA", "#232323")
    return snake_part


def make_snake():
    snake = []
    for i in range(0, 3):
        snake_part = make_snake_part()
        snake_part.setx(snake_part.xcor() - CASE_SIZE * i)
        snake.append(snake_part)
    return snake


def face_north(snake_part):
    snake_part.setheading(90)


def face_south(snake_part):
    snake_part.setheading(270)


def face_east(snake_part):
    snake_part.setheading(0)


def face_west(snake_part):
    snake_part.setheading(180)


def move_snake_part(snake_part):
    snake_part.forward(20)


def move_snake(snake):
    for snake_part in snake:
        move_snake_part(snake_part)

#### MAIN ####


def main():
    # score = setup_score()
    snake = make_snake()
    screen.update()
    while True:
        move_snake(snake)
        screen.update()
        time.sleep(0.5)

    # game_lost()

    screen.exitonclick()


if __name__ == "__main__":
    main()
