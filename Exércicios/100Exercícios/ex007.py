#faça um programa que leia as notas de um aluno e que calcule e mostre a sua média.
nome = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
s = n1+n2
m = s/2
print('A média do aluno {} é de {}, resultante da soma da primeira nota {} com a segunda nota {} dividindo o total de {} por 2, esta correto?'.format(nome, m, n1, n2, s))



