#melhore o desafio 028 onde o computador vai "pensar" em um número de 0 a 10 e o usuário tenta adivinhar
#só que agora o jogador vai tentar até adivinhar, mostre quantas tentativas o usuário precisou para acertar.

import random
comp = random.randint(0, 10)
jogador = ''
tentativas = 0
print('O computador acabou de escolher um número dentre 0 e 10, tente adivinhar.')
while jogador != comp:
    jogador = int(input('Qual o seu palpite? : '))
    tentativas += 1
    if jogador < comp:
        print('Mais...')
    if jogador > comp:
        print('Menos...')
    if jogador > 10:
        print('Número inválido, tente novamente com números no intervalo de 1 à 10.')
        tentativas -= 1
print('O jogador precisou de {} para acertar o {} que foi o número que o computador escolheu.'.format(tentativas, comp))



