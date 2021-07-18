import turtle as t
from random import randint

screen = t.Screen()


def make_turtle(color):
    """Makes a single colored turtle"""
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    return new_turtle


def make_turtles():
    """Makes all them fine turtles"""
    colors = ['green', 'blue', 'purple', 'red', 'orange', 'yellow']
    turtles = []
    for color in colors:
        turtles.append(make_turtle(color))
    return turtles


def setup_turtles(turtles):
    """Places the turtles in their starting position"""
    i = 0
    for turtle in turtles:
        turtle.setpos(20 - screen.window_width()/2, 125 - 50*i)
        i += 1


def winner_is(turtles):
    """Returns the color of the winning turtle if a turtle has won, else returns 'none'"""
    for turtle in turtles:
        if turtle.xcor() > (screen.window_width()/2 - 20):
            return turtle.color()
    return "none"


def main():
    player_bet = screen.textinput(
        title="Make your bet!", prompt="Who's tha fastest turtlez EVAH? plz enter color:")
    turtles = make_turtles()
    setup_turtles(turtles=turtles)
    while winner_is(turtles) == 'none':
        for racer in turtles:
            racer.forward(randint(5, 50))
    if player_bet == winner_is(turtles)[0]:
        print("Good job! You won!")
    else:
        print("Better luck next time!")
    screen.bye()


if __name__ == "__main__":
    main()
