import turtle
import math
turtle.bgcolor("black")
def draw_tree(t, length, angle):
    if length < 5:
        t.penup()
        t.forward(length)
        t.pendown()
        t.dot(5)
        t.penup()
        t.backward(length)
        t.pendown()
        return

    t.forward(length)
    t.right(angle)
    draw_tree(t, length * 0.7, angle)
    t.left(angle * 2)
    draw_tree(t, length * 0.7, angle)
    t.right(angle)
    t.backward(length)

# Create the turtle object
t = turtle.Turtle()
t.speed()
t.goto(-100,100)

# Set the turtle pen color to white
t.pencolor("white")

# Set the turtle pen size to 3
t.pensize(3)
t.left(90)
# Draw the tree
draw_tree(t, 100, 45)

# Keep the turtle window open until closed manually
turtle.done()
