#escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#o primeiro valor é maior ou o segundo valor é maior
#não existe valor maior, ambos são iguais.
n1 = int(input('Digite um número qualquer inteiro: '))
n2 = float(input('Digite um outro número qualquer inteiro: '))
if n1 > n2:
    print('O {:.0f}, que é o primeiro número digitado é maior que o {:.0f}, que foi o segundo número digitado.'.format(n1, n2))
elif n2 > n1:
    print('O {:.0f}, que é o segundo número digitado é mairo que {:.0f}, que foi o primeiro número digitado.'.format(n2, n1))
else:
    print('Não existe maior ou menor, ambos são idênticos.')

