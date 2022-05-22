#modifique as funções que foram cridas no desafio 107 para que elas aceitem um parâmetro a mais
#informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desnvolvida no desafio 108
import moeda

num = float(input('Ditige um valor R$ '))
print(f'Aumentado 10%, temos R$ {moeda.aumentar(num, 10, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'A metade de {moeda.moeda(num)} é {(moeda.metade(num, True))}')
print(f'Diminuindo o preço em 10%, temos {(moeda.diminuir(num, 10, True))}')
