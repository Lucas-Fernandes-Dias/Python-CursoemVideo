#crie um programa que leia o desempenho de um jogador de futebol
#programa vai ler o nome do jogador, quantas partidas ele jogou
#depois vai ler a quantidade de gols feito em cada partida
#no final tudo isso será guardado em um dicionario incluindo o total de gols feitos durante o campeonato
dados = {}
dados['Nome'] = str(input('Nome do Jogador: '))
golss = []
Partidas = int(input('Total de Partidas Jogadas: '))
print('-='*15)
dados['Partidas'] = Partidas
for i in range(Partidas):
    golss.append(int(input(f'Quantos gols na partida {i+1}º?: ')))
print('-='*15)
dados['Gols'] = golss[:]
dados['total'] = sum(golss)
print('-='*32)
print(dados)
print('-='*32)
for k, v in dados.items():
    print(f'- O campo {k} tem valor {v}')
print('-='*32)
print(f'O jogador {dados["Nome"]} jogou {dados["Partidas"]} partidas')
c = 0
for c in range(Partidas):
    print(f'  => Na partida {c+1}, fez {dados["Gols"][c]} gols')
    c +=1
print(f'Ao todo o jogador {dados["Nome"]} fez {dados["total"]} gols em {dados["Partidas"]} partidas.')






