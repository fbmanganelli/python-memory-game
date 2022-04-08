#Modulos
from funcs import *
import random

#Inicio
clearConsole() 
Start()
Continue()

while True:
    
    while True:
        try:
            op = int(input("(1) Iniciar o Jogo || (2) Regras || (0) Sair do Jogo\n"))
        except ValueError:
            print("Argumento invalido, tente novamente")
        else:
            break

    if op == 1:
        
        #Contadores
        vida = 3
        acerto = 0

        #Tabela de cores
        tab_color = ['\033[92mO\033[m', '\033[92mO\033[m', '\033[93mO\033[m', '\033[93mO\033[m', '\033[91mO\033[m', '\033[91mO\033[m', '\033[94mO\033[m', '\033[94mO\033[m']
        tab_close = ['O','O','O','O','O','O','O','O']
        random.shuffle(tab_color)

        clearConsole()
        print("Voce tera apenas 5 segundos para memorizar a tabela e corresponder os seus pares!\n")
        Continue()

        print_tab(tab_color)

        tempo()
        clearConsole()

        while acerto < 4 and vida > 0:
            
            print_tab(tab_close)
            print("Sua vida:", vida)

            while True:
                
                l1 = int(input("Linha do primeiro par: "))-1
                c1 = int(input("Coluna do primeiro par: "))-1
                
                y1 = 4*l1+c1
                if l1 >= 0 and l1 <= 1 and c1 >= 0 and c1 <= 3 and tab_color[y1] != 'X':
                    tab_close[y1] = tab_color[y1]
                    break
                else:
                    if l1 < 0 or l1 > 1 or c1 < 0 or c1 > 3:
                        print("POSIÇÃO INVALIDA! TENTE NOVAMENTE")
                    elif tab_color[y1] == 'X':
                        print('PAR JÁ CORRESPONDIDO! TENTE NOVAMENTE')
                
            clearConsole()
            print_tab(tab_close)
            print("Sua vida:", vida)

            while True:
                l2 = int(input("Linha do segundo par: "))-1
                c2 = int(input("Coluna do segundo par: "))-1
                y2 = 4*l2+c2
                if l2 >= 0 and l2 <= 1 and c2 >= 0 and c2 <= 3 and tab_color[y2] != 'X' and y2 != y1:
                    tab_close[y2] = tab_color[y2]
                    break
                else:
                    if y2 == y1:
                        print('ESCOLHA UMA POSIÇÃO DIFERENTE DA ANTERIOR!')
                    elif l2 < 0 or l2 > 1 or c2 < 0 or c2 > 3:
                        print("POSIÇÃO INVALIDA! TENTE NOVAMENTE")
                    elif tab_color[y2] == 'X':
                        print('PAR JÁ CORRESPONDIDO! TENTE NOVAMENTE')

            if tab_color[y1] != tab_color[y2]:
                print('VOCE ERROU! TENTE NOVAMENTE')
                vida -= 1
                tab_close[y1] = tab_close[y2] = 'O'
                Continue()
            else:
                if acerto == 0:
                    print("VOCE ACERTOU UM PAR, PARABENS!")
                else:
                    print("VOCE ACERTOU OUTRO PAR, PARABENS!")
                acerto += 1
                tab_color[y1] = tab_color[y2] = 'X'
                Continue()
            clearConsole()
            
        if vida == 0:
            GameOver()
            Continue()
        else:
            Congratulation()
            Continue()
        clearConsole
    
    elif op == 2:
        clearConsole()
        Regras()
        Continue()
    elif op == 0:
        clearConsole()
        print("Beba agua!")
        sleep(0.5)
        clearConsole()
        break
    else:
        print("Numero INVALIDO")
        Continue()
