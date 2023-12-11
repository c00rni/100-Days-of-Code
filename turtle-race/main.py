from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=600, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
while True:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
    if user_bet in colors:
        is_race_on = True
        break

count = -100
turtles = []

for color in colors:
    new_turtle = Turtle()
    turtles.append(new_turtle)
    new_turtle.shape(name="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-270, y=count)
    count += 40

winner = ""

while is_race_on:
    for turtle in turtles:
        turtle.fd(random.randrange(11))
        if turtle.xcor() > 300:
            winner = turtle.pencolor()
            is_race_on = False

if user_bet == winner:
    print(f"You won ! The winning turtle is {winner}")
else:
    print(f"You lost. The winning turtle is {winner}")

screen.mainloop()
