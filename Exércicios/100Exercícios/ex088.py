#crie um progrmaa que gere palpites para mega sena
#o programa vai perguntar quantos palpites vc deeja gerar
#não pode haver números repetidos no mesmo jogo.
#os jogos são gerados dentro de 1 a 60
#cadastre tudo em uma lista composta
from random import randint
from time import sleep
lista = []
jogos = []
print('\033[1:34m-*\033[m'*12)
print('   \033[1:33mPALPITES MEGA SENA\033[m   ')
print('\033[1:34m-*\033[m'*12)
quant = int(input('\033[1:97mQuantos palpites quer gerar?: \033[m'))
print('\033[1:31m-*\033[m'*15)
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    total += 1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print('   \033[1:97mSORTEANDO OS PALPITES!!!\033[m  ')
print('\033[1:31m-*\033[m'*18)
for i, l in enumerate(jogos):
    print(f'\033[1:97mJogo\033[m \033[32m{i+1}\033[m \033[36m>>>\033[m {l}')
    sleep(1)
print('\033[31m-*\033[m'*18)


