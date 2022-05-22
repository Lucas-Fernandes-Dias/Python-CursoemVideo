# faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros
#O progrma tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint
from time import sleep
def l():
    print('-='*20)


def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados: ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = cont
        else:
            if valor > maior:
                maior = valor
        cont += 1
    sleep(0.5)
    print(f'Foram informados {cont} valores.')
    print(f'O maior entre eles é {maior}')
    sleep(0.5)
    l()



maior(2, 4, 5, 7, 89, 102, 15)
maior(29, 14, 59, 17, 97, 10, 15)
maior(12, 48, 15, 77, 99, 10, 75)
maior(25, 84, 35, 27, 19, 12, 17)

