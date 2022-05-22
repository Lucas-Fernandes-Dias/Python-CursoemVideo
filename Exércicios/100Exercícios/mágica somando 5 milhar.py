#crie um algoritmo que faça um soma de 5 centenas dar um determinado numero já pre estabelecido.
#o algoritmo vai dar uma milhar 6 digitos r logo após começa a magica.
#o algoritmo digita a primeira milhar
#o usuário digita a 2 milhar e o computador digita novamente só q agora a 3 milhar
#o usuário digita a 4 milhar e por fim o algoritmo digita a 5 e ultima milhar
#a soma deve ser o numero ja revelado pelo algoritmo anteriormente no inicio da mágica
import random
from time import sleep
comp = random.randint(20000, 29999)
resultado = (comp)
milharcomp1 = milharcomp2 = milharcomp3 = usu1 = usu2 = usu3 = 0
while True:
    resp = str(input(f'Esse \033[1:97m{resultado}\033[m será o resultado da nossa soma de 5 milhares de 4 digitos cada, quer apostar? [ S ] SIM [ N ] NÃO: '))
    if resp in 'Ss':
        print('Muito bem, vamos nessa.....')
        computador = str(resultado).strip()
        strcomp = (computador[1:])
        milharcomp1 = int(strcomp)+2
        print(f'O computador vai começar escolhendo uma milhar de 4 digitos, essa milhar é a \033[1:31m{milharcomp1}\033[m')
        print('Agora preciso que você digite uma milhar de 4 digitos qualquer, ok')
        usu1 = int(input('Digite sua milhar de 4 digitos: '))
        print(f'A sua milhar de 4 digitos foi \033[1:32m{usu1}\033[m')
        milharcomp2 = 9999- usu1
        print(f'A milhar de 4 digitos do computador foi \033[1:31m{milharcomp2}\033[m')
        usu2 = int(input('Digite sua centena: '))
        print(f'A sua milhar de 4 digitos foi \033[1:32m{usu2}\033[m')
        milharcomp3 = 9999 - usu2
        print(f'A milhar de 4 digitos do computador foi \033[1:31m{milharcomp3}\033[m')
        soma = milharcomp3 + milharcomp1 + milharcomp2 + usu3 + usu1 + usu2
        print(f'Milhar Nº1\033[1:31m {milharcomp1}\033[m\nMilhar Nº2\033[1:32m {usu1}\033[m\nMilhar Nº3\033[1:31m {milharcomp2}\033[m\nMilhar Nº4\033[1:32m {usu2}\033[m\033[m\nMilhar Nº5\033[1:31m {milharcomp3}\033[m\033[m')
        print('-'*10)
        sleep(1)
        print(f'total é \033[1:32m{soma:>7}\033[m')
    elif resp not in 'SsNn':
        print('Ditige uma resposta válida, por favor.')
    else:
        print('O programa será encerrado')
        break




