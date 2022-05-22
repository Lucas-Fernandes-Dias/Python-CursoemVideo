#crie um algoritmo quer leia um numero e mostre o seu dobro, triplo e sua raiz quadrada.
numero = int(input('Digite um número por favor: '))
d = numero*2
t = numero*3
r2 = numero**(1/2)
print('O número digitado foi {} o dobro desse número é {} e o seu triplo é {} tendo a raiz quadrada de {:.5}, está correto?'.format(numero, d, t, r2))

