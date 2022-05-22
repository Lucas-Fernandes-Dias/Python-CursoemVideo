#crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única
#que mantenha separados os valores pares e impares.
#no final, mostre os valores pares e impares em ordem crescente.
ordem = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º: '))
    if valor % 2 == 0:
        ordem[0].append(valor)
    else:
        ordem[1].append(valor)
print('-*'*20)
ordem[0].sort()
print(f'Os valores pares foram: {ordem[0]}')
ordem[1].sort()
print(f'Os valores impares foram: {ordem[1]}')
