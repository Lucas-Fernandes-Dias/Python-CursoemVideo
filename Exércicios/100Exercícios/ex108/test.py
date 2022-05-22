#adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar
#numeros como um valor monetário formatado.
import moeda

num = float(input('Ditige um valor R$ '))
print(f'Aumentado 10%, temos R$ {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'Diminuindo o preço em 10%, temos {moeda.moeda(moeda.diminuir(num, 10))}')