'''lista = ('Lápis', 1.75,
         'Caneta', 2.50,
         'Caderno', 15,
         'Borracha', 2)
print('Listagem de preços\n')
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
         print(f'R${lista[pos]:.2f}')



listagem = ('lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')'''



'''lista = ('borracha', 2,
         'lapis', 1.50,
         'mochila', 30,
         'caderno', 15)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print('{:.<30}'.format(lista[c]), end=' ')
    else:
            print(f'R${lista[c]:.2f}')'''


material = ('borracha', 1,
            'lapis', 2,
            'caderno', 15,
            'bolsa', 30,
            'caneta', 3)
print('-='*25)
listagem = 'Listagem de material'
print(f'{listagem:^45}')
print('-='*25)

for materiais in range(0, len(material)):
    if materiais % 2 == 0:
        print(f'{material[materiais]:.<30}', end=' ')
    else:
        print(f'R${materiais:.2f}')