#desenvolva um programa  que leia seis numeros inteiros e mostre na tela a soma apenas daqueles que forem pares
#se o valor digitador for impar, desconsidere-o
soma = 0
count = 0
count1 = 0
for c in range(1, 7):
    numero =int(input('Digite um número inteiro qualquer: '))
    count1 = count1 + 1
    if numero % 2 == 0:
       soma = soma + numero
       count = count + 1
print('A soma dos \033[1:97m{}\033[m números pares contigos nos \033[1:32m{}\033[m digitados é \033[1:97m{}\033[m'.format(count, count1, soma))

