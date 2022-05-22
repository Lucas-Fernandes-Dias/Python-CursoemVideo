#desenvolva um programa que leia quatro valores pelo teclado e guarde os em uma tupla.No final, mostre
#quantas vezes apareceu o número 9
#em que posição foi digitado o primeiro valor 3
#quais foram os números pares.
num = tuple(int(input('Digite um número: '))for c in range(0, 4))
print(num,'→ ')
print(f'O número 9 foi encontrado {num.count(9)} vezes')
if num.count(3) == 0:
    print('Não foi encontrado número 3 na sequência')
else:
    print(f'Foram encontrados {num.count(3)} números 3 na sequência aparecendo a primeiro vez na posição {num.index(3)+1}º')
cont =0
for c in num:
    if c % 2 == 0:
        cont +=1
if cont == 0:
    print('Não foram encontrados números pares na sequência.')
else:
    print(f'Foram encontrados {cont} números pares, sendo eles os números: ',end='')
for c in num:
    if c % 2 == 0 :
        print(f'{c} → ', end='')
#print(f'O número 3 foi digita pela 1ª na posição {num.index(3)+1}º')
#print('Foram digitado', (n for n in num if n % 2 == 0),' números pares.')
