#crie um programa que leia o nome ano de nascimento e carteira de trabalho e cadastre-o (com idade)
#se por acaso o CTPS for diferente de ZERO o dicionário receberá também o ano de contratação e o salário
#calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.
from time import sleep
from datetime import datetime
dados = {}
print('-='*15)
print(' == CADASTRO DE APOSENTADORIA == ')
print('-='*15)
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
CTPS = int(input('Carteira de Trabalho Nº: '))
if CTPS != 0:
    dados['CTPS'] = CTPS
    dados['Contratacao'] = int(input('Ano de Contratação: '))
    dados['Salario'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = (dados['Contratacao'] - nasc) + 35
    print('-=' * 20)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
print("FIM")







