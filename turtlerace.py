from turtle import Turtle
from random import randint

# create four instances of Turtles
dusty = Turtle()
dusty.color('blue')
dusty.shape('turtle')
dusty.penup()
dusty.goto(-160, 100)
dusty.pendown()

taylor = Turtle()
taylor.color('purple')
taylor.shape('turtle')
taylor.penup()
taylor.goto(-160, 70)
taylor.pendown()

lilo = Turtle()
lilo.color('red')
lilo.shape('turtle')
lilo.penup()
lilo.goto(-160, 40)
lilo.pendown()

stitch = Turtle()
stitch.color('green')
stitch.shape('turtle')
stitch.penup()
stitch.goto(-160, 10)
stitch.pendown()

finish_line = Turtle()
finish_line.color('black')
finish_line.shape('arrow')
finish_line.penup()
finish_line.goto(150, 0)
finish_line.pendown()
finish_line.goto(150, 110)

for movement in range(100):
    dusty.forward(randint(1, 5))
    taylor.forward(randint(1, 5))
    lilo.forward(randint(1, 5))
    stitch.forward(randint(1, 5))

