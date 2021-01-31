import turtle

turtle.speed(0)

iterations = 5
angle = 35
isForward = 1

turtle.pensize(1)
turtle.setworldcoordinates(-150, 0, 150, 250)

turtle.left(90)

len = 40


def branch(pos, len, i, isForward):
    if isForward:
        turtle.forward(len)
        turtle.left(angle)
        print("forward")
    else:
        print("backward")
        turtle.color((1, 0, 0))
        turtle.backward(len/1.25)
        turtle.color((0, 1, 0))
        turtle.right(2 * angle)
        turtle.forward(len/1.25)
        turtle.backward(len/1.25)
        turtle.left(angle)
        turtle.color((0, 0, 1))
        turtle.backward(len)
        i += 1

    if i <= iterations:
        return branch(turtle.position(), len * 0.8, i + 1, 1)
    else:
        turtle.right(angle)
        return branch(turtle.position(), len * 1.25, i - 1, 0)


turtle.forward(100)
branch(turtle.position(), len, 0, isForward)

turtle.exitonclick()
