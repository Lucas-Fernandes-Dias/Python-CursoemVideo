#elabora um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento
#a vista dinheiro ou cheque 10% de desconto
#a vista no cartão 5% de desconto
#em até 2x no cartão preço normal
#3x ou mais no cartão 20% de juros.
prod = float(input('Digite o valor do produto original: R$ '))
pag = ('''Qual será a forma de pagamento:
[1] à vista dinheiro
[2] à vista cartão débito
[3] em até 3x no cartão
[4] 3x ou mais no cartão''')
a = prod - (prod * 10 / 100)
b = prod - (prod * 5 / 100)
c = prod
d = prod + (prod * 20 / 100)
print(pag)
opção = int(input('Digite em qual opção será o pagamento feito pelo cliente: '))
print(opção)
if opção == 1:
    print('O valor do produto sofrerá um reajuste, e passa a ficar assim R$ {:.2f}.'.format(a))
elif opção == 2:
    print('O valor do produto sofrerá um reajuste, e passa a ficar assim R$ {:.2f}'.format(b))
elif opção == 3:
    print('O valor do produto sofrerá um reajuste, e passa a ficar assim R$ {:.2f}'.format(c))
elif opção == 4:
    print('O valor do produto sofrerá um reajuste, e passa a ficar assim R$ {:.2f}.'.format(d))
else:
    print('Opção inválida, por favor digite uma opção correta.')

