'''from random import randint

numero = (randint(0, 10), randint(0, 10),
          randint(0, 10), randint(0, 10),
          randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numero:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numero)}')
print(f'O menor valor sorteado foi {min(numero)}')'''

from random import randint

n = (randint(0, 10), randint(0, 10),
     randint(0, 10), randint(0, 10),
     randint(0, 10))

'''print(f'Os valores sorteados foram ', end='')
for numeros in n:
    print(f'{numeros}', end=' ')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'E o menor valor sorteado foi {min(n)}')'''

print('Os valores sorteados foram: ', end='')
for numero in n:
    print(f'{numero}', end=' ')
print()