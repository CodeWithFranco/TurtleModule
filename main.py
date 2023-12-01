from turtle import Turtle, Screen
import random

# import turtle as t
ninja_turtle = Turtle()
ninja_turtle.shape("turtle")

colors = ["royal blue", "forest green", "goldenrod", "pale green", "sandy brown"]
direction = [0, 90, 180, 270]
width = [5, 6, 7, 10]

for i in range(500):
    ninja_turtle.color(random.choice(colors))
    ninja_turtle.forward(30)
    ninja_turtle.setheading(random.choice(direction))
    ninja_turtle.pensize(random.choice(width))






screen = Screen()
screen.exitonclick()
