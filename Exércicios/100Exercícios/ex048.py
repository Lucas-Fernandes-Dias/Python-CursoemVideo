#faça um programa que calcule a soma  entre todos os numeros impares que são multiplos de três
#e que se encontram no intervalo de 1 a 500
soma = 0
count = 0
for c in range(1, 501):
        if c % 2 == 1 and c % 3 == 0:
            soma = soma + c
            count = count + 1
            print(c, end=' ')
print('\nA soma de todos os \033[1:97m{}\033[m números ímpar que são multiplos de 2 é \033[1:97m{}\033[m'.format(count, soma))

