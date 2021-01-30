import turtle

turtle.setworldcoordinates(-600, -500, 600, 500)

turtle.penup()

turtle.speed(0)
turtle.hideturtle()
turtle.goto(-800, -600)

turtle.pendown()

x = 90

for i in range(200):
    turtle.forward(1599)
    turtle.left(x)
    turtle.forward(5)
    turtle.left(x)

    x *= -1

turtle.exitonclick()