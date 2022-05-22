def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'


def resumo(num=0, taxaa=10, taxar=5,):
    print(f'{taxaa}% de aumento: \t\t{aumentar(num, taxaa, True)}')
    print(f'O dobro de {moeda(num)} é \t{dobro(num, True)}')
    print(f'A metade de {moeda(num)} é \t{metade(num, True)}')
    print(f'{taxar}% de redução:\t\t\t{diminuir(num, taxar,True)}')



