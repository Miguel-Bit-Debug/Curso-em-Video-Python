'''def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor de um fartorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(f'x', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f


print(fatorial(5, show=False))'''


'''def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(f'x', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f
print(fatorial(5, show=True))'''

def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            elif c <= 1:
                print('=', end=' ')
        f *= c
    return f

print(fatorial(5, show=True))