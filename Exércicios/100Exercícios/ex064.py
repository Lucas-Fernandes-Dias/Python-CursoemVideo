#crie um progrma que leia números inteiro pelo teclado, e pare somente quando for digitado 999
a = (' '*7)
n = cont = soma = 0
n = int(input('Digite um número inteiro qualquer: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número inteiro qualquer: '))
print('-*-'*20)
print('{} Você digitou {} números e a soma deles é {}.'.format(a, cont, soma))
print('-*-'*20)
print("fim")