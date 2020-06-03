'''matriz1 = [[], [], []]
matriz2 = [[], [], []]
matriz3 = [[], [], []]
matriz1[0].append(int(input('Digite um valor para [0, 0]: ')))
matriz1[1].append((int(input('Digite um valor para [0, 1]'))))
matriz1[2].append(int(input('Digite um valor para [0, 2]')))
for m1 in matriz1:
    print(f'{m1} ', end='')'''


'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}], [{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}], [{c}]: '))
print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()

