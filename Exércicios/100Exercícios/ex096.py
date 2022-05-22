#faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
#e mostre a área do terreno.
def area(a, l):
    tot = a * l
    print(f'A área de um terreno cuja as medidas são {largura:.2f} largura e {comprimento:.2f} comprimento é {tot:.2f}m²!')


def texto(txt):
    print('-*'*15)
    print(txt)
    print('-*'*15)


largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento  (m): '))
texto('Controle de Área')
area(largura, comprimento)

