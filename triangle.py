# Import turtle module
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed and background color
t.speed(0)
turtle.bgcolor("black")

# Define a function to draw a triangle
def triangle(size, color):
    # Set the fill color
    t.fillcolor(color)
    # Start filling
    t.begin_fill()
    # Draw a triangle with the given size
    for i in range(3):
        t.forward(size)
        t.left(120)
    # End filling
    t.end_fill()

# Define a function to draw a triangle pattern
def triangle_pattern(size, color):
    # Draw a triangle with the given size and color
    triangle(size, color)
    # Move the turtle to the next position
    t.penup()
    t.right(10)
    t.forward(10)
    t.pendown()
    # Decrease the size by 2
    size -= 2

# Define a list of colors
colors = ["purple","blue", "green", "yellow", "orange", "red"]

# Set the initial size
size = 100

# Draw the triangle pattern with different colors and sizes
for i in range(50):
    # Choose a color from the list
    color = colors[i%6]
    # Draw the triangle pattern with the current size and color
    triangle_pattern(size, color)

# Hide the turtle
t.hideturtle()

# Keep the turtle window open
turtle.done()
