#crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), dobro() e metade().
# faça também  um programa que importe esses módulos e use algumas dessas funções
import moeda

num = float(input('Ditige um valor R$ '))
print(f'Aumentado 10%, temos R$ {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'Diminuindo o preço em 10%, temos {moeda.moeda(moeda.diminuir(num, 10))}')