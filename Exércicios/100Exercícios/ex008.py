#escrava um programa que leia o numero em metros, e exiba esse numero convertido para centimetro e milimetro
numero = float(input('Digite um numero em metros: '))
print('{}m'.format(numero))
d= numero*10
c = numero*100
mm = numero*1000
dam = numero/10
hm = numero/100
km = numero/1000
print('O medida digitada foi {}m'.format(numero))
print('A conversão para centimetro fica {}cm'.format(c))
print('A conversão para milimitro fica {}mm'.format(mm))
print('A conversão para decametro fica {}dam'.format(dam))
print('A conversão para hectometro fica {}hm'.format(hm))
print('A conversão para kilometro fica {}km'.format(km))


