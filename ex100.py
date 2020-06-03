'''from random import randint
numeros = []
def sorteio():
    numeros.append(randint(0, 6))
    numeros.append(randint(0, 6))
    numeros.append(randint(0, 6))
    numeros.append(randint(0, 6))
    numeros.append(randint(0, 6))
    numeros.append(randint(0, 6))
    print(f'A lista contem {len(numeros)} números que são {numeros} ')
def par():
    par = 0
    somapar = 0
    #print('Todos números pares', end=' ')
    for num in numeros:
        if num % 2 == 0:
            par = num
            somapar += par
            #print(f'{par}', end=' ')
    #print()
    print(f'A soma de todos os valores pares de {numeros}', end=' '  f'é = {somapar}')


sorteio()
par()'''

'''from random import randint
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end=' ')
    for cont in range(0, 5):
        lista.append(randint(1, 10))
        print(f'{cont}', end=' ')
    print('PRONTO!')
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando todos os valores pares de {lista}, temos {soma}')
numeros = list()
sorteia(numeros) 
somapar(numeros)'''

'''from random import randint

l = []
def sorteia():
    print('-'*30)
    print('Sorteando valores')
    for numero in range(0, 5):
        l.append(randint(1, 10))
    print(l)
    print('-'*30)

def soma_par():
    soma = 0
    for valor in l:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando todos os números pares temos {soma}')
    print('-'*30)

sorteia()
soma_par()'''


'''from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)

def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lista}, temos {soma}')



numeros = []
sorteia(numeros)
soma_par(numeros)'''


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

#n = int(input('Digite um número: '))

f1 = fatorial(5)
f2 = fatorial(7)
f3 = fatorial(6)
print(f'Os resultados são {f1}, {f2} e {f3}')