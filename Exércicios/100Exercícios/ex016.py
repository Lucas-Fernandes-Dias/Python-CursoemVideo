#faça um programa que leia um número real qualquer e mostre na tela sua porção inteira.
#ex. digitou-se o número 6.322323 sua porção inteira é 6
from math import floor
num = float(input('Digite um numero quebrado qualquer: '))
int = floor(num)
print('O numero digitado foi {} e sua porção inteira é {}'.format(num, int))


