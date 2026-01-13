import turtle
import random
import math

t = turtle.Turtle()
t.width(3)
t.speed(0)

t.hideturtle()

screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(1.0)

radius = 150

for i in range(3600):
    t.color(
        math.sin(math.radians(i))**2,
        math.sin(math.radians(i + 120))**2,
        math.sin(math.radians(i + 240))**2
    )
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.left(1)

    t.circle(radius)
    t.left(1)
    t.right(math.sin(i/10)*23)

turtle.done()
