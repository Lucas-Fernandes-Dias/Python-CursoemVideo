#crie um programa que leia 5 valores numéricos e guarde-os em uma lista
#Mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = []
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'{valores}')
print(f'o {maior} é o maior número digitado e sua posição é: ', end='')
for pos, c in enumerate(valores):
    if c == maior:
        print(f'{pos}...', end='')
print()
print(f'o {menor} é o menor número digitado e sua posição é: ', end='')
for pos, c in enumerate(valores):
    if c == menor:
        print(f'{pos}...', end='')
print()
print('Fim')
