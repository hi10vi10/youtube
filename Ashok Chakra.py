# Import turtle module
import turtle

# Create a turtle object
t = turtle.Turtle()
t1 = turtle.Turtle()
# Set the speed and background color
t.speed(0)
turtle.bgcolor("black")

# Define a function to draw a star
def star(size, color):
    # Set the fill color
    t.fillcolor(color)
    # Start filling
    t.begin_fill()
    # Draw a star with the given size
    for i in range(5):
        t.forward(size)
        t.right(144)
    # End filling
    t.end_fill()

# Define a function to draw a star spiral
def star_spiral(size, color):
    # Draw a star with the given size and color
    star(size, color)
    # Move the turtle to the next position
    t.penup()
    t.right(10)
    t.forward(10)
    t.pendown()
    # Decrease the size by 2
    size -= 2

# Define a list of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Set the initial size
size = 200

# Draw the star spiral with different colors and sizes
for i in range(50):
    # Choose a color from the list
    color = colors[i%6]
    # Draw the star spiral with the current size and color
    star_spiral(size, color)

# Hide the turtle
t.hideturtle()
t1.color("gold")
t1.goto(300,100)
t1.write("ASHOK CHAKRA",font=("ARIAL",20,"bold"))

# Keep the turtle window open
turtle.done()
