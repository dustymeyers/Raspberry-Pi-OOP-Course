from shapes import Paper, Triangle, Rectangle, Oval

paper = Paper()

# Here's the random Oval we are required to add
rand_oval = Oval()
rand_oval.randomize(51, 125)

rand_oval.draw()

g_oval = Oval()
g_oval.set_width(50)
g_oval.set_height(100)
g_oval.set_color('green')
g_oval.set_x(120)
g_oval.set_y(350)

g_oval.draw()

r_rect = Rectangle()
r_rect.set_width(200)
r_rect.set_height(130)
r_rect.set_color('red')

r_rect.draw()

p_rect = Rectangle()
p_rect.set_width(100)
p_rect.set_height(350)
p_rect.set_color('purple')
p_rect.set_x(450)
p_rect.set_y(50)

p_rect.draw()

b_triangle = Triangle(5, 5, 80, 45, 100, 200)
b_triangle.set_color('blue')

b_triangle.draw()

y_triangle = Triangle(200, 240, 125, 130, 15, 105)
y_triangle.set_color('yellow')

y_triangle.draw()

paper.display()
