#faça um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
frase = str(input('Digite uma frase para verificar se é um PALINDROMO: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('TEMOS UM PALINDROMO')
else:
    print('NÃO TEMOS UM PALINDROMO')




