#faça um programa que tenha uma função chamava escreva(), que receba um texto qualquer como parametro e mostre
#uma mensagem com tamanho adaptavel.
def escreva(txt):
    print('-' * int(len(txt)))
    print(txt)
    print('-' * int(len(txt)))
escreva('Olá Mundo!')
escreva('Meu filho')
escreva('Palmeiras')