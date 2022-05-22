#crie um programa onde 4 jogadores joguem o dado e tenham resultados aleatórios
#Guarde esses resultados em um dicionário em Python
#no final, coloque esse dicionário em ordem, sabendo que o vencedor  tirou o maior número no dado.
from time import sleep
from random import randint
from time import sleep
from operator import itemgetter
a = ' '
jogadores ={'Lucas': randint(1, 7),
            'Enzo': randint(1, 7),
            'Leticia': randint(1, 7),
            'Amy': randint(1, 7)}
posições = list()
print('\033[1:97m-=\033[m'*20)
print(f'{a*12}\033[1:31mVAMOS JOGAR DADO\033[m')
print('\033[1:97m-=\033[m'*20)
for k, v in jogadores.items():
    print(f'\033[1:97m{k}\033[m \033[1:33mtirou no dado o valor de\033[m \033[1:31m{v}\033[m')
    sleep(1)
posições = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('\033[1:97m-=\033[m'*20)
print(' \033[1:97m==\033[m \033[1:97:41mRANKING DOS JOGADORES\033[m \033[1:97m==\033[m ')
print()
print('\033[1:97m-=\033[m'*20)
for i, v in enumerate(posições):
    print(f'\033[1:32m{i+1}º\033[m \033[1:97mlugar:\033[m \033[1:33m{v[0]}\033[m \033[1:97mcom\033[m \033[1:31m{v[1]}\033[m')
    sleep(1)
print('\033[1:97m-=\033[m'*20)
print('\033[1:31mFIM\033[m')









