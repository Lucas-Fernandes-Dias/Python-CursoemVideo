#crie um programa que leia vários produtos e seus preços
# mostre no fim quantos produtos tem o preço maior que 1mil reais
#e o nome do produto mais barato e o valor.
#gasto total da compra.
from time import sleep
qtd = soma = cont = maior = cont = 0
resp = ' '
barato = ' '
while resp != 'N':
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    valor = float(input('Digite o valor do produto: '))
    qtd += 1
    soma += valor
    cont += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    if valor >= 1000:
        maior += 1
    perg = str(input('Deseja cadastrar novos produtos [ S ] Sim [ N ] Não: ')).strip().upper()[0]
    if perg not in 'NS':
        perg = str(input('Deseja cadastrar novos produtos [ S ] Sim [ N ] Não: ')).strip().upper()[0]
    elif perg == 'N':
        print('Coletando informações cadastradas, aguarde um momento, por favor.')
        break
print(f'Você cadastrou {qtd} protudos')
print(f'O produto mais barato é o {barato}.')
print(f'O valor total da compra ficou em R$ {soma:.2f}.')
print(f'Teve {maior} produtos que custaram mais que R$ 1.000,00')
sleep(1)
print('Fim')