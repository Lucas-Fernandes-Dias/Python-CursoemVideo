#crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
#retornando um valor literal indicando se uma pessoa tem voto negado, opicional e obrigatório nas eleições.

def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento
    if idade < 16:
        return f'Com {idade} Não vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} o Voto Facultativo'
    else:
        return f'Com {idade} o é Vota Obrigatório'
data = int(input('Digita o ano de nascimento: '))
print(voto(data))

