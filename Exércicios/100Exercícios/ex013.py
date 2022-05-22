#faça um algoritmo que leia o salário de um funcionário e como seria caso ele recebece um aumento de 15%.
salario = float(input('Digite o salário do funcionário: R$ '))
ns = salario+(salario/100)*15
print('O salário atual é de R$ {:.2f} e o seu novo salário com o reajuste de 15% seria de R$ {:.2f}'.format(salario, ns))