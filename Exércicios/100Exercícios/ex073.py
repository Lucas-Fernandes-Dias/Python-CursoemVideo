#crie um programa que leia uma tupla
#a tupla deve conter os 20 primeiros colocados do brasileirão
#mostre os 5 primeiro --- os 4 ultimos ------- times em orden alfabética ----- em que posição está a palmeiras.
times = ('corinthians', 'bragantino', 'atlético mineiro', 'coritiba', ' são paulo',
         'santos', 'cuiabá', 'internacional', 'avai', 'américa mineiro',
         'palmeiras', 'flamengo', 'botafogo', 'fluminense', 'ceara',
         'atlético paranaense', 'atlético goianiense', 'goias', 'juventude', 'fortaleza')
print('-=-'*25)
print(f'\033[1:31mtabela do BRASILEIRÃO: \033[1:97m{times}\033[m')
print('-=-'*25)
print(f'\033[1:31mOs 5 primeiros do BRASILEIRÃO são: \033[1:97m{times[0:5]}\033[m')
print('-=-'*25)
print(f'\033[1:31mOs 4 últimos da tabela do  BRASILEIRÃO são: \033[1:97m{times[-4:]}\033[m')
print('-=-'*25)
print(f'\033[1:31mO Palmeiras se encontra : \033[1:97m{times.index("palmeiras")+1}ª\033[m')
print('-=-'*25)


