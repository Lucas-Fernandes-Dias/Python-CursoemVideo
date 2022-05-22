#faã um programa que leia o nome digitado e que mostre o primeiro e o ultimo nome digitado.
n = str(input('Digite o seu nome completo por favor: ')).strip()
nome = n.split()
print('O primeiro nome que aparece é o {}'.format(nome[0]))
print('O ultimo nome que aparece é o {}'.format(nome[len(nome)-1]))

