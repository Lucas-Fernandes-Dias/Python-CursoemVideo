#crie um programa que leia nome e média de um aluno guardando tambem a situação em um dicionário
#mostre o conteudo da estrutura na tela
from time import sleep

grupo = {}
grupo['nome'] = str(input('Nome: '))
grupo['media'] = float(input('Média: '))
if grupo['media'] >= 7:
    grupo['situação'] = 'APROVADO'
else:
    grupo['situação'] = 'REPROVADO'
for k, v in grupo.items():
    print(f' - {k} é igual a {v}')
#print(f'O aluno {grupo["nome"]}')
#print(f'Tem média de {grupo["media"]}')
#print(f'O {grupo["nome"]} com média de {grupo["media"]} está {grupo["situação"]}')



