#faça um programa que leia o sexo de uma pessoa, mas só aceite valores 'M' e 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = ''
fem = ''
mas = ''
while sexo != 'MF':
    sexo = str(input('Por favor digite o sexo corretamente: ')).strip().upper()[0]
    if sexo == 'M':
       fem = ''
       mas = 'Masculino'
       print('O sexo digitado é {}.'.format(mas))
    if sexo == 'F':
       fem = 'Feminino'
       mas = ''
       print('O sexo digitado é {}.'.format(fem))
    print('FIM')