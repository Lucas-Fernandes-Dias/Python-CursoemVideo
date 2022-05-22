#faça um programa que leia o ano digitado pelo usuário e diga se é BISSEXTO ou não.
ano = int(input('Digite um ano qualquer: '))
if (ano % 4 == 0 and ano % 100 != 1) or (ano % 400 == 0):
    print('O ano digitado é BISSEXTO')
else:
    print('O ano NÃO é BISSEXTO')


