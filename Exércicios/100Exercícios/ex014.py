#faça um programa que converta a temperatura ºC para ºF.
temp = float(input('Digite a temperatura em ºC: '))
print('{:.1f}ºC'.format(temp))
fah = ((9*temp) / 5) + 32
print('{:.1f}ºF'.format(fah))
