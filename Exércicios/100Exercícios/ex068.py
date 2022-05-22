#faça um programa para o computador jogar par ou impar com o usuário.
import random
from time import sleep
soma = v = 0
num = [1,2,3,4,5,6,7,8,9,10]
while True:
    jog = int(input('Escolha um número entre 1 à 10: '))
    comp = random.choice(num)
    escolha = ' '
    soma = comp + jog
    while escolha not in 'PI':
        escolha = str(input('Você quer ser [ P ] PAR ] [ I ] ÍMPAR: ')).strip().upper()[0]
        print(f'O jogador escolheu : \033[1:97m{jog}\033[m')
        print(f'O computador escolheu :\033[1:31m{comp}\033[m')
        print(f'O Total de {soma}')
        if soma % 2 == 0:
            print('DEU PAR')
        else:
            print('DEU IMPAR')
            #if escolha in 'Ii' and soma % 2 > 0:
     #   print('O Computador VENCEU!!!')
    if escolha in 'Pp' and soma % 2 == 0:
        print('O jogador VENCEU!!!')
        v += 1
    elif escolha in 'Ii' and soma % 2 > 0:
        print('O jogador VENCEU!!!')
        v += 1
    else:
        print('O computador Venceu!!!!')
        break
    des = str(input('Deseja continuar? [ S ] Sim [ N ] Não: '))
    if des in 'Nn':
       break
print(f'Você venceu {v} vezes, PARABÉNS')
sleep(1)
print('FIM')

