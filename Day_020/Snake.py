import turtle as t
import random as r
import time
import Snake_class as S

screen = t.Screen()
screen.bgcolor("#232323")
screen.setup(width=600, height=600)
screen.title("Snake! The Game!")
screen.tracer(0)

#### TEXT ####


def setup_score():
    """Writes up the initial score on the screen"""
    score = t.Turtle()
    score.penup()
    score.hideturtle()
    score.color("#FAFAFA")
    score.goto(0, screen.window_height()/2 - 40)
    score.write("Score : 0", align="center", font=("Arial Black", 20))
    return score


def game_lost():
    """Writes up that the game is lost on the screen"""
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
    """Changes the score writing to show the updated score"""
    score.clear()
    score.write(f"Score : {points}", align="center", font=("Arial Black", 20))


#### SNAKE CONTROL ####


#### MAIN ####
def main():
    # score = setup_score()
    snake = S.Snake()
    snake.set_listeners(screen)
    screen.update()
    while not snake.is_dead():
        snake.move()
        screen.update()
        time.sleep(0.15)

    # game_lost()

    screen.exitonclick()


if __name__ == "__main__":
    main()
