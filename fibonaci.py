import turtle

iterations = 6
coords = [12, 10]

turtle.setworldcoordinates(-coords[0], -coords[1], coords[0], coords[1])
turtle.right(90)
turtle.forward(10)
turtle.left(90)
turtle.speed(0)

def fib (currentNum, nextNum, secondNextNum, i, coords):
    turtle.circle(currentNum * 5, 90)
    turtle.circle(currentNum * 5, -90)
    turtle.setworldcoordinates(-coords[0], -coords[1], coords[0], coords[1])
    for i in range(3):
        turtle.forward(currentNum * 5)
        turtle.left(90)
    turtle.right(90)
    turtle.backward(currentNum * 5)
    turtle.right(90)

    coords[0] *= 1.618
    coords[1] *= 1.618


    if i <= iterations:
        return fib(nextNum, secondNextNum, nextNum + secondNextNum, i + 1, coords)
    else:
        return currentNum

# def draw ():

print(fib(1, 1, 2, 0, coords))