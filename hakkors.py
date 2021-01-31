import turtle

iterations = 6

turtle.setworldcoordinates(-600, -500, 600, 500)
turtle.left(90)
turtle.forward(10)
turtle.right(90)

def fib (currentNum, nextNum, secondNextNum, i):
    for i in range(3):
        turtle.forward(currentNum*10)
        turtle.right(90)
    turtle.left(90)
    turtle.backward(currentNum*10)
    turtle.right(90)
    if i <= iterations:
        return fib(nextNum, secondNextNum, nextNum + secondNextNum, i + 1)
    else:
        return currentNum

# def draw ():

print(fib(1, 1, 2, 0))