import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data.state.to_list()
xpos = data.x.to_list()
ypos = data.y.to_list()


new_data = dict()
for index in range(len(states)):
    new_data[states[index].casefold()] = (xpos[index], ypos[index])
game_on = True

size = len(states)
count = 0 
while count < size:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another states's name ?")
    answer_state = answer_state.casefold()
    if new_data.get(answer_state):
        name = turtle.Turtle()
        name.hideturtle()
        name.penup()
        name.goto(new_data.get(answer_state))
        name.write(f"{answer_state[0].capitalize()}{answer_state[1:]}", move=True, align="center", font=('Open Sans', 12, 'normal'))
        new_data.pop(answer_state)
        count += 1

screen.mainloop()