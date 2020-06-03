'''n1 = []
n2 = []
n3 = []
while True:
    num = int(input('Digite um valor: '))
    n1.append(num)
    print('Valor adicionado...')
    r = str(input('Quer continuar? [S/N]: '))
    if num % 2 == 0:
        n2.append(num)
    else:
        n3.append(num)
    if r in 'nN':
        break
print(f'Você digitou {len(n1)} valores')
print(f'Todos os valores {n1}')
print(f'todos os numeros pares {n2}')
print(f'Todos os numeros impares {n3}')'''

#codigo curso em video

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]: ')).upper()
    if resp in 'nN':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('='*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')