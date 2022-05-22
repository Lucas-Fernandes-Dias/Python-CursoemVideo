#crie um progrmaa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no fina de acordo com a média atingida
# média abaixo de 5.0 REPROVADO
#média entre 5.0 e 6.9 RECUPERAÇÃO
# média acima ou igual a 7.0 APROVADO
aluno = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a primeira nota do {}: '.format(aluno)))
n2 = float(input('Digite a segunda nota do {}: '.format(aluno)))
n3 = float(input('Digite a terceira nota do {}: '.format(aluno)))
print('A primeira nota foi {:.2f} a segunda nota foi {:.2f} e a terceira nota foi {:.2f}.'.format(n1, n2, n3))
A = ['n1', 'n2', 'n3']
len([A])
media = (n1 + n2 + n3)/len(A)
print('Sua média foi de {:.2f} nesse semestre, espere para saber se foi APROVADO, REPROVADO ou RECUPERAÇÃO.'.format(media))
if media < 5:
    print('Sua média foi de {:.2f} e por isso você está \033[1:31:107mREPROVADO\033[m esse semestre!'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi de {:.2f} e por isso você está de \033[1:33:107mRECUPERAÇÃO\033[m nesse semetre!'.format(media))
elif media >= 7:
    print('\033[1:32:107mAPROVADO\033[m nesse semestre, \033[1:32:107mPARABÉNS\033[m')
else:
    print('Consulte seu professora para saber mais sobre sua média')
