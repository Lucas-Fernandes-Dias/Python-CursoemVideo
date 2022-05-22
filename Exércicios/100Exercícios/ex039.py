#faça um programa que leia o ano de nascimento de um jovem e informe-o de acordo com a sua idade
#se ele ainda vai se alistar ao serviço militar
#se é a hora dele se alistar
#se já passou do tempo do alistamente.
#seu programa tem q mostrar o tempo que falta ou o tempo que já passou para o alistamento correto.

import datetime
nasc = int(input('Digite o ano de seu nascimento: '))
correto = 17
date = datetime.date.today()
year = int(date.strftime("%Y"))
idade = (year - nasc)
falta = (idade -17)
if idade == correto:
    print('Você está no ano correspondente ao ano que deve se alistar.')
elif idade > correto:
    print('Você perdeu o ano correto pra se alistar, o ano correto seria há {} anos.'.format(falta))
else:
     print('Ainda falta {} anos para você poder se alistar.'.format(abs(falta)))
