# import turtle 
import turtle 

# initialise turtle instance 
stars = turtle.Turtle() 
t = turtle.Turtle()
f = turtle.Turtle()
# increases the speed of turtle 
stars.speed(10000) 
f.speed(10000) 
# to change the background color 
stars.getscreen().bgcolor("black")
 
stars.color("red") 

# stop drawing 
stars.penup() 

# move the turtle 
stars.goto((-200, 50)) 

# start drawing 
stars.pendown() 

# function to draw stars 
def star(turtle, size): 
	if size <= 10: 
		return 
	else: 
		for i in range(5): 
			
			# moving turtle forward 
			turtle.forward(size) 
			star(turtle, size/3) 
			# moving turtle left 
			turtle.left(216) 
			
f.color("green")
f.penup() 

# move the turtle 
f.goto((-200, 50)) 

# start drawing 
f.pendown() 
def st(turtle, size): 
	if size <= 10: 
		return 
	else: 
		for i in range(5): 
			
			# moving turtle forward 
			f.forward(size) 
			st(turtle, size/3) 
			# moving turtle left 
			f.left(216) 


# calling the star function 
star(stars, 360) 
st(stars, 360)
t.color("red")
t.write("STARFRACTAL", font=("Arial", 25, "normal"), align="center")
turtle.done() 
