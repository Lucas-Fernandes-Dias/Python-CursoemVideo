#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
#triangulo retângulo e calcule e mostre o comprimento da hipotenusa.

import math
co = float(input('Digita o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = ((co**2 + ca**2))
h = math.sqrt(hip)
print('a hipotenusa é {:.2f}'.format(h))
