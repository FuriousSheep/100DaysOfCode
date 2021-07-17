# import colorgram
import turtle as t
from random import choice

# How we selected the colors
# colors = colorgram.extract('STEAL.jpg', 10)
t.colormode(255)

colorlist = [
    (249, 249, 248),
    (236, 240, 247),
    (241, 247, 244),
    (248, 241, 244),
    (132, 164, 202),
    (227, 150, 100),
    (30, 43, 64),
    (201, 135, 147),
    (165, 59, 47),
    (236, 212, 87)
]

TURTLE_SIZE = 20

screen = t.Screen()
turtle = t.Turtle()
turtle.speed(0)
turtle.hideturtle()
turtle.pensize(20)
turtle.penup()
turtle.goto(-250, 250)
turtle.pendown()
for _ in range(0,10):
    for _ in range(0,10):
        turtle.color(choice(colorlist))
        turtle.dot(20)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
    turtle.penup()
    turtle.backward(500)
    turtle.sety(turtle.ycor() - 50)
    turtle.pendown()


t.exitonclick()