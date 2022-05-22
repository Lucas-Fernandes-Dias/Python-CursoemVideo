#crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiúscula
#o nome com todas as letras minúscula
#quantas letras o nome tem sem considerar o espaços
#quantas letras tem o primeiro nome
nome = str(input('Digite o seu nome completo por favor: '))
up = nome.upper()
print('O nome digitado é {} e passando todas as letras para maiúscula ficaria assim {}'.format(nome,up))
low = nome.lower()
print('O nome digitado é {} e passando todas as letras para minúscula ficaria assim {}'.format(nome, low))
space = nome.replace(' ','')
numtotal = len(space)
print('O nome digita foi {} e ele contém {} de letras sem considerar os espaços vazios'.format(nome, numtotal))
notspace = nome.split()
first = len(notspace[0])
print('O nome digitado foi {} tendo como primeiro nome {} e esse nome tem {} letras'.format(nome, notspace[0], first ))









