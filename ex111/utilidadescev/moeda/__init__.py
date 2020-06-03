def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(preco)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(preco)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'O dobro do preço: \t{dobro(preco*2, True)}')
    print(f'A metade do preco: \t{metade(preco/2, True)}')
    print(f'Com taxa de aumento: {aumentar(preco, taxaa, True)}')
    print('-'*30)