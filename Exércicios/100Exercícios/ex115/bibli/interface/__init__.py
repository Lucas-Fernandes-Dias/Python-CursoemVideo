def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[1;33mERROR! Digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[1;33mO usuário preferiu encerrar sessão.\033[m')
            return 'indeterminado'
        else:
            return n


def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção:\033[m ')
    return opc