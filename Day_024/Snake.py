import turtle as t
import random as r
import time
import Snake_class as S
import Food
import Score

screen = t.Screen()
screen.bgcolor("#232323")
screen.setup(width=600, height=600)
screen.title("Snake! The Game!")
screen.tracer(0)

#### TEXT ####


def game_lost():
    """Writes up that the game is lost on the screen"""
    lose = t.Turtle()
    lose.penup()
    lose.color("#FAFAFA")
    lose.hideturtle()
    lose.write(
        arg="You lost! Better luck next time =)",
        align="center",
        font=("Arial Black", 20)
    )


def is_food_being_eaten(food, snake):
    """Determines if food is in the head space of the snake"""
    head = snake.head
    lower_x = head.xcor() - 10
    higher_x = head.xcor() + 10
    lower_y = head.ycor() - 10
    higher_y = head.ycor() + 10
    food_in_head_case = \
        food.xcor() >= lower_x and food.xcor() <= higher_x and \
        food.ycor() >= lower_y and food.ycor() <= higher_y
    return food_in_head_case


#### MAIN ####
def main():
    score = Score.Score()
    snake = S.Snake()
    snake.set_listeners(screen)
    food = Food.Food()
    screen.update()
    game_is_on = True
    while game_is_on:
        if snake.is_dead():
            # if snake is dead:
            # reset score
            score.reset()
        # remove all the snake parts,
        # remake a snake
            snake.reset()
        # ask to press a key to play
        snake.move()
        if is_food_being_eaten(food, snake):
            food.place_food()
            snake.grow()
            score.update()
        screen.update()
        time.sleep(0.08)
    game_lost()
    screen.exitonclick()


if __name__ == "__main__":
    main()
