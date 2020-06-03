'''n = []
c = 1
while True:
    num = (int(input(f'{c}º valor: ')))
    if num not in n:
        n.append(num)
        print('Valor adicionado com sucesso...')
        c += 1
    else:
        print('Esse valor ja existe')
    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    if continuar in 'nN'.upper():
        break
print(f'Você digitou os valores {n}')'''

#codigo curso em video

num = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar')
    r = str(input('Quer continuar? [S/N]: ')).upper()
    if r in 'Nn':
        break
print('='*30)
num.sort()
print(f'Você digitou os valores {num}')
