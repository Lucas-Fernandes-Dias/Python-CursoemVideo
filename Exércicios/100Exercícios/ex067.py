# faça um programa que mostre a tabuada de qualquer número que o usuário digitar, só para de mostrar quando ele digitar um valor negativo.
from time import sleep
cont = 1
while True:
    num = int(input('Deseja saber a TABUADA de qual número?: '))
    cont = 1
    if num < 0:
        break
    while cont <= 10:
        print('{} x {:2} = {:2}'.format(num, cont, (num*cont)))
        cont += 1
    print('-*-' *10)
print('O usuário encerrou o programa da TABUADA, aguarde...')
sleep(1)
print("FIM")