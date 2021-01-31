import time
import turtle

x = 600
y = 500

length = 30

for i in range(30):
    turtle.setworldcoordinates(-x, -y, x, y)
    turtle.left(90)
    turtle.forward(length)
    for j in range(3):
        turtle.right(90)
        turtle.forward(length)
    turtle.left(180)
    turtle.forward(length)
    length *= 2

    x += length/2
    y += length/2

    time.sleep(0.5)

    x += length/2
    y += length/2