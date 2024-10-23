import tkinter

def set_tile (row, column):
    global curr_player

    if board[row][column]['text'] != '':
        return

    board[row][column]['text'] = curr_player

    if curr_player == PlayerO: #switch palyer
        curr_player = PlayerX
    else:
        curr_player = PlayerO

    label['text'] = curr_player + "'s turn"

    #check winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    #horizontally, check 3 rows
    for row in range(3):
        if (board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] and board [row][0]['text'] != ''):
            label.config(text=board[row][0]['text'] + 'is the winner!', foreground = clr_ylw)
            for column in range(3):
                board[row][column].config(foreground = clr_ylw, background = clr_gry)
            game_over = True
            return

    #vertical, check 3 columns
    for column in range(3):
        if (board[0][column]['text'] == board[1][column]['text'] == board[2][column]['text'] and board[0][column]['text'] != ''):
            label.config(text=board[0][column]['text']+ ' is the winner!', foreground = clr_ylw)
            for row in range(3):
                board[row][column].config(foreground = clr_ylw, background = clr_gry)
            game_over = True
            return

    #diagonally
    if (board[0][0]['text'] == board [1][1]['text'] == board[2][2]['text'] and board[0][0]['text'] != ''):
        label.config(text=board[0][0]['text']+ ' is the winner!', foreground = clr_ylw)
        for i in range(3):
            board[i][i].config(foreground = clr_ylw, background = clr_gry)
        game_over = True
        return

    #anti-diagonally
    if (board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] and board[0][2]['text'] != ''):
        label.config(text=board[0][2]['text']+ ' is the winner!', foreground = clr_ylw)
        board[0][2].config(foreground = clr_ylw, background = clr_gry)
        board[1][1].config(foreground = clr_ylw, background = clr_gry)
        board[2][0].config(foreground = clr_ylw, background = clr_gry)
        game_over = True
        return
    
    #tie
    if (turns == 9):
        game_over = True
        label.config(text='Tie', foreground=clr_ylw)

def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label['text'] = curr_player+ "'s turn"

    for row in range(3):
        for column in range(3):
            board[row][column].config(text = '', foreground = clr_blu, background = clr_gry)


#Game Setup
PlayerX='X'
PlayerO='O'
curr_player=PlayerX
board= [[0,0,0,],
        [0,0,0,],
        [0,0,0,]]

clr_blu='#4584b6'
clr_ylw='#ffde57'
clr_gry='#646464'

turns = 0
game_over = False   

#Window Setup
window=tkinter.Tk() #create game window
window.title('Tic Tac Toe')
window.resizable(False, False) #widht & height fixed

frame = tkinter.Frame(window) #placing frame inside the window
label = tkinter.Label(frame, text=curr_player + " 's turn", font=('consolas', 20), background=(clr_gry), foreground=('white'))

label.grid(row=0, column=0, columnspan=3, sticky='we')

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame,text='', font=('consolas', 50, 'bold'), background=clr_gry, foreground=clr_blu, width=4, height=1, command=lambda row=row, column=column: set_tile(row, column))

        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text='restart', font=('consolas', 20), background=clr_gry, foreground='white', command=new_game)

button.grid(row=4, column=0, columnspan=3, sticky='we')

frame.pack()

#center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

# format: "(W) * (H) + (X) +(Y)"
window.geometry(f'{window_width}x{window_height}+{window_x}+{window_y}')
window.mainloop()