# Import turtle module
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed and background color
t.speed(0)
turtle.bgcolor("black")

# Define a function to draw a square
def square(size, color):
    # Set the fill color
    t.fillcolor(color)
    # Start filling
    t.begin_fill()
    # Draw a square with the given size
    for i in range(4):
        t.forward(size)
        t.left(90)
    # End filling
    t.end_fill()

# Define a function to draw a square spiral
def square_spiral(size, color):
    # Draw a square with the given size and color
    square(size, color)
    # Move the turtle to the next position
    t.penup()
    t.left(10)
    t.forward(10)
    t.pendown()
    # Decrease the size by 2
    size -= 2

# Define a list of colors
colors = ["purple","blue", "green", "yellow", "orange", "red"]

# Set the initial size
size = 100

# Draw the square spiral with different colors and sizes
for i in range(50):
    # Choose a color from the list
    color = colors[i%6]
    # Draw the square spiral with the current size and color
    square_spiral(size, color)

# Hide the turtle
t.hideturtle()

# Keep the turtle window open
turtle.done()
