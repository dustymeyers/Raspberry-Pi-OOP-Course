from turtle import Turtle

# create four instances of Turtles
dusty = Turtle()
dusty.color('blue')
dusty.shape('turtle')

taylor = Turtle()
taylor.color('purple')
taylor.shape('turtle')

lilo = Turtle()
lilo.color('red')
lilo.shape('turtle')

stitch = Turtle()
stitch.color('green')
stitch.shape('turtle')

# Put each turtle in its starting places
dusty.penup()
dusty.goto(-160, 100)
dusty.pendown()

taylor.penup()
taylor.goto(-160, 70)
taylor.pendown()

lilo.penup()
lilo.goto(-160, 40)
lilo.pendown()

stitch.penup()
stitch.goto(-160, 10)
stitch.pendown()
