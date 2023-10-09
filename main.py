import pandas
import turtle

screen = turtle.Screen()
screen.title("USA")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

states = pandas.read_csv("./50_states.csv")
score = 0
quessed_states = []


def write_state(x_cor, y_cor, state):
    state_name = turtle.Turtle()
    state_name.hideturtle()
    state_name.penup()
    state_name.goto(x=x_cor, y=y_cor)
    state_name.write(state)
    state_name.color("black")


# Initial Load from save
write_states_saved = pandas.read_csv("./guessed_states.csv")
for index, state in enumerate(states["state"]):
    for state_g in write_states_saved["0"]:
        if state == state_g:
            score += 1
            quessed_states.append(state)
            write_state(states["x"][index], states["y"][index], state)

while score < 50:
    # Ask the state
    answer_state = screen.textinput(
        title=f"{score}/50 Guessed the state", prompt="State name?"
    ).capitalize()
    # Check whether state exists
    for index, state in enumerate(states["state"]):
        # if state exists
        if state.capitalize() == answer_state and state not in quessed_states:
            score += 1
            write_state(states["x"][index], states["y"][index], state)
            quessed_states.append(state)
            st = pandas.DataFrame(quessed_states)
            st.to_csv("guessed_states.csv")


screen.exitonclick()
