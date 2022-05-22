#melhore o ex086
#mostre a soma de todos os valores pares
#a soma dos valores da terceira coluna
#o maior valor da segunda linha
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = []
totalpar = somapar = coluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l} , {c}: '))
    if l % 2 == 0:
        par.append(matriz[l])
    if c % 2 == 0:
        par.append(matriz[c])
print('-*'*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 < 1:
            totalpar += matriz[l][c]
            somapar += 1
        if c == 2:
            coluna += matriz[l][c]
        if l == 0:
            maior = matriz[1][c]
            if matriz[1][c] > maior:
                maior = matriz[1][c]
    print()
print(f'Foram digitados {somapar} números pares, e sua soma é {totalpar}')
print(f'A soma da coluna é {coluna}')
print(f'O maior número da 2 linha é {maior}')




