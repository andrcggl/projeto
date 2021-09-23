import random

m, n, k = 0, 0, 0

while not m in range(3,27):
    m = int(input('choose value for m (3 to 26): '))
while not n in range(3,27):
    n = int(input('choose value for n (3 to 26): '))
while not k in range(3, max(m, n)+1):
    k = int(input('choose value for k (3 <= k <= max(m, n): '))

board = [['  ' #j + i*m
        for j in range(1, m+1)]     # m is the board's width
        for i in range(n)]          # n is the board's height

def columns(board):
    return [[board[j][i]
             for j in range(n)]
            for i in range(m)]
            
def diagonals(board):
    return [[board[n - p + q - 1][q]
             for q in range(max(p-n+1, 0), min(p+1, m))]
            for p in range(n + m - 1)]

def antidiagonals(board):
    return [[board[p - q][q]
             for q in range(max(p-n+1,0), min(p+1, m))]
            for p in range(n + m - 1)]

def lines(board):
    return [x for x in 
            (board + columns(board) 
                   + diagonals(board)
                   + antidiagonals(board))
        if len(x) >= k]

def print_board():
    letters = 'abcdefghijklmnopqrstuvwxyz'[0:m]
    top_border = '  '
    for i in letters:
        top_border = f'{top_border:<4}{i}  '
    print(top_border)
    for i in range(1, n+1):
        rows = ''
        rows = f'{rows}{i:<3}|'
        for j in range(m):
            rows = rows + f'{board[i-1][j]}|'
        divisor = '   +--'
        for k in range(m-1):
            divisor = f'{divisor}+--'
        print(f'{divisor}+')
        print(f'{rows}{i:>3}')
    print(f'{divisor}+')
    print(top_border)

def move_is_legal(move):
    if len(move) == 2 and move[0].isalpha() and move[1].isdigit():
            line = int(move[1]) - 1
    elif len(move) == 3 and move[0].isalpha() and move[1:3].isdigit():
            line = int(move[1:3]) -1
    column = ord(move[0]) - 97
    if column in range(m) and line in range(n):
        if board[line][column] == '  ':
           return True

def game(player1, player2):  # player1 and 2 are functions
    print('\nGame start\n')
    print_board()
    i = 1
    current_player = player1
    turn = '><'
    while i <= n*m:
        print(f'\n{turn}\'s turn.')
        current_player(turn)
        print_board()
        if i >= (k*2)-1:
            if is_game_over():
                print('\nGame Over.\n')
                print(f'*** {turn} won! ***')
                exit()
                #play_again(player1, player2)
        if turn == '><':
            turn = '()'
        else:
            turn = '><'
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
        i += 1
    print('\nGame Over.\nIt is a tie.')
    exit()
    #play_again(player1, player2)

def is_game_over():
    for line in lines(board):
        count = 1
        for i in range(len(line) - 1):
            if line[i] == line[i+1] != '  ':
                count += 1
                if count == k: 
                    return True
            else:
                count = 1

########### PLAYERS #############
def human_player(turn):
    move = input('\nYour move: ')
    if len(move) == 2 and move[0].isalpha() and move[1].isdigit():
            line = int(move[1]) - 1
    elif len(move) == 3 and move[0].isalpha() and move[1:3].isdigit():
            line = int(move[1:3]) -1
    else:
        print('\nIlegal move. Try again.')
        human_player(turn)
    column = ord(move[0]) - 97
    if move_is_legal(move):
        board[line][column] = turn
    else:
        print('\nIlegal move. Try again.')
        human_player(turn)

def cpu_random(turn):
    a = True
    while a:
        i = random.randint(0, n-1)
        j = random.randint(0, m-1)
        if board[i][j] == '  ':
            board[i][j] = turn
            a = False
#################################

game(human_player, cpu_random)