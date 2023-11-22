import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("US State Game")
img = "C:\\Users\\hp\\Documents\\Python Dev Udemy\\US state game\\blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


data = pd.read_csv("C:\\Users\\hp\\Documents\\Python Dev Udemy\\US state game\\50_states.csv")
# length = len(data)
states = data.state.to_list()
length = len(states)
guess_states = []
not_guessed_states = []
guess_state=0


while guess_state<=5:
    message = screen.textinput(title=f"{guess_state}/50 Guess the State", prompt="What's the another state's name?").title()
    # print(message.capitalize())

    if message=="Exit":
        # for state in states:
        #     if state not in guess_states:
        #         not_guessed_states.append(state)
        not_guessed_states = [state for state in states if state not in guess_states]
        print(f"You Missed These States : {not_guessed_states}")
        new_data = pd.DataFrame(not_guessed_states)
        new_data.to_csv("Missed.csv")
        break

    if(message in states):
        guess_states.append(message)
        t= turtle.Turtle()
        print("Hello")
        state_data = data[data.state == message]
        print(state_data)
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(message)
    guess_state+=1

# def get_mouse(x,y):
#     print(x,y)


# turtle.onscreenclick(get_mouse)
screen.mainloop()