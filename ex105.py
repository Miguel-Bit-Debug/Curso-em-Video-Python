def notas(*n, sit=False):
    """
    -> Função para analisar notas e situções de varios alunos.
    :param n: uma ou mais notas dos alunos
    :param sit:valor opcional, indicando se deve ou nao adciconar a situacao
    :return: dicionario com varias informacoes da turma
    """
    r = {}
    r['Total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['Situação'] = 'Boa'
        elif r['media'] >= 5:
            r['Situação'] = 'Razoavel'
        else:
            r['Situação'] = 'Ruim'
    return r

resp = notas(5.5, 2.5, 8.5, 9, sit=True)
print(resp)