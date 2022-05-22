#faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
#ex: 1234 unidade 4 dezena 3 centena 2 milhar 1
num = int(input('Digite um numero qualquer de 0 à 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A milhar desse número é: {}'.format(m))
print('A centena desse número é: {}'.format(c))
print('A dezena desse número é: {}'.format(d))
print('A unidade desse número é: {}'.format(u))









