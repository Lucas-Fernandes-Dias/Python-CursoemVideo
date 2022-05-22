#faça um programa pra sorte entre os alunos um para limpar o quadro.

import random

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno:  '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno:   '))
lista = [aluno1, aluno2, aluno3, aluno4]
print('O nomes dos alunos que participaram do sorteio para limpar o quadro são: \n {} \n {} \n {} \n {}'.format(aluno1, aluno2, aluno3, aluno4))
sorteio = random.choice(lista)
print('O nome sorteado foi:',sorteio)
