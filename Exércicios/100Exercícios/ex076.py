#crie um programa que tenha uma tulipa única com nomes de produtos e seus respectivos preços na sequência
#No final, mostre uma listagem de preços organizando os dado em forma tabular.
lista = ('Caderno', 15.90, 'Livro', 32.90, 'Lápis', 2.90, 'Mochila', 24.90,
         'Borracha', 3.59, 'Compasso', 8.99)
a = ' '
print('-='*22)
print('{} Lista de Produtos na Promoção'.format(a*7))
print('-='*22)
for p in range(0, len(lista)):
    if p % 2 ==0:
        print(f'{lista[p]:.<34}', end='')
    else:
        print(f'R$ {lista[p]:>7.2f}')
print('-=' * 22)
print('Consulte semana que vem a próxima lista.')





