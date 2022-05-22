#faça um programa que mostre o que a pessoa tem na carteira em reais o valor que seria em dolar.
din = float(input('Digite o valor em R$ que tem em sua carteira: R$ '))
print('R$ {:.2f}'.format(din))
do = din/3.27
print('A quantia que você disponhe em reais é de R$ {:.2f} essa quantia daria pra comprar $ {:.2f} dolares.'.format(din, do))
