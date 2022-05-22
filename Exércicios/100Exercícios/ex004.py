#dissecando uma variável
#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.
inf = input('Digite algo que lhe venha a cabeça: ')
a = type(inf)
b = inf.isupper()
c = inf.isdecimal()
d = inf.isalnum()
e = inf.isalpha()
f = inf.islower()
print('O tipo primitivo do que foi digitado é: {}'.format(a))
print('O que foi digitado esta tudo em maiusculo? {}'.format(b))
print('O que foi digitado é decimal? {}'.format(c))
print('O que foi digitado é alfanumerico? {}'.format(d))
print('O que foi digitado é alfabetico? {}'.format(e))
print('O que foi digitado esta tudo em minusculo? {}'.format(f))

