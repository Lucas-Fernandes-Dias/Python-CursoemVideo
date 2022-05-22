# crie um programa que faça o computador jogar jokenpo com você.
import random
from time import sleep
itens = ['tesoura', 'papel', 'pedra']
computador = str(random.choice(itens))
a = 'tesoura'
b = 'papel'
c = 'pedra'
print('\033[31m*\033[m'*20)
print('Vamos jogar JOKENPO? ')
print('\033[31m*\033[m'*20)
print('''[1] Sim 
[2] Não''')
escolha = int(input('\033[1:33mQual vai ser sua escolha:\033[m '))
jogador = 0
if escolha == 2:
     print('NÃO???')
     print('Que pena, fica para um próxima vez então.')
elif escolha == 1:
    print('SIM')
    print('Vamos nessa então, você está preparado?')
    jogador = str(input('''faça sua escolha:
tesoura papel pedra
: '''))
   # print('JO')
    #sleep(1)
    #print("KEN")
    #sleep(1)
    #print('PO!!!')
    print('Jogador escolheu {}.'.format(jogador))
    print('Computador escolheu foi {}.'.format(computador))
    if computador == jogador:
        print('EMPATE')
    elif computador == a and jogador == b or computador == b and jogador == c or computador == c and jogador == a:
        print('Computador Venceu!!!')
    elif jogador == a and computador == b or jogador == b and computador == c or jogador == c and computador == a:
        print('Jogador VENCEU, PARABÉNS')
elif escolha != 1 and escolha != 2:
    print('Opção Inválida')







