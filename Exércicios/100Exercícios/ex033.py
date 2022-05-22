# faça um programa que leia 3 números e diga qual é o maior e qual é o menor dentre os 3.
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior dentre os 3 números digitados é o {}.'.format(maior))
#verificando o menor número dentre os 3.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O meno dentre os 3 números digitados é o {}.'.format(menor))
