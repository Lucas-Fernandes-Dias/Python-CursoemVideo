#dentro do pacote utilidadescev que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheir()
#que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

from utilidadescev import moeda
from utilidadescev import dado

num = dado.leiaDinheiro('Digite um valor R$ ')
moeda.resumo(num, 20, 12)
