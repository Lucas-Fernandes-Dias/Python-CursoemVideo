#aprimore o desafio ex093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador.
time = list()
jogador = dict()
partidas = list()

print('-='*15)
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input('Total de Partidas Jogadas: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}º?: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [ S ] SIM [ N ] NÃO: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERROR! Digite uma resposta válida: S/N')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40)
while True:
    busca = int(input('Desejar fazer o levantamento de qual jogador?[999 parar]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERROR! Não existe jogador cadastrado para esse código {busca}.')
    else:
        print(f' ==LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
        print('-=' * 30)
print('<< VOLTE SEMPRE >>')



'''print('-='*32)
print(dados)
print('-='*32)
for k, v in dado.items():
    print(f'- O campo {k} tem valor {v}')
print('-='*32)
print(f'O jogador {dado["Nome"]} jogou {dado["Partidas"]} partidas')
c = 0
for c in range(Partidas):
    print(f'  => Na partida {c+1}, fez {dado["Gols"][c]} gols')
    c +=1
print(f'Ao todo o jogador {dado["Nome"]} fez {dado["total"]} gols em {dado["Partidas"]} partidas.')'''
