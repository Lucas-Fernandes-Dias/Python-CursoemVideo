#adicione ao modulo moeda.py criado nos desafios anteriores, uma função chamada resumo()
#que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
from utilidadescev import moeda
from utilidadescev import dado

num = dado.leiaDinheiro('Ditige um valor R$ ')
moeda.resumo(num, 20, 12)
