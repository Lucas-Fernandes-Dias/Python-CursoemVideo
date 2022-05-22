#crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dado de cada pessoa em um dicionário
#e todos os dicionários em uma lista. No final, mostre: A) quantas pessoas foram cadastradas B) a média de idade
#c) uma lista com as mulheres D) uma lista de pessoas com idade acima da média.
pessoa = {}
galera = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [ S ] SIM [ N ] NÃO: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, responda S ou N')
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A média de idade é {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão fora da média de idade: ')
for p in galera:
    if p['idade'] > media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('      <<      ENCERRANDO      >>')



