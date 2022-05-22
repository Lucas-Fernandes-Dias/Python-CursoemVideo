#faça um progrma que leia um número inteiro digitado pelo usuário e mostre os 7 primeiro numeros de sua fibonacci
from time import sleep
a = (' '*8)
print('-*-'*15)
print('{} \033[1:97mSEQUÊNCIA DE FIBONACCI\033[m'.format(a))
print('-*-'*15)
term = int(input('Quantos TERMOS você quer mostrar: '))
sleep(1)
p1 = 0
p2 = 1
cont = 3
print('{} → '.format(p1), end='')
sleep(1)
print('{}'.format(p2), end='')
while cont <= term:
    p3 = p1 + p2
    sleep(1)
    print(' → {}'.format(p3), end='')
    p1 = p2
    p2 = p3
    cont += 1
sleep(1)
print(' → FIM')
sleep(1)