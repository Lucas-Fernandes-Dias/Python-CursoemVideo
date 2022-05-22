#faça um programa que leia um nome de cidade ditado pelo usuário e que ele diga que se o nome começa com SANTO
city = str(input('Digite a cidade onde você nasceu: ')).upper().strip().split()
print('A cidade que você nasceu começa com Santo?: {}'.format('SANTO'== city[0]))






