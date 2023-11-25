# Import turtle module
import turtle

# Create a turtle object
t1 = turtle.Turtle()
t=t1.clone()

# Set the speed and background color
t.speed(1)
turtle.bgcolor("black")
t.penup()
t.goto(0,-250)
t.pendown()
t.color("red")

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
heart(400,"red")

# Hide the turtle
t.hideturtle()
t.color("white")
t.penup()
t.goto(0,50)
t.pendown()
t.left(3)
t.forward(400)
t.left(180)
t.forward(850)
t.penup()
t1.goto(-250,50)
t.pendown()
t1.color("black")
t1.write("WE LOVE U ❤️", font=("Arial",50,"bold"))

# Keep the turtle window open
turtle.done()
