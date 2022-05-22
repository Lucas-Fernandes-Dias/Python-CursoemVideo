#crie um programa que leia números pelo teclado e que faça a média entre os números digitados
#pergunte se o usuário que digitar mais números
#mostre o maior e o menor número digitados.

print('Escolha uma opção abaixo para continuarmos \n[ 1 ] Digitar um número \n[ 2 ] Sair')
escolha = int(input('Digite sua escolha: '))
maior = menor = soma = cont = num = 0
if escolha == 1:
    alt = 'S'
    while alt == 'S':
        num = int(input('Digite um número inteiro qualquer: '))
        soma += num
        cont += 1
        alt = str(input('Você quer continuar [ S/N ]: ')).upper().strip()
        if cont == 1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
    media = soma / cont
    print('A média dos números digitados é {:.0f}'.format(media))
    print('O maior número digitado foi {}'.format(maior))
    print('O menor número digitado foi {}'.format(menor))
if escolha != 1 and escolha != 2:
    print('Digite uma escolha válida!!!')
else:
    print('FIM')

