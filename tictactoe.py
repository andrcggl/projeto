import random

score = 0
coord = ''
tabuleiro = {'a1': ' ', 'b1': ' ', 'c1': ' ',
             'a2': ' ', 'b2': ' ', 'c2': ' ',
             'a3': ' ', 'b3': ' ', 'c3': ' '}

def printTabuleiro(tabuleiro):
    print('  a b c')
    print('1 ' + tabuleiro['a1'] + '|' + tabuleiro['a2'] + '|' + tabuleiro['a3'])
    print('  -+-+-')
    print('2 ' + tabuleiro['b1'] + '|' + tabuleiro['b2'] + '|' + tabuleiro['b3'])
    print('  -+-+-')
    print('3 ' + tabuleiro['c1'] + '|' + tabuleiro['c2'] + '|' + tabuleiro['c3'])

def legalMove(move):
    if tabuleiro[move] == ' ':
        return True
    else:
        return False

#def cpuEasy():


def jogadaCPU(dificuldade):
    if dificuldade == '1':
        a = 2
        #   random.choice()
    else:
        a = 1
        # algoritmo

def primeirajogada():
    a = random.randint(0,1)
    if a == 0:
        print('A CPU começa.')
    else:
        print('Você começa!')
        jogada = input('Digite sua jogada: ')

def main():
    
    print('Bem vindo ao jogo da velha!')
    print('Jogue de acordo com as coordenadas a seguir:')
    printTabuleiro(tabuleiro)
    
    print('Gostaria de jogar contra:\n -1- CPU \n -2- um ser humano')
    print('Escolha o nível de dificuldade:\n 1. fácil\n 2. difícil')

    dificuldade = int(input())
    print('\n' + str(dificuldade))    

    if dificuldade == 1 or dificuldade == 2:
        primeirajogada()  
    else:
        print('Por favor, escolha 1 ou 2.')
        main()


#loop do jogo
    while True:
        printTabuleiro(tabuleiro)
        coord = input('Escolha a sua jogada: ')
        legalMove(coord)
        tabuleiro[coord] = 'X'
        jogadacpu(dificuldade,?)
        legalMove(coord)
        tabuleiro[coord] = '0'
        
        

main()


