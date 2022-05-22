#faça um programa que leia o nome digitado e que mostre quandos vezes aparece a letra A em que posição ela
#aparece a primeira vez e em que posição ela aparece a ultima vez.
nome = str(input('Digite seu nome: ')).upper().strip()
l = 'A'
print('A primeira vez que a letra a aparece é na posição {}'.format(nome.find(l)+1))
print('A ultima vez que a letra a aparece é na posição {}'.format(nome.rfind(l)+1))


