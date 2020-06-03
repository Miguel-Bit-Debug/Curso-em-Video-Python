'''n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
n4 = int(input('Digite um numero: '))
tupla = (n1, n2, n3, n4)

print(f'Você digitou os números', end=' ')
print(tupla)
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram', end=' ')
for num in tupla:
    if num % 2 == 0:
        print(num, end=' ')'''

#codigo curso em video


'''num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')),)
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for n in num:
    if n % 2 ==0:
        print(n, end=' ')'''


n = (int(input('1º Valor: ')),
     int(input('2º Valor: ')),
     int(input('3º Valor: ')),
     int(input('4º Valor: ')))
'''print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 esta na {n.index(3)}')
else:
    print('O valor 3 não foi digitado')
par = 0
for numeros in n:
    if numeros % 2 == 0:
        par += 1
print('Os valores pares digitados foram: ', end='')
for num in n:
    print(f'{num}', end=' ')'''
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram ', end='')
for v in n:
    if v % 2 == 0:
        print(v, end=' ')