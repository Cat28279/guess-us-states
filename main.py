import turtle
import pandas

data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].to_list()

x_coordinates = data["x"].to_list()
print(x_coordinates)
y_coordinates = data["y"].to_list()
print(y_coordinates)


screen = turtle.Screen()
screen.setup(725, 491)
screen.title("U.S.A. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

guessed_states = []
score = 0

game_over = False

while not game_over:
    states_guessed = f"{score}/50"
    player_guess = turtle.textinput(title=states_guessed, prompt="Guess a U.S. state. Type Exit to end game.")
    player_guess = player_guess.title()
    if player_guess in list_of_states and player_guess not in guessed_states:
        score += 1
        guessed_states.append(player_guess)
        index = list_of_states.index(player_guess)
        new_x = x_coordinates[index]
        new_y = y_coordinates[index]
        t.goto(new_x, new_y)
        t.write(player_guess)
    elif player_guess in guessed_states:
        player_guess = turtle.textinput(title="Guess a state: ", prompt="Guess a U.S. state. Type Exit to end game.")
        player_guess = player_guess.title()
    elif score == 50:
        game_over = True
        turtle.textinput(title="You guessed all 50 states!")
    elif player_guess == "Exit":
        player_guess = player_guess.title()
        game_over = True
        states_remaining = [state for state in list_of_states if state not in guessed_states]
        new_data = pandas.DataFrame(states_remaining)
        new_data.to_csv("states_to_learn.csv")


