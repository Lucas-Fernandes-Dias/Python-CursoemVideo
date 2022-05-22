#façã um programa que leia a largura e a altura de uma parede em metros e calcule a sua área
#e a  quantidade de tinta necessária para pinta-lá, sabendo-se que a cada litro de tinta pinta uma área de 2m².
l = float(input('Digite a medida da largura da parade: '))
al = float(input('Digite a altura da parede: '))
area = l*al
tinta = area/2
print('A area da parede é de {}m², e a quantidade de tinta necessária para pinta-lá seria em torno de {}L'.format(area, tinta))


