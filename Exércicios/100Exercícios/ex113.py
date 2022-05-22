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


def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('\033[1;33mERROR! Digite um número real válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[1;33mO usuário preferiu encerrar sessão.\033[m')
            return 'indeterminado'
        else:
            return n


num = leiaInt('Digite um valor qualquer: ')
print(f'O valor digitado foi {num}')
n1 = leiaFloat('Digite um número real: ')
print(f'O valor digitado foi {n1}')