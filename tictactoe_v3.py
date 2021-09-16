import random

board = {'a1': ' ', 'b1': ' ', 'c1': ' ',
         'a2': ' ', 'b2': ' ', 'c2': ' ',
         'a3': ' ', 'b3': ' ', 'c3': ' '}

lines = [['a1', 'b1', 'c1'],    # 1 row
         ['a2', 'b2', 'c2'],    # 2 row
         ['a3', 'b3', 'c3'],    # 3 row
         ['a1', 'a2', 'a3'],    # a column
         ['b1', 'b2', 'b3'],    # b column
         ['c1', 'c2', 'c3'],    # c column
         ['a1', 'b2', 'c3'],    # diagonal
         ['a3', 'b2', 'c1']]    # diagonal

score = {}

match_count = 1

def main():
    print('\n**Welcome to Python Tic-Tac-Toe!**\n')
    print('Play against:\n1. CPU easy\n2. CPU hard\n3. Human')
    choice = input('Choose (1, 2 or 3):')
    if choice == '1':
        tictac(human_player, cpu_easy)
    elif choice == '2':
        tictac(human_player, cpu_hard)
    elif choice == '3':
        tictac(human_player, human_player)
    else:
        print('1, 2 or 3 please.')
        main()

def tictac(player1, player2):  # player1 and 2 are functions
    global match_count
    print('\nGame start\n')
    print_board()
    i = 1
    current_player = player1
    turn = 'X'
    while i <= len(board.keys()):
        print('\n'+ turn + '\'s turn.')
        current_player(turn)
        print_board()
        if i >= 5:
            if is_game_over():
                score[match_count] = turn
                match_count += 1
                print('\nGame Over.\n')
                print('*** ' + turn + ' won! ***')
                play_again(player1, player2)
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
        i += 1
    score[match_count] = 'tie'
    match_count += 1
    print('\nGame Over.\nIt is a tie.')
    play_again(player1, player2)

def print_board():
    print('  a b c')
    print('1 ' + board['a1'] + '|' + board['b1'] + '|' + board['c1'])
    print('  -+-+-')
    print('2 ' + board['a2'] + '|' + board['b2'] + '|' + board['c2'])
    print('  -+-+-')
    print('3 ' + board['a3'] + '|' + board['b3'] + '|' + board['c3'])

def legalMove(move):
    if move in board:
        if board[move] == ' ':
            return True
    else:
        return False

def print_score():
    x_final_score = len([k for k,v in score.items() if v == 'X'])
    o_final_score = len([k for k,v in score.items() if v == 'O'])
    print('\n***FINAL SCORE***\n')
    print('#       X   O\n')
    for i in score:
        if score[i] == 'X':
            print(str(i) + '.      @   -')
        elif score[i] == 'O':
            print(str(i) + '.      -   @')
        else:
            print(str(i) + '.      -   -')
    print('\ntotal   ' + str(x_final_score) + '   ' + str(o_final_score))

def play_again(player1, player2):
    print('\nWould you like to play again?')
    answer = input('Y or N: ')
    if answer == 'y' or answer == 'Y':
        for i in board:
            board[i] = ' '
        tictac(player1, player2)
    elif answer == 'n' or answer == 'N':
        print_score()
        exit()
    else:
        print('Y or N, please.')
        play_again(player1, player2)

def is_game_over():
    for line in lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != ' ':
            return True

def possible_win():
    win_lines = [[], []]        # [[x poss wins], [o poss wins]]
    for line in lines:
        line_value = 1
        empty_square = ' '
        for key in line:
            if board[key] == ' ':
                line_value *= 2
                empty_square = key
            elif board[key] == 'X':
                line_value *= 3
            elif board[key] == 'O':
                line_value *= 5
        if line_value == 18:
            win_lines[0].append(empty_square)
        elif line_value == 50:
            win_lines[1].append(empty_square)
    return win_lines


########### PLAYERS #############
def human_player(turn):
    move = input('\nYour move: ')
    if legalMove(move):
        board[move] = turn
    else:
        print('\nIlegal move. Play again.')
        human_player(turn)

def cpu_easy(turn):
    for move in random.sample(board.keys(), len(board)):
        if legalMove(move):
            board[move] = turn
            break

def cpu_hard(turn):
    move = 'b2'
    if turn == 'X': 
        if possible_win()[0]:
            move = possible_win()[0][0]
            board[move] = turn
        elif possible_win()[1]:
            move = possible_win()[1][0]
            board[move] = turn
        elif legalMove(move):
            board[move] = turn
        else:
            for move in random.sample(board.keys(), len(board)):
                if legalMove(move):
                    board[move] = turn
                    break
    else:
        if possible_win()[1]:
            move = possible_win()[1][0]
            board[move] = turn
        elif possible_win()[0]:
            move = possible_win()[0][0]
            board[move] = turn
        elif legalMove(move):
            board[move] = turn
        else:
            for move in random.sample(board.keys(), len(board)):
                if legalMove(move):
                    board[move] = turn
                    break
    

#def cpu_perfect():

##################################

#tictac(cpu_easy, cpu_hard)

main()
