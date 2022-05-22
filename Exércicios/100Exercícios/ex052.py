#faça um programa que leia um número inteiro e diga se ele é ou não um numero primo.
#numero primo é maior que 1 divisível por ele mesmo e por 1
nume = str(input('Digite um numero inteiro para saber se ele é primo: '))
num = int(nume)
tot = 0
for c in range(1, num+1):
       if num % c == 0:
           print('\033[1:31m', end='')
           tot = tot + 1
       else:
           print('\033[1:32m', end='')
       print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível \033[1:31m{} vezes.\033[m'.format(num, tot))
if tot == 2:
    print('Portanto o {} \033[1:32mÉ PRIMO!!!\033[m'.format(num))
else:
    print('Portanto  o {} \033[1:31mNÃO é PRIMO!!!\033[m'.format(num))




