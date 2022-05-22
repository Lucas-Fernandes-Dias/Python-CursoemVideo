#crie um programa que leia dois valores e mostre um menu na tela
from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
sair = 0
escolha = 0
while escolha != 6:
    print('[ 1 ] SOMAR\n[ 2 ] DIVIDIR\n[ 3 ] MULTIPLICAR\n[ 4 ] SUBTRAIR\n[ 5 ] NOVOS NÚMEROS\n[ 6 ] SAIR')
    escolha = int(input(''))
    if escolha == 1:
        soma = n1 + n2
        print('A soma {} e {} é {}.'.format(n1, n2, soma))
        sleep(1)
    elif escolha == 2:
        div = n1 / n2
        print('A dividão entre {} e {} é igual a {}'.format(n1, n2 ,div))
        sleep(1)
    elif escolha == 3:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, mult))
        sleep(1)
    elif escolha == 4:
        sub = n1 - n2
        print('A subtração dos números {} {} é igual {}'.format(n1, n2, sub))
        sleep(1)
    elif escolha == 5:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        sleep(1)
    elif escolha == 6:
        print('O programa será encerrado.')
        sleep(1)
        print('Finalizando, aguarde um momento, por favor.')
        sleep(1)
    else:
        print('Digite um número válido para executar a tarefa desejada!')
    sleep(1)
    print('=-=*'*10)
sleep(1)
print('FIM')


