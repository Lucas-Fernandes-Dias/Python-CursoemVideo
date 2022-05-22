# escreva um programa que pergunte o valor do seu salário e calcule o valor do seu aumento.
# para salários superiores a R$ 1250.00 calcule um aumento de 10%
# para salários inferiores ou iguaias a R$ 1250.00 calcule um aumento de 15%
sal = float(input('Digite o seu salário para saber o aumento que receberá:R$ '))
if sal > 1250.00:
    print('O aumento real em seu salário será de R${:.2f}'.format(sal*10/100))
if sal <= 1250.00:
    print('O aumento real em seu salário será de R${:.2f}'.format(sal*15/100))



