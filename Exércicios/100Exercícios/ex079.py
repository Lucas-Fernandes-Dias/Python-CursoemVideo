# crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
# caso o número ja exista na lista, não aceite o cadastramento.
# mostre ao final todos os valores únicos digitados em ordem crescente
numeros = list ()
while True:
    n = int(input('Digite um valor qualquer: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!!!')
    else:
        print('Esse valor já existe, e não foi adicionado!')
    r = str(input('Deseja cadastrar mais números? [ S ] SIM [ N ] NÃO : ')).strip().upper()
    if r not in 'SsNn':
        print('Digite uma resposta válida')
        r = str(input('Deseja cadastrar mais números? [ S ] SIM [ N ] NÃO : ')).strip().upper()
    if r in 'Nn':
        break
print('-*'*20)
print(numeros)


