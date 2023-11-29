# Import turtle module
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed and background color
t.speed(0)
turtle.bgcolor("black")

# Define a function to draw a heart
def heart(size, color):
    # Set the fill color
    t.fillcolor(color)
    # Start filling
    t.begin_fill()
    # Draw a heart with the given size
    t.left(140)
    t.forward(size)
    t.circle(-size/2, 180)
    t.left(90)
    t.circle(-size/2, 180)
    t.forward(size)
    # End filling
    t.end_fill()

# Define a function to draw a heart pattern
def heart_pattern(size, color):
    # Draw a heart with the given size and color
    heart(size, color)
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
size = 200

# Draw the heart pattern with different colors and sizes
for i in range(50):
    # Choose a color from the list
    color = colors[i%6]
    # Draw the heart pattern with the current size and color
    heart_pattern(size, color)

# Hide the turtle
t.hideturtle()

# Keep the turtle window open
turtle.done()
