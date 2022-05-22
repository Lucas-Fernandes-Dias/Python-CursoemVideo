#a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria de acordo com a idade
#até 9 anos MIRIM até 14 anos INFANTIL até 19 anos JUNIOR até 20 anos SENIOR acima MASTER
import datetime
nome = str(input('Digite o nome do atleta: '))
nasci = str(input('Digite a data de nascimento do atleta {}: '.format(nome))).strip()
len(nasci)
ano = int(nasci[6:])
a = ('Mirim')
b = ('Infantil')
c = ('Junior')
d = ('Senior')
mirim = 9
infantil = 14
junior = 19
senior = 20
date = datetime.date.today()
year = int(date.strftime("%Y"))
idade = (year - ano)
print('O ano de nascimento do atleta {} é {}.'.format(nome, ano))
print('A idade atual do atleta {} é {}.'.format(nome, idade))
if idade <= mirim:
    print('O atleta {} pertence a categoria \033[1:30:42m{}\033[m.'.format(nome, a.upper()))
elif idade > mirim and idade <= infantil:
    print('O atleta {} pertence a categoria \033[1:30>42m{}\033[m.'.format(nome, b.upper()))
elif idade > infantil and idade <= junior:
    print('O atleta {} pertence a categoria \033[1:30:42m{}\033[m.'.format(nome, c.upper()))
elif idade > senior:
    print('O atleta {} pertence a categoria \033[1:30:42m{}\033[m.'.format(nome, d.upper()))


