#desenvolva um programa que leia o comprimento de três rotas e diga ao usuário se eleas podem ou não formar um triângulo
r1 = float(input('Digite a primeira rota: '))
r2 = float(input('Digite a segunda rota:  '))
r3 = float(input('Digite a terceira rota: '))
#r1 isolado pra comparação        r2 isolado para comparação      r3 isolado para comparação
if (r2 - r3) < r1 < (r2 + r3) and (r1 - r3) < r2 < (r1 + r3)  and ( r1 - r2) < r3 < (r1 + r2):
    print('As 3 rotas podem fomar um triângulo.')
else:
    print('As 3 rotas não podem formar um triângulo. ')


