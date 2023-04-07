import turtle
import random

colors = turtle.colormode(255)
color_list = []
for r in range(0, 256, 10):
    for g in range(0, 256, 10):
        for b in range(0, 256, 10):
            color_list.append((r,g,b))

ninja = turtle.Turtle()

ninja.speed(10000)

for i in range(180):
    color = random.choice(color_list)
    ninja.pencolor(color)

    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(1.5)

turtle.done()
