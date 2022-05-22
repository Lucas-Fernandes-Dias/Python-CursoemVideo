#faça um programa ma determinar a ordem de apresentação de trabalho os alunos de uma determinada sala.
import random

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno:  '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno:    '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(lista)


