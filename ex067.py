'''n = 1
c = 0
n1 = int(input('Digite um número para ver sua tabuada: '))
while True:
    n += 1
    c += 1
    if n1*c >= 999:
        break
    print(f'{n1} x {c} = {n1*c}')'''


'''c = 0
produto = 1
n1 = int(input('Quer ver a tabuada de qual valor? '))
while True:
    print(f'{n1} x {produto} = {n1 * produto}')
    produto += 1
    c += 1
    if n1 <= 1:
        print('Programa tabuada encerrado. Volte sempre')
        break'''


#codigo curso em video

'''while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('Programa tabuada tabuada encerrado. Volte sempre')
'''


while True:
    n1 = int(input('Digite um numero para ver sua tabuada: '))
    if n1 < 0:
        break
    for num in range(1, 11):
        print(f'{n1} x {num} = {n1*num}')
print('Prorama de tabuada encerrado. Volte sempre')