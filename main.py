import turtle
from turtle import Turtle, Screen

Jimmy = Turtle()
Jimmy.shape("turtle")
Jimmy.color("blue")


key_mappings = {
    "w": lambda: Jimmy.forward(10),
    "a": lambda: Jimmy.left(90),
    "d": lambda: Jimmy.right(90),
    "s": lambda: Jimmy.left(180),
}


screen = Screen()
screen.listen()

for key, function in key_mappings.items():
    screen.onkey(function, key)

turtle.done()
