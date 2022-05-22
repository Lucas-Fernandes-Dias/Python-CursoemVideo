#refaça o desafio 051 só que usando a estrutura while.
#faça um programa que leia a PA de um número inteiro, mostrando 10 primeiros termos da progressão.
print('Vamos calcular a PA de um número inteiro')
num = int(int(input('Digite o Termo da PA: ')))
raz = int(input('Digite a Razão da PA: '))
term = num
cont = 1
print('O Termo de {} e a sua Razão de {} tem sua PA: '.format(term, raz), end='')
while cont <= 10:
    print('{} → '.format(term), end='')
    term = term + raz
    cont += 1
print('FIM')

