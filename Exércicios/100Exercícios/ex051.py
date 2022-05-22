#desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
a = (' '*10)
print('-*'*20)
print('\033[1:97m{}10 TERMOS DE UMA PA\033[m'.format(a))
print('-*'*20)
term = int(input('Digite um TERMO: '))
raz = int(input('Digite uma Razão: '))
cont = term + (10*raz)
print('TERMO: {}'.format(term))
print('RAZÃO: {}'.format(raz))
for c in range(term, cont):
    print(c, '→', end=' ')
print('\033[1:31mACABOU\033[m')
