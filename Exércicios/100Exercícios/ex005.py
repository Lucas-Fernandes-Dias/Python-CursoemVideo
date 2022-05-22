#faça um programa que leia um numero inteiro e mostre na tela o seu antecessor e o seu sucessor.
numero = int(input('Digite um número por favor: '))
ant = numero-1
suc = numero+1
print('O número digitado foi {} sendo o seu antecessor {} e o seu sucessor {}, está correto? '.format(numero, ant, suc))
