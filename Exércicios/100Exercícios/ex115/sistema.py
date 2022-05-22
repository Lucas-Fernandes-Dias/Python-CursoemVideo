from bibli.interface import *
from time import sleep
from bibli.arquivo import *

arq = 'cursosemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #Opção cadastrar novas pessoas
        cabecalho('NOVO CADASTRO')
        nome = str(input('Digite o nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #opção para sair do sistema.
        cabecalho('\033[1:97mSaindo do Sitema..... \033[m\n\033[33mAguarde enquanto sistema é encerrado.\033[m')
        break
    else:
        #Digitou a opção errada no menu
        print('\033[1;31mERROR! Digite uma opção válida.\033[m')
    sleep(1)





