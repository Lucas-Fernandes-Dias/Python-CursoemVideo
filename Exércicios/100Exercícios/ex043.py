#desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule e mostre o seu IMC
#monstrando o seu status de acordo com a tabela abaixo
# abaixo de 18.5 abaixo do peso ideal
# entre 18.5 e 25 peso ideal
# 25 até 30 sobrepeso
# 30 até 40 obesidade
# acima de 40 obesidade mórbida
altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura**2)
ap = ('Abaixo do Peso')
id = ('No peso ideal')
sp = ('Sobrepeso')
ob = ('Obesidade')
om = ('Obesidade Mórbida')
a = float('18.5')
z = int(a)
b = int('25')
c = int('30')
d = int('40')
print(imc)
if imc < a:
    print('\033[1:97:41m{\033[m.'.format(ap))
elif imc >= z and imc <= b:
    print('Você esta no \033[1:97:42m{}\033[m.'.format(id))
elif imc > b and imc < c:
    print('\033[1:97:43m{}\033[m'.format(sp))
elif imc > c and imc < d:
    print('\033[1:97:44m{}\033[m'.format(ob))
elif imc > d:
    print('\033[1:97:41m{}\033[m.'.format(om))


