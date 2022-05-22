#faça um algoritmo que leia o preço de um produto e mostre seu novo valor com 5% de desconto.
p = float(input('Digite o valor do preço que vai sofrer um desconto de 5%: R$ '))
np = p-(p/100)*5
print('O preço original era de R$ {:.2f} e o seu novo preço com o desconto de 5% será de R$ {:.2f}'.format(p, np))
