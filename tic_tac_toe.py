#TIC TAC TOE
from tkinter import *
#to overcome draw anomaly
anomaly = True
#set a new game config file and start the game accordingly
def start_game(player1):
    global config

    config = {
    'player1': None,
    'player2': None,
    'next_turn': None,
    }

    if player1 == 'X':
        config['player1'] = 'X'
        config['player2'] = 'O'
        config['next_turn'] = 'O'
    elif player1 == 'O':
        config['player1'] = 'O'
        config['player2'] = 'X'
        config['next_turn'] = 'X'
    else:
        print('Invalid')

#set a new game board and resets everything to initital state
def new_game():
    config['player1'] = None
    config['player2'] = None
    config['next_turn'] = None
    e1.delete(0, END)
    msg.config(text = '')

    #reset the buttons to original state
    buttons[0].config(command = lambda:press(buttons[0]))
    buttons[0].config(text = '-')
    buttons[1].config(command = lambda:press(buttons[1]))
    buttons[1].config(text = '-')
    buttons[2].config(command = lambda:press(buttons[2]))
    buttons[2].config(text = '-')
    buttons[3].config(command = lambda:press(buttons[3]))
    buttons[3].config(text = '-')
    buttons[4].config(command = lambda:press(buttons[4]))
    buttons[4].config(text = '-')
    buttons[5].config(command = lambda:press(buttons[5]))
    buttons[5].config(text = '-')
    buttons[6].config(command = lambda:press(buttons[6]))
    buttons[6].config(text = '-')
    buttons[7].config(command = lambda:press(buttons[7]))
    buttons[7].config(text = '-')
    buttons[8].config(command = lambda:press(buttons[8]))
    buttons[8].config(text = '-')


#this function changes the text on button accordingly
def change(button):
    if config['next_turn'] == 'O':
        button.config(text = 'X')
        config['next_turn'] = 'X'
    elif config['next_turn'] == 'X':
        button.config(text = 'O')
        config['next_turn'] = 'O'

#check for invalid movement in the game board
def invalid_mov(button):
    if button.cget('text') != '-':
        return True
    else:
        return  False



#check winner in row way
def row_check(str):
    if b1.cget('text') == str and b2.cget('text') == str and b3.cget('text') == str:
        msg.config(text = f'winner is {str}')
        stop()
    elif b4.cget('text') == str and b5.cget('text') == str and b6.cget('text') == str:
        msg.config(text = f'winner is {str}')
        stop()
    elif b7.cget('text') == str and b8.cget('text') == str and b9.cget('text') == str:
        msg.config(text = f'winner is {str}')
        stop()

#check winnr in column way
def col_check(str):
    if b1.cget('text') == str and b4.cget('text') == str and b7.cget('text') == str:
        msg.config(text = f'winner is {str}')
        stop()
    elif b2.cget('text') == str and b5.cget('text') == str and b8.cget('text') == str:
        msg.config(text = f'winner is {str}')
        stop()
    elif b3.cget('text') == str and b6.cget('text') == str and b9.cget('text') == str:
        msg.config(text = f'winner is {str}')
        stop()

#check winner in diagonal way
def dgnl_check(str):
    if b1.cget('text') == str and b5.cget('text') == str and b9.cget('text') == str:
        msg.config(text = f'winner is {str}')
        stop()
    elif b3.cget('text') == str and b5.cget('text') == str and b7.cget('text') == str:
        msg.config(text = f'winner is {str}')
        stop()

#draw for game
def draw():
    count = 0
    for item in buttons:
        if item.cget('text') != '-':
            count += 1
            if count == 9 and anomaly:
                msg.config(text = 'DRAW!')

#stop the game after winner is decided
def stop():
    global anomaly
    for item in buttons:
        if item.cget('text') == '-':
            item.config(command = False)
    anomaly = False


#decide Winner
def get_winner():
    row_check(config['player1'])
    row_check(config['player2'])
    col_check(config['player1'])
    col_check(config['player2'])
    dgnl_check(config['player1'])
    dgnl_check(config['player2'])
    draw()

def press(button):
    if invalid_mov(button):
        return
    else:
        change(button)
        get_winner()


def main():
    #setting root window of game
    root = Tk()

    #setting title of the root windows
    root.title('TIC TAC TOE')

    Label(root, text = 'Player1').pack()

    global e1
    e1 = Entry(root)
    e1.pack()

    buttonFrame = Frame(root, padx = 10, pady = 10)
    buttonFrame.pack()

    Button(buttonFrame, text = 'START', command = lambda:start_game(e1.get())).pack(side='left')
    Button(buttonFrame, text = 'NEW GAME', command = new_game).pack(side='right')

    frame = Frame(root, padx = 10, pady = 10)
    frame.pack()


    #button object are created
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    b1 = Button(frame, text = '-', width = 5, height = 3)
    b2 = Button(frame, text = '-', width = 5, height = 3)
    b3 = Button(frame, text = '-', width = 5, height = 3)
    b4 = Button(frame, text = '-', width = 5, height = 3)
    b5 = Button(frame, text = '-', width = 5, height = 3)
    b6 = Button(frame, text = '-', width = 5, height = 3)
    b7 = Button(frame, text = '-', width = 5, height = 3)
    b8 = Button(frame, text = '-', width = 5, height = 3)
    b9 = Button(frame, text = '-', width = 5, height = 3)

    global buttons
    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    #button object are organized in grid format
    b1.grid(row = 0, column = 0)
    b2.grid(row = 0, column = 1)
    b3.grid(row = 0, column = 2)
    b4.grid(row = 1, column = 0)
    b5.grid(row = 1, column = 1)
    b6.grid(row = 1, column = 2)
    b7.grid(row = 2, column = 0)
    b8.grid(row = 2, column = 1)
    b9.grid(row = 2, column = 2)



    #button objects are configured to change the button text on event
    b1.config(command=lambda:press(b1))
    b2.config(command=lambda:press(b2))
    b3.config(command=lambda:press(b3))
    b4.config(command=lambda:press(b4))
    b5.config(command=lambda:press(b5))
    b6.config(command=lambda:press(b6))
    b7.config(command=lambda:press(b7))
    b8.config(command=lambda:press(b8))
    b9.config(command=lambda:press(b9))

    global msg
    msg = Message(root, text = '')
    msg.pack()

    root.mainloop()

if __name__=='__main__':main()
