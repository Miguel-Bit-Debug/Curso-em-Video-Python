n = []
while True:
    num = int(input('Digite um numero: '))
    n.append(num)
    r = str(input('Quer continuar: [S/N]: '))
    if r in 'Nn':
        break
n.sort(reverse=True)
print(f'Você digitou os números {n}')
if 5 in n:
    print(f'O valor 5 foi digitado na posição {n.index(5)}')
else:
    print('O valor 5 não foi digitado')