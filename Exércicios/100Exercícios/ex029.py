#escreva um programa que leia a velocidade de um carro
#se ele ultrapassar 80 km/h mostre uma mensagem dizendo que ele foi multado
#a multa vai custar R$ 7,00 a cada km acima do limite permitido.
vel = str(input('Digite a velocidade em que o carro está agora: '))
med = int(vel)
perm = int('80')
multa = (med - perm)
valor = (multa * 7)

if med > perm:
    print('Você acabou de ser multado, sua multa esta sendo calculada.')
    print('O valor da multa é de R$ {:.2f}.'.format(valor))
    print('não corra, não bata, não morra')
else:
    print('Você esta dentro da velocidade permitida para a via. Parabéns')
