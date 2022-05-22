#escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5
#peça para o usuário tentar adivinhar que número o computador escolheu
#o computador deverá escrever na tela se o usuário acertou ou não.
import random
print('Esse programa vai escolher um número de 0 à 10, tente adivinhar, você terá apenas 1 chance, boa sorte')
num = random.randint(1, 11)
ad = int(input('Digite o número que você acha que o computador escolheu: '))
if ad == num:
    print('Parabéns você acertou!!!!!')
else:
    print('O computador venceu essa rodada, tente outra vez.')
print('O número escolhido pelo computador foi o {}.'.format(num))