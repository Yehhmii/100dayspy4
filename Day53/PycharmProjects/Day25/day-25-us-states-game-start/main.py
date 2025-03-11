import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# helps us get the coordinates of the point on turtle
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name")
    answer_state_t = answer_state.title()
    if answer_state_t == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        missed_state_data = pandas.DataFrame(missing_states)
        missed_state_data.to_csv("states_to_learn.csv")
        break
    if answer_state_t in all_states:
        guessed_states.append(answer_state_t)
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_row = data[data.state == answer_state_t]
        timmy.goto(int(state_row.x), int(state_row.y))
        timmy.write(answer_state_t)

# state_to_learn.csv
