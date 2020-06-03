'''cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
        'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
        'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
        'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')'''

'''cont = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO',
        'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
        'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE',
        'DEZESSEIS', 'DEZESSETE', 'DEZOITO',
        'DEZENOVE', 'VINTE')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente Novamente. ', end=' ')
print(f'Você digitou o número {cont[numero]}')
'''

'''cont = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO',
        'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
        'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE',
        'DEZESSEIS', 'DEZESSETE', 'DEZOITO',
        'DEZENOVE', 'VINTE')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n > 20 or n < 0:
        print('Tente novamente. ',end='')
    elif n >= 0 <= 20:
        break
print(f'Você digitou o número {n}')'''

cont = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO',
        'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
        'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE',
        'DEZESSEIS', 'DEZESSETE', 'DEZOITO',
        'DEZENOVE', 'VINTE')

'''for c in range(0, len(cont)):
for pos, numeros in enumerate(cont):
    #print(f'{cont[c]} na posicao {c}')
    print(f'{numeros} na posicao {pos}')'''





while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if n > 20 or n < 0:
        print('Tente novamente. ', end='')
    elif n >= 0 or n <= 20:
        break
print(f'Você digitou o numero {cont[n]}')