#melhor o desafio 061, fazendo um campo de pergunta, se o usuário quer que mostre mais alguns termos da PA.
from time import sleep
print('Vamos calcular um PA!!! ')
num = int(input('Digite o Termo da PA: '))
raz = int(input('Digite a Razão da PA: '))
term = num
cont = 1
while cont <= 10:
    print('{} → '.format(term), end='')
    term += raz
    cont += 1
usuário = int(input('Deseja continuar? \n[ 1 ] SIM \n[ 2 ] NÃO.:'))
if usuário == 1:
    opção = int(input('Quantos termos você deseja ver mais sobre essa PA: \n[  5 ] TERMOS \n[ 10 ] TERMOS \n[ 15 ] TERMOS \n[ 20 ] TERMOS \n[  0 ] SAIR \n: '))
    if opção == 5:
        while cont <= 15:
            print('{} → '.format(term), end='')
            term += raz
            cont += 1
    elif opção == 10:
            while cont <= 20:
                print('{} → '.format(term), end='')
                term += raz
                cont += 1
    elif opção == 15:
        while cont <= 25:
            print('{} → '.format(term), end='')
            term += raz
            cont += 1
    elif opção == 20:
        while cont <= 30:
            print('{} → '.format(term), end='')
            term += raz
            cont += 1
    elif opção == 0:
        print('Encerrando o programa, aguarde um momento por favor....')
        sleep(1)
    else:
        print('OPÇÃO INEXISTENTE. FAVOR DIGITE UM OPÇÃO EXISTENTE DENTRO DO MENU MOSTRADO.')
else:
    sleep(1)
print('FIM')
