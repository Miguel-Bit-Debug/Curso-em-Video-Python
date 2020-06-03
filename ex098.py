'''from time import sleep
def contador():
    for i in range(0, 11):
        print(i, end=' ')
    print('\n')
    print('-'*30, '\n')
    for i in range(10, 0, -2):
        print(i, end=' ')
    print('\n')
    print('-'*30, '\n')
    inicio = int(input('Qual o inicio? '))
    fim = int(input('Qual o fim? '))
    passo = int(input('Qual o passo? '))
    for i in range(inicio, fim, passo):
        print(i, end=' ')


contador()'''

#codigo curso em video
from time import sleep
def contador(i, f, p):
    print('-'*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            cont += 1
            sleep(0.5)
        print('FIM')
    else:
        cont = i
        if p < 0:
            p *= -1
        if p == 0:
            p = 1
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            cont -= p
            sleep(0.5)
        print('FIM')
        print('-'*20)
contador(1, 10, 1)
contador(10, 0, 2)
print('-'*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
