'''num = []
valores = []
par = []
impar = []
for n in range(1, 8):
    num.append(int(input(f'Digite {n}º número: ')))
    valores.append(num[:])

    for n in num:
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    num.clear()


print(f'{par}')
print(f'{impar}')
print(f'Todos os valores {valores}')'''

'''numeros = []
num = []
par = []
impar = []
for numero in range(1, 8):
    numeros.append(int(input(f'Digite o {numero}º número: ')))
    for n in numeros:
        if n % 2 == 0:
            par.append(n)
        elif n % 2 == 1:
            impar.append(n)
    num.append(numeros[:])
    numeros.clear()
print(f'Todos os valores {num}')
print(f'Todos os valores pares {par}')
print(f'Todos os valores impares {impar}')'''

#codigo curso em video

'''num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Todos os valores {num}')'''

'''num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c} valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    elif valor % 2 == 1:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Todos os valores pares {num[0]}')
print(f'Todos os valores impares {num[1]}')'''

num = [[], []]
valor = 0
for c in range(1, 5):
    valor = int(input(f'Digite o {c}º número: '))
    if valor % 2 == 0:
        num[0].append(valor)
    elif valor % 2 == 1:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Todos os valores pares {num[0]}')
print(f'Todos os valores impares {num[1]}')
