board = {'a1': ' ', 'b1': ' ', 'c1': ' ',
         'a2': ' ', 'b2': ' ', 'c2': ' ',
         'a3': ' ', 'b3': ' ', 'c3': ' '}

moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

turn = 'X'

def print_board(board):
    print('  a b c')
    print('1 ' + board['a1'] + '|' + board['b1'] + '|' + board['c1'])
    print('  -+-+-')
    print('2 ' + board['a2'] + '|' + board['b2'] + '|' + board['c2'])
    print('  -+-+-')
    print('3 ' + board['a3'] + '|' + board['b3'] + '|' + board['c3'])

def legalMove(move):
    if move in moves:
        if board[move] == ' ':
            return True
    else:
        return False

def play_again():
    print('\nWould you like to play again?')
    answer = input('Y or N: ')
    if answer == 'y' or answer == 'Y':
        for i in moves:
            board[i] = ' '
        tictac(player1, player2, turn)
    elif answer == 'n' or answer == 'N':
        exit()
    else:
        print('Y or N, please.')
        play_again()

def game_over(board, turn):
    if board['a1'] == board['a2'] == board['a3'] != ' ':  # a column
        print('\nGame Over.\n')
        print('*** ' + turn + ' won! ***')
        play_again()
    elif board['b1'] == board['b2'] == board['b3'] != ' ':  # b column
        print('\nGame Over.\n')
        print('*** ' + turn + ' won! ***')
        play_again()
    elif board['c1'] == board['c2'] == board['c3'] != ' ':  # c column 
        print('\nGame Over.\n')
        print('*** ' + turn + ' won! ***')
        play_again()
    elif board['a1'] == board['b1'] == board['c1'] != ' ':  # 1 row
        print('\nGame Over.\n')
        print('*** ' + turn + ' won! ***')
        play_again()
    elif board['a2'] == board['b2'] == board['c2'] != ' ':  # 2 row
        print('\nGame Over.\n')
        print('*** ' + turn + ' won! ***')
        play_again()
    elif board['a3'] == board['b3'] == board['c3'] != ' ':  # 3 row
        print('\nGame Over.\n')
        print('*** ' + turn + ' won! ***')
        play_again()
    elif board['a1'] == board['b2'] == board['c3'] != ' ':  # diagonal
        print('\nGame Over.\n')
        print('*** ' + turn + ' won! ***')
        play_again()
    elif board['a3'] == board['b2'] == board['c1'] != ' ':  # diagonal
        print('\nGame Over.\n')
        print('*** ' + turn + ' won! ***')
        play_again()

def human_player(board, turn):
    move = input('\nYour move: ')
    if legalMove(move):
        board[move] = turn
    else:
        print('\nIlegal move. Play again.')
        human_player(board, turn)
    return board

def cpu_easy(board, turn):
    for move in moves:
        if legalMove(move):
            board[move] = turn
            return board
        else:
            for move in reversed(moves):
                if legalMove(move):
                    board[move] = turn
                    return board

player1 = human_player

player2 = cpu_easy

def tictac(player1, player2, turn):  # player1 and 2 are functions
    print('\nGame start\n')
    print_board(board)
    i = 1
    player = player1
    while i < 9:
        print('\n'+ turn + '\'s turn.')
        print_board(player(board, turn))
        game_over(board, turn)
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        if player == player1:
            player = player2
        else:
            player = player1
        i += 1
    print('\nGame Over.\nIt is a tie.')
    exit()
        
def main():
    print('\n**Welcome to Python Tic-Tac-Toe!**\n')
    print('Play against:\n1. CPU\n2. Human')
    choice = input('Choose (1 or 2):')
    if choice == '1':
        tictac(player1, cpu_easy, turn)
    elif choice == '2':
        player2 = human_player
        tictac(player1, player2, turn)
    else:
        print('1 or 2, please.')
        main()


#tictac(player1, player2, turn)

main()
