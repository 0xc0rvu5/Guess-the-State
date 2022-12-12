import turtle, pandas


#initialize global variables
ANSWERS = []
DATA = pandas.read_csv('50_states.csv')
IMAGE = 'blank_states_img.gif'
SCREEN = turtle.Screen()
STATES = DATA['state'].to_list()


#create game window
SCREEN.title('U.S. Guess The States Game')
SCREEN.setup(width=700,height=500)
SCREEN.addshape(IMAGE)
turtle.shape(IMAGE)


def recall():
    '''Output all states not supplied by user to a file called 'states_to_recall_better.csv' when program ends.'''
    missing_states = [ms for ms in STATES if ms not in ANSWERS]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv('states_to_recall_better.csv')


#initiate game loop
try:
    while len(ANSWERS) < 50:
        #additional game setup
        answer_state = SCREEN.textinput(title=f'{len(ANSWERS)}/50 Guess The States',prompt='What\'s another state\'s name?').title()

        #type 'exit' to leave the game functionality while updating 'states_to_recall_better.csv'
        if answer_state == 'Exit':
            recall()
            break

        #if answer is correct append to list and display on map
        if answer_state in STATES:
            ANSWERS.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_row = DATA[DATA.state == answer_state]
            t.goto(int(state_row.x), int(state_row.y))
            t.write(answer_state)
            
except AttributeError:
    recall()
    print('See you later.')
