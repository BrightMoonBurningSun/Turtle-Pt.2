import turtle
from random import*
turtle.color('red')
turtle.shape('turtle')

for i in range(20):
    turtle.forward(randrange(10, 50))
    turtle.right(randrange(1, 180))
    turtle.backward(randrange(10, 50))
    turtle.left(randrange(1, 180))
