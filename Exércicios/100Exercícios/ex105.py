#faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
#retornar um dicionário com as seguintes informaçõe:
#a) mior note b) menor nota c)média da turma d) situação(opicional)
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: um ou mais notas dos alunos ( aceita várias).
    :param sit: valor opicional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação de turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r
resp = notas(2.8, 5.5, 8, 7.5, 9, sit=True)
print(resp)
help(notas)