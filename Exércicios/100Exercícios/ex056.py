#desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas no final do programa, mostre:
#a média de idade do grupo
#qual é o nome do HOMEM mais VELHO
#quantas mulheres tem com idade menor de 20 anos
somaidade = 0
media = 0
homemmaisvelho = 0
nomevelho = ''
total = 0
for c in range(1, 5):
    print( '************ {}ª pessoa ************'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade = somaidade + idade
    if c == 1 and sexo in 'Mm':
        homemmaisvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        total = total + 1
media = somaidade/4
print('A média de idade ente os 4 participantes é {} anos'.format(media))
print('O homem mais velho se chama {} e tem {} anos'.format(nomevelho, homemmaisvelho))
print('tem {} mulheres com menos de 20 anos.'.format(total))

