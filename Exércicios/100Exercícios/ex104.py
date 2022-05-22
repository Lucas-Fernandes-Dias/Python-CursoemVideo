#crie um programa que tenha a função leiaint() que vai funcionar de forma semelhante a função input() do Python
#só que fazendo a validação para aceitar apenas um valor numérico. Ex n = leiaint('Digite um número qualquer: ')
def leiaInt(txt):
    ok = False
    valor = 0
    while True:
        numbers = str(input(txt))
        if numbers.isnumeric():
            valor = int(numbers)
            ok = True
        else:
            print('\033[0;31m ERRO! Digite um número inteiro válido\033[m.')
        if ok:
            break
    return valor


numbers = leiaInt('Digite um número qualquer: ')
print(f'Você digitou o número {numbers}')

