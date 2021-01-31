import turtle
import random

turtle.setworldcoordinates(-75, 0, 75, 125)
turtle.speed(0)
turtle.left(90)


def forward (length, i):

	turtle.forward(length)
	turtle.left(degrees)
	tree(length, i)

def backward (length, i):
	turtle.color(random.randint(0, 10)/10, random.randint(0, 10)/10, random.randint(0, 10)/10)

	turtle.right(degrees*change)
	turtle.backward(length/change)
	turtle.right(2 * degrees)
	turtle.forward(length/change)
	turtle.backward(length/change)
	turtle.left(degrees)
	turtle.backward(length/change)
	tree(length, i)

length = 30
iterations = 5
i = 0
isForward = True
degrees = 41
change = 1.25


def tree (length, i):

	if i <= iterations:
		return forward(length / change, i + 1)
	else:
		return backward(length * change, i - 1)


tree(length, i)

turtle.exitonclick()
