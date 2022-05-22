#crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999
# que é a condição de parada. No final mostre quantos números foram digitados e a soma de todos desconsiderando o flag.
soma = cont = 0
while True:
    num = int(input('Digite um número inteiro qualquer: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Você digitiou \033[1:97m{cont}\033[m e a soma deles é \033[1:97m{soma}\033[m.')
