# faça um program que leia um número qualquer e que nos mostre o seu fatorial.
from time import sleep
num = int(input('Digite um número inteiro: '))
print('Vamos calular o fatorial do número digitado, só um momento enquanto nossos computadores fazem os cálculos necessários.')
print('Calculando o fatoria de {}! ='.format(num), end='')
sleep(1)
fact = num
fatorial = 1
while fact > 0:
    print('{}' .format(fact), end='')
    print(' x ', end='')
    fatorial = fatorial * fact
    fact -= 1
    if fact < 1:
        print('= ', end='')
        sleep(1)
        print(fatorial)
        sleep(1)
        print('Encerrando o programa')
        sleep(1)
print('Fim')
sleep(1)