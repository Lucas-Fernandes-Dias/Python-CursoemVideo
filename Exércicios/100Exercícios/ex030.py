#crie um programa para ler um número inteiro e que diga se ele é par ou ímpar.
num = int(input('Digite um numero inteiro qualquer: '))
test = (num % 2)
if test == 0:
    print('O número {} digitado é PAR'.format(num))
else:
    print('O número {} que foi digitado é ÍMPAR'.format(num))