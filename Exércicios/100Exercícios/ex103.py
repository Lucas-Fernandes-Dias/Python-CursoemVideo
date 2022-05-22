#Faça um programa que tenha uma função chamada ficha() que receba dois parâmetros opicionais
#nome do jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador
#Mesmo que algum dado esteja faltando.
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jogador} fez {gols} gols')


jogador = str(input('Nome do JOGADOR: '))
gols = str(input(f'Quantos gols o {jogador} fez?: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(gol=gols)
else:
    ficha(jogador, gols)
