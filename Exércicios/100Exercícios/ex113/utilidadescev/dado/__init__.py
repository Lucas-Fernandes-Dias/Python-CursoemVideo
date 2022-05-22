def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[1;31mERRO!\033[mDigite um valor monetário: ')
        else:
            valido = True
            return float(entrada)


