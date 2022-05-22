#desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem cobrando R$ 0,50 por km para viagens até 200km de distância
#e R$ 0,45 para viagens mais longas.
dist = int(input('Digite a distância da sua viagem em km, por favor: '))
km = int(200)
if dist <= km:
    print('A viagem de {}km vai custar para o passageiro R${:.2f}'.format(dist, (dist * 0.50)))
else:
    print('A viagem de {}km vai custar para o passageiro R${:.2f}'.format(dist, (dist * 0.45)))