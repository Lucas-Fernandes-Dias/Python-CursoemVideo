#refaça o desafio 009 mostrando a tabuada de um numero que o usuário escolher só que agora utilizando o laço for
numero = int(input('Digite o número que deseja saber sua tabuada: '))
exp = -1
for c in range(0, 11):
    s = numero*c
    exp = exp + 1
    print('\033[1:36m{}\033[m \033[1:33mx\033[m \033[1:34m{:2}\033[m = \033[1:97m{:2}\033[m'.format(numero, exp, s))
print('A TABUADAdo {} é essa ai de cima!!!'.format(numero))

