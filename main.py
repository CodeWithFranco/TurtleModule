from turtle import Turtle, Screen

# import turtle as t
ninja_turtle = Turtle()
ninja_turtle.shape("turtle")

"""
0deg = west
45deg = south east
90deg = south
135deg = southwest
180deg = west
225deg = northwest
270deg =  north
"""


def triangle():
    ninja_turtle.color("blue")
    for i in range(3):
        ninja_turtle.forward(100)
        ninja_turtle.right(120)


def square():
    ninja_turtle.color("gray")
    for i in range(4):
        ninja_turtle.forward(100)
        ninja_turtle.right(90)


def pentagon():
    ninja_turtle.color("green")
    for i in range(5):
        ninja_turtle.forward(100)
        ninja_turtle.right(360 / 5)


def hexagon():
    ninja_turtle.color("red")
    for i in range(6):
        ninja_turtle.forward(100)
        ninja_turtle.right(360 / 6)


def heptagon():
    ninja_turtle.color("pink")
    for i in range(7):
        ninja_turtle.forward(100)
        ninja_turtle.right(360 / 7)


def octagon():
    ninja_turtle.color("purple")
    for i in range(8):
        ninja_turtle.forward(100)
        ninja_turtle.right(360 / 8)


def nonagon():
    ninja_turtle.color('maroon')
    for i in range(9):
        ninja_turtle.forward(100)
        ninja_turtle.right(360 / 9)


def decagon():
    ninja_turtle.color("green")
    for i in range(10):
        ninja_turtle.forward(100)
        ninja_turtle.right(360 / 10)


triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()

screen = Screen()
screen.exitonclick()
