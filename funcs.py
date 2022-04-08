import os
from time import sleep

def Start():
    print("Trabalho Final Logica Matemática")
    print("Alunos: Alessandra, Filipe e Iury")
    print("\n\tJogo da Memoria\n")

def Continue():
    input("Aperte <Enter> para continuar")
    clearConsole()

def Regras():
    print("Voce devera memorizar uma tabela de cores que sera mostrada pra voce e corresponder todos os pares corretamente")
    print("Indique uma cor atraves da linha e coluna da tabela")
    print("Voce tem APENAS 3 vidas")
    print("Bom jogo!\n")

def GameOver():
    print("Você perdeu todas as vidas!")
    print("\n\033[91m============== GAME OVER ==============\033[m\n")

def Congratulation():
    print('PARABENS! VOCE ACERTOU TODOS OS PARES')
 
def print_tab(tab):
    for x in range(0,8,4):
        print('\t', tab[x], tab[x+1], tab[x+2], tab[x+3])
    print("")

def tempo():
    for i in range(1, 6):
        print(i)
        sleep(1)

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)