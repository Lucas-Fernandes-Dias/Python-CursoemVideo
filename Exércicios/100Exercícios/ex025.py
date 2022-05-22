#crie um programa que diga se contem Silva no nome digitado pelo usuário.
nome = str(input('Digite seu nome por favor: ')).upper().strip()
print('No nome {} contém o sobrenome Silva?: {}'.format(nome, 'SILVA'in nome))

