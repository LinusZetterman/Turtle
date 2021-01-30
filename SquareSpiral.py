import turtle

turtle.setworldcoordinates(-600, -500, 600, 500)

turtle.speed(0)

for i in range(200):
    turtle.left(90)
    turtle.forward(i * 2)

turtle.exitonclick()
