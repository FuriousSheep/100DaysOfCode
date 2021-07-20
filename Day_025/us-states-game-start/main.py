import turtle
from typing import Tuple
import pandas
from pandas.core.arrays import string_

HOME_FOLDER = "/home/ioannis/Bureau/PythonCourses/Day_025/us-states-game-start/"

screen = turtle.Screen()
screen.title("USA! USA! USA! USA!")
screen.bgpic(HOME_FOLDER + "blank_states_img.gif")
game_is_on = True

data = pandas.read_csv(HOME_FOLDER + "50_states.csv")

found_states = []
n_found_states = len(found_states)
game_is_on = True

while n_found_states < 50 and game_is_on:
    input = screen.textinput(
        title=f"{n_found_states}/50", prompt="Enter a missing state of the US of A!\n or (exit)")
    if input in data["state"].values and input not in found_states:
        found_states.append(input)
        state = data[data.state == input]
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.shape("circle")
        t.shapesize(0.2, 0.2)
        t.goto(int(state.x), int(state.y))
        t.write(state.state.iloc[0], align="center")
    elif input == "exit":
        game_is_on = False
        print("Here are all the states that you missed!")
        missed_states = data.state
        for state in found_states:
            missed_states = missed_states[missed_states.values != state]
        missed_states.to_csv(HOME_FOLDER + "missed_states.csv")
    n_found_states = len(found_states)
