# Import turtle module
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed and background color
t.speed(0)
turtle.bgcolor("black")

# Define a function to draw a hexagon
def hexagon(size, color):
    # Set the fill color
    t.fillcolor(color)
    # Start filling
    t.begin_fill()
    # Draw a hexagon with the given size
    for i in range(6):
        t.forward(size)
        t.left(60)
    # End filling
    t.end_fill()

# Define a function to draw a hexagonal pattern
def hex_pattern(size, color):
    # Draw a hexagon with the given size and color
    hexagon(size, color)
    # Move the turtle to the next position
    t.penup()
    t.right(10)
    t.forward(10)
    t.forward(size * 2)
    t.pendown()
    # Draw another hexagon with the same size and color
    # hexagon(size, color)

# Define a list of colors
colors = ["purple","blue", "green", "yellow", "orange", "red","white","hotpink", "gray"]

# Set the initial size
size = 100

# Draw the hexagonal pattern with different colors and sizes
for i in range(50):
    # Choose a color from the list
    # color = colors[i]
    color = colors[i%9]
    # Draw the hexagonal pattern with the current size and color
    hex_pattern(size, color)
    # Increase the size by 10
    size += 10
    # Turn the turtle right by 60 degrees
    t.right(70)

# Hide the turtle
t.hideturtle()

# Keep the turtle window open
turtle.done()
