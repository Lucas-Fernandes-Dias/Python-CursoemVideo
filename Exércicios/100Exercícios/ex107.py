#crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), dobro() e metade().
# faça também  um programa que importe esses módulos e use algumas dessas funções
import moeda

num = int(input('Ditige um valor R$ '))
print(f'Aumentado 10%, temos R$ {moeda.aumentar(num)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'A metade de {num} é {moeda.metade(num)}')
