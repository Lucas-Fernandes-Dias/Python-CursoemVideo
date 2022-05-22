#crie um programa  que vai ler vários números digitados pelo teclado e vai colocar em uma lista
#depois disso, crie 2 listas extras para separar os numeros da lista 1 em pares e impares.
#mostre as 3 listas.
from time import sleep
num = []
par = []
impar = []
while True:
    v = int(input('Digite um valor: '))
    num.append(v)
    r = str(input('Deseja continuar cadastrando valores [ S ] SIM [ N ] NÃO: '))
    if r in 'Nn':
        print('Espere enquanto sua lista é processada....')
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
sleep(1)
print(f'Você casdastrou {len(num)} novos valores.')
print(f'A sua lista ficou assim: {num}')
print(f'A lista de valores pares ficou assim: {par}')
print(f'A lista de valores impares ficou assim: {impar} ')






