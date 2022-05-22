#crie um programa que tenha uma tupla com várias pavras (não usar acentos). Depois disso, você
#deve mostrar , cada palavra , e suas vogais.
from time import sleep
lst = ('Acabaxi', 'fruta', 'comida', 'agua', 'mulher', 'homem','paraguai', 'uruguai')
print('-='*40)
for palavra in lst:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for vogal in palavra:
        if vogal.lower() in 'aeiou':
            print('\033[1:97m', vogal.lower(),'\033[m', end='')
sleep(1)
print('\n')
print('-='*40)
print('Fim')
print('-='*40)