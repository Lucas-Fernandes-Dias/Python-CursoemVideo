#refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero Todos os lados iguais
#Isósceles 2 lados iguais
#escaleno todos os lados diferentes
a = int(input('Digite um primeiro valor: '))
b = int(input('Digite um segundo valor:  '))
c= int(input('Digite um terceiro valor:  '))
print(a, b, c)
if a == b and b == c:
    print('Essas 3 medidas formariam um triângulo EQUILÁTERO.')
elif a == b and b != c or a == c or b == c:

    print('Essas 3 medidas formariam um triângulo ISÓSCELES.')
elif a != b and b !=c and a != c:
    print('Essas 3 medidas formariam um triângulo ESCALENO.')

