#crie um programa que vai ler vários números e colocar em uma lista
#depois disso, mostre
#a) quantos números foram digitados
#b) a lista de valores, ordenada de forma decrescente
#c)se o valor 5 foi digitado e está ou não na lista.
num = []
while True:
    num.append(int(input('Digite um númeor qualquer: ')))
    resp = str(input('Deseja continuar cadastrando novos números [ S ] SIM [ N ] NÃO: ')).strip().upper()
    if resp in 'Nn':
        break
print('-*'*20)
print(f'Você digitou {len(num)} elementos')
num.sort(reverse=True)
print(f'Os valores em ordem decrescente fica assim: {num}')
print('-*'*20)
if 5 in num:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte desta lista.')


