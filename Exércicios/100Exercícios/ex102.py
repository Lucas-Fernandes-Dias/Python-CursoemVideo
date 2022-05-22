#Crie um programa que tenha um função fatorial() que receba dois parâmetros: o primeiro que indique o numero a calcular
# o outro chamado show, que será um valor lógico(opicional) indicando se será mostrado ou não na tela o processo fatorial
def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#Programa principal
print(fatorial(5, show=True))


