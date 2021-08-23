import random

tabuleiro = {'a1': ' ', 'a2': ' ', 'a3': ' ',
             'b1': ' ', 'b2': ' ', 'b3': ' ',
             'c1': ' ', 'c2': ' ', 'c3': ' '}

def printTabuleiro(tabuleiro):
    print(tabuleiro['a1'] + '|' + tabuleiro['a2'] + '|' + tabuleiro['a3'])
    print('-+-+-')
    print(tabuleiro['b1'] + '|' + tabuleiro['b2'] + '|' + tabuleiro['b3'])
    print('-+-+-')
    print(tabuleiro['c1'] + '|' + tabuleiro['c2'] + '|' + tabuleiro['c3'])

def legalMove(move):
    if tabuleiro[move] = ' ':
        return True
    else:
        return False

def cpuEasy():
    random.choice()

def main():
    print('Bem vindo ao jogo da velha!')
    print('Escolha o nível de dificuldade:\n 1. fácil\n 2. difícil')



main()