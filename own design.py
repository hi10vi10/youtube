import turtle
import random
turtle.bgcolor("black")
turtle.setpos(5,5)
def draw_rangoli():
    # Create the turtle object
    t = turtle.Turtle()
    t.speed(0)
    
    # Set the background color to black
    # t.bgcolor("black")

    # Set the turtle pen color to white
    t.pencolor("white")

    # Set the turtle pen size to 3
    t.pensize(20)

    # Define the rangoli pattern
    pattern = [
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0],
    ]
    # Draw the rangoli pattern
    for row in pattern:
        for cell in row:
            if cell == 1:
                t.dot(20)
                t.penup()
                t.forward(20)
                t.pendown()
            else:
                t.penup()
                t.forward(20)
                t.pendown()

        t.penup()
        t.goto(0, t.ycor() - 20)
        t.pendown()

    # Keep the turtle window open until closed manually
    turtle.done()

# Draw the rangoli pattern
draw_rangoli()
