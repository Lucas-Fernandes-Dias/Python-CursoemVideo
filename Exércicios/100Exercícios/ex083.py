#crie um programa onde o usuário digite uma expressão qualquer que use parenteses
#seu programa deverá analisar se a expressão é válida ou não, considerando se os parentes estão sendo abertos e fechados
#mostre a mensagem se a expressão é correta ou se a expressão é inválida.
exp = str(input('Digite uma expressão com parentes, pode ser qualquer expressão: '))
parenteses = []
for simb in exp:
    if simb == '(':
        parenteses.append(simb)
    elif simb == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(simb)
if len(parenteses) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão não é válida')


