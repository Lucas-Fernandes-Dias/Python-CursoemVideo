#crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas ja são maiores.
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?: '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        print('Esse candidato é maior de idade.')
        maior = maior + 1
    else:
        print('Esse candidato é menor de idade.')
        menor = menor + 1
print('A quantidade de candidatos maiores de idade é {}.'.format(maior))
print('A quantidade de candidatos menores de idade é {}.'.format(menor))


