#escreva um programa que pergunte a quantidade de km rodado por um carro alugado
#que pergunte quantos dias o carro ficou alugado
#calcule o preço a pagar pelo cliente sabendo que o carro custa R$ 60,00 e R$ 0,15 por km rodado.
dias = float(input('Quantos dias o carro ficou alugado pelo cliente: '))
print('O carro ficou alugado por {:.0f} dias'.format(dias))
km = float(input('Qual foi a quilometragem rodada durante os {:.0f} alugados?: '.format(dias)))
print('O quantidade rodada foi de {:.1f}km'.format(km))
tdias = dias*60.00
tkm = km*0.15
st = tdias+tkm
print('O total do aluguel, que é a soma dos dias alugados mais, a quantidade do km rodado multiplado por R$ 0,15,'
      'que dá R$ {:.2f}'.format(st))





