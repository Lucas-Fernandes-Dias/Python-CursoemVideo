#crie um programa que simule o inicio de um caixa eletronico
#mostre a pergunta q " qual valor deseja sacar"
#informe a quantidade de cedulas que vai receber
#considere o caixa com notas de R$ 50 R$ 20 R$ 10 R$ 1
a = ' '
print('-=-'*20)
print(f'{a*15}\033[1:31mBem vindo ao banco \033[1:97mAMYZO\033[m')
print('-=-'*20)
valor = int(input('Você deseja sacar quantos reais R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('Sessão finalizada com sucesso. Volte sempre!')



#print(f'\033[1:97mR$ {valor:.2f}\033[m')