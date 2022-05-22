#faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a sgunda
#função vai mostrar entre todos os valores a soma dos números pares feito pela função somaPar().
from random import randint
from time import sleep

def sorteia(lista):
    print('-='*32)
    print('SORTEANDO OS 5 VALORES DA LISTA!! → ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} → ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')
    print('-='*32)
def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    sleep(0.5)
    print(f'Somando os valores pares de {lista}, temos {soma}')
    print('-='*32)


numeros = list()
sorteia(numeros)
somaPar(numeros)

