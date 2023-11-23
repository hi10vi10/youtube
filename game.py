import turtle
import random
turtle.bgcolor("black")
turtle.title("GAME!!!!")
t=turtle.Turtle()

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)
t = player_one.clone()
t.shape("arrow")
t.color("red")
t.goto(300,30)
t.pendown()
t.right(90)
t.forward(200)
t.right(180)
t.forward(300)
t.write("END LINE", font=("Arial", 20, "bold"))

die = [1,2,3,4,5,6]
for i in range(20):
    if player_one.pos() >= (300,100):
            t.penup()
            t.goto(-200,100)
            t.write("Player One Wins  🏆", font=("Arial", 30, "bold"))
            break
    elif player_two.pos() >= (300,-100):
            t.penup()
            t.goto(-200,100)
            t.write("Player Two Wins  🏆", font=("Arial", 30, "bold"))
            break
    else:
            player_one_turn = input("Press 'Enter' to roll the die ")
            die_outcome = random.choice(die)
            print("The result of the die roll is: ")
            print(die_outcome)
            print("The number of steps will be: ")
            print(20*die_outcome)
            player_one.fd(20*die_outcome)
            player_two_turn = input("Press 'Enter' to roll the die ")
            die_outcome = random.choice(die)
            print("The result of the die roll is: ")
            print(die_outcome)
            print("The number of steps will be: ")
            print(20*die_outcome)
            player_two.fd(20*die_outcome)
turtle.done()