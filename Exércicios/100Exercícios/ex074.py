#crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem números
# indique o menor e o maior número gerado pelo computador.

import random
num = ()
maior = c =  0
menor = 2000
for c in range(0,5):
    comp = random.randint(0, 2000)
    c += 1
    num = comp
    if comp > maior:
        maior = comp
    if menor > comp:
        menor = comp
    print(num,'→ ',end='')
print(f'\nO maior número dentre os escolhidos foi o {maior}')
print(f'O menor número dentre os escolhidos foi o {menor}')
print('Fim')