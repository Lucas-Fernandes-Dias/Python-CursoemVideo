#faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso do {}ª candidato: '.format(c)))
    if c == 1:
       maior = peso
       menor = peso
    else:
         if peso > maior:
            maior = peso
         if peso < menor:
            menor = peso
print('O MAIOR peso é {:.0f} KG.'.format(maior))
print('O MENOR peso é {:.0f} KG.'.format(menor))

