# crime um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possta mostrar
#as notas de cada aluno individualmente.
from time import sleep
dados = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    r = str(input('Deseja continuar cadastrando alunos [ S ] SIM [ N ] NÃO: ')).strip().upper()
    if r in 'Nn':
        break
    print('-*'*30)
    print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
    print('-*'*25)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostra notas de qual aluno (999 para encerrar): '))
    if opc == 999:
        print('Você optou por encerrar o programa, aguarde um momento')
        sleep(2)
        break
    if opc <= len(dados) -1:
        print(f'Notas de {dados[opc][0]} são {dados[opc][1]}')
print('Finalizado')


