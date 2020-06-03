valores = []
maior = 0
menor = 0
for v in range(0, 5):
    valores.append(int(input('Digite um valor para a posição {}: '.format(v))))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]

print('Você digitou os valores {}'.format(valores))
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, c in enumerate(valores):
    if c == maior:
        print(f'{i}', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições', end=' ')
for i, c in enumerate(valores):
    if c == menor:
        print(f'{i}', end=' ')
print()