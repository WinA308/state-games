import turtle

import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
tr = 0
turtle.shape(image)

'''

def get_mouse_click_coor(x , y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
'''

def turtle_writer_on_map(x ,y ,state_name):
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.goto(x ,y)
    t.write(state_name)
guess = 0
guess_states = []
miss_states = []

data = pandas.read_csv("50_states.csv")

print(data)
while(guess!=50)and(tr < 3):
    answer_state = screen.textinput(title="Guess the State", prompt=f"What's Another State's {guess}/50 ")
    answer_state = answer_state.title()
    if(answer_state == "Exit"):
        for st in data.state:
            if st not in guess_states:
                miss_states.append(st)
        break
    for st in data.state:
        answer_state = answer_state.title()
        if(st == answer_state):
            state_dat = data[data.state == answer_state]
            guess_states.append(answer_state)
            guess += 1
            turtle_writer_on_map(int(state_dat.x), int(state_dat.y), answer_state)

new_data = pandas.DataFrame(miss_states)
new_data.to_csv("state_to_learn.csv")
print(miss_states)



screen.exitonclick() # turtle.mainloop() --------------- Keep Screen Open