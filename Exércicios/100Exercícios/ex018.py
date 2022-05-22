#faça um algoritmo que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Digite o valor do ângulo: '))
cos = math.cos(math.radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2}'.format(ang, cos))
sen = math.sin(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2}'. format(ang, sen))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2}'.format(ang, tan))

