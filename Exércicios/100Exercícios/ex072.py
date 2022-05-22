'''#crie um programa que tenha uma tupla totalmente preenchida com contagem por extenso, de zero a vinte.
#Seu programa deverá ler o número digitado pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis,', 'sete', 'oite', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
teclado = int(input('Digite um número (0 a 20): '))
if teclado > 20 or teclado < 0:
    teclado = int(input('Digite um número válido entre 0 e 20: '))
for pos, n in enumerate(contagem):
    posi = pos
    if teclado == posi:
       print(f' {n}')'''
from time import sleep
contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis,',
            'sete', 'oite', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    teclado = int(input('Digite um número entre 0 e 20: '))
    if 0 <= teclado <= 20:
        print(f'Você digitou o {teclado} e esse número por extenso fica assim: {contagem[teclado]}')
    else:
        print('Tente novamente, dessa vez use um número válido. ', end='')
    resp = str(input('Você deseja continuar digitando [ S ] SIM [ N ] NÃO :  ')).strip().upper()[0]
    if resp not in 'SN':
        print('Digite uma resposta válida:')
    elif resp in 'Nn':
        print('O programa será encerrado em em seguida, aguarde por favor....')
        sleep(1)
        break
print('Fim')









