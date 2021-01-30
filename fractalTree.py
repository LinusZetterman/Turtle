import turtle

turtle.speed(0)

iterations = 5
angle = 35
isForward = 1

turtle.setworldcoordinates(-600, 0, 600, 1000)

turtle.left(90)

len = 40

def branch(pos, len, i, isForward):
    if isForward:
        turtle.forward(len)
        turtle.left(angle)
    else:
        turtle.backward(len)
        turtle.right(2 * angle)
        turtle.forward(len)
        i += 1


    if i <= iterations:
        return branch(turtle.position(), len * 0.8, i + 1, 1)
    else:
        return branch(turtle.position(), len * 1.25, i - 1, 0)

turtle.forward(100)
branch(turtle.position(), len, 0, isForward)

turtle.exitonclick()