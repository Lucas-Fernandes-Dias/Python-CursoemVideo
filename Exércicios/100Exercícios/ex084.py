#crie um programa que leia nome e peso de várias pessoas guardando tudo em uma lista
#no final mostre
#quantas pessoas fora cadastradas]
#uma listagem com as pessoas mais pesadas
#uma listagem com as pessoas mais leves
from time import sleep
princ = []
temp = []
mai = men = 0
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = str(input('Deseja continuar cadastrando?: [ S ] SIM [ N ] NÃO: ')).strip().upper()
    if r in 'Nn':
        print('Programa sendo encerrado, aguarde um momento....')
        break
sleep(1)
print(f'{len(princ)} foram cadastradas')
print(f'O maior peso foi de: {mai}kg. Peso de', end='')
for p in princ:
    if p[1] == mai:
        print(f' [{p[0]}]', end='')
print()
print(f'O menor peso foi de: {men}kg. Peso de', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()








