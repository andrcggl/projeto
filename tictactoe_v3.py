import random

board = {'a1': ' ', 'b1': ' ', 'c1': ' ',
         'a2': ' ', 'b2': ' ', 'c2': ' ',
         'a3': ' ', 'b3': ' ', 'c3': ' '}

def main():
    print('\n**Welcome to Python Tic-Tac-Toe!**\n')
    print('Play against:\n1. CPU\n2. Human')
    choice = input('Choose (1 or 2):')
    if choice == '1':
        tictac(human_player, cpu_easy)
    elif choice == '2':
        tictac(human_player, human_player)
    else:
        print('1 or 2, please.')
        main()

def tictac(player1, player2):  # player1 and 2 are functions
    print('\nGame start\n')
    print_board()
    i = 1
    current_player = player1
    turn = 'X'
    while i <= len(board.keys()):
        print('\n'+ turn + '\'s turn.')
        current_player(turn)
        print_board()
        if is_game_over(turn):
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
    if move in board.keys():
        if board[move] == ' ':
            return True
    else:
        return False

def play_again(player1, player2):
    print('\nWould you like to play again?')
    answer = input('Y or N: ')
    if answer == 'y' or answer == 'Y':
        for i in board.keys():
            board[i] = ' '
        tictac(player1, player2)
    elif answer == 'n' or answer == 'N':
        exit()
    else:
        print('Y or N, please.')
        play_again()

def is_game_over(turn):
    if board['a1'] == board['a2'] == board['a3'] != ' ':  # a column
        return True
    elif board['b1'] == board['b2'] == board['b3'] != ' ':  # b column
        return True
    elif board['c1'] == board['c2'] == board['c3'] != ' ':  # c column 
        return True
    elif board['a1'] == board['b1'] == board['c1'] != ' ':  # 1 row
        return True
    elif board['a2'] == board['b2'] == board['c2'] != ' ':  # 2 row
        return True
    elif board['a3'] == board['b3'] == board['c3'] != ' ':  # 3 row
        return True
    elif board['a1'] == board['b2'] == board['c3'] != ' ':  # diagonal
        return True
    elif board['a3'] == board['b2'] == board['c1'] != ' ':  # diagonal
        return True

def human_player(turn):
    move = input('\nYour move: ')
    if legalMove(move):
        board[move] = turn
    else:
        print('\nIlegal move. Play again.')
        human_player(turn)
    return board

def cpu_easy(turn):
    for move in random.sample(board.keys(), len(board.keys())):
        if legalMove(move):
            board[move] = turn
            return board


#tictac(cpu_easy, cpu_easy, turn)

main()
