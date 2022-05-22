from time import sleep
a = (' '*8)
print('{}GERADOR DE PA'.format(a))
print('=-='*10)
primeiro = int(input('Digite o primeiro número: '))
raz = int(input('Digite a Razão da PA: '))
cont = 1
term = primeiro
mais = 10
total = 0
while mais != 0:
    total += mais
    sleep(1)
    while cont <= total:
        print('{} → '.format(term), end='')
        term += raz
        cont += 1
    print('Espere ...')
    sleep(1)
    mais = int(input('Quantos termos mais você gostaria de ver na tela: '))
print('Foi mostrado {} termos.'.format(total))
sleep(1)
print('FIM')
