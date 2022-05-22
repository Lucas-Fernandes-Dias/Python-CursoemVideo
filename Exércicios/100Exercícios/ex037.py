#escreva um programa  que leia um número inteiro qualquer e que ele escolha qual será a base da conversão.
# a) binário b) octal 3) hexadecimal
num = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão:
[1] Converter em BINÁRIO
[2] Converter em OCTAL
[3] Converter em HEXADECIMAL''')
opção = int(input('Digite a opção desejada: '))
if opção == 1:
    print('O número digitado é {} e sua conversão para BINÁRIO fica assim: {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número digitado é {} e sua conversão para OCTAL fica assim: {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número digitado é {} e sua conversão para o HEXADECIMAL fica assim {}.'.format(num, hex(num)[:2]))
else:
    print('a opção escolhida é inválida, por favor, tente novamente. Obrigado.')

