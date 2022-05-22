#escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#o programa vai perguntar o valor da casa
#o salário do comprador
#em quantos anos ele vai pagar
#calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
casa = float(input('Digite o valor da casa a ser financiada: R$  '))
salario = float(input('Digite o valor do salário do comprador:  R$ '))
ano = int(input('Digite em quantos anos será pago o valor emprestado: '))
meses = ano*12
prestacao = casa / meses
maximo = (salario*30/100)
print('{:.2f}'. format(prestacao))
print('{:.2f}'.format(maximo))
print('A Casa custa R${:.2f}'.format(casa))
print('O salário do comprador é de R${:.2f}'.format(salario))
print('Ele deseja financiar em {:.0f} anos.'.format(meses))
print('A parcela não pode ultrapassar o valor de R$ {}'.format(maximo))
if prestacao <= maximo:
    print('EMPRÉSTIMO \033[32mAPROVADO')
else:
    print('EMPRÉSTIMO \033[31mNEGADO')