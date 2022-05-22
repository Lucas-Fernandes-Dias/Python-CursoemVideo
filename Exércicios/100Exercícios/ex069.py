#crie um programa que leia a idade e o sexo de várias pessoas a cada pessoa cadastrada o programa precisa perguntar
#se o usuário quer continuar cadastrando novas pessoas
#mostre quantas pessoas tem 18 anos  quantos homens foram cadastrados quantas mulheres tem menos que 20 anos
from time import sleep
mas = fem = pes = mulher = total =0
a = ' '
print('-=-'*15)
print(f'{a*10}CADASTRAMENTO DE PESSOAS')
print('-=-'*15)
while True:
    sexo = str(input('Qual é o sexo [ M ] [ F ]: ')).strip().upper()[0]
    total += 1
    if sexo in 'MF':
        if sexo == 'M':
            mas += 1
        idade = int(input('Qual a idade: '))
        if idade > 18:
            pes += 1
        if idade < 20 and sexo == 'F':
            mulher += 1
        print('-=-'*20)
        resp = str(input('Deseja continuar cadastrando? [ S ] Sim [ N ] Não: ')).strip().upper()[0]
        print('-=-'*20)
        if resp == 'N':
            break
        if resp not in 'SN':
            resp = str(input('Deseja continuar cadastrando? [ S ] Sim [ N ] Não: ')).strip().upper()[0]
            print('-=-'*20)
print('Processando......')
print('-=-'*45)
print(f'Teve {total} pessoas cadastradas sendo {pes} com mais de 18 anos e dessas pessoas cadastradas {mas} são homens e {mulher} são mulheres com menos de 20 anos.')
print('-=-'*45)
sleep(1)
print('Encerrando, aguarde um momento.....')
sleep(1)
print('-=-'*12)
print('Fim')
print('-=-')

