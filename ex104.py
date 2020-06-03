'''def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número valido.\033[m')
        if ok:
            break
    return valor
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')'''


def leaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            of = True
        else:
            print('\033[31mErro! Digite um número inteiro\033[m')
        if ok:
            break
        return valor
num = leaint('Digite um número: ')
print(f'Você digitou o número {num}')