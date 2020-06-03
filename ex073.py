time = ('Palmeiras', 'Santos', 'Flamengo', 'Internacional',
        'Atlético', 'Goiás', 'Botafogo', 'Bahia', 'São Paulo',
        'Corinthias', 'Grêmio', 'Athletico-PR', 'Ceará SC',
        'Fortaleza', 'Vasco da Gama', 'Fluminense',
        'Chapecoense', 'Cruzeiro', 'CSA', 'Avaí')
print('-='*30)
print(f'Lista de times do Braseleirão: {time}')
print('-='*30)

print('Os 5 primeiros colocados são: ')
print(time[0:5])
print('-='*30)

print('Os ultimos 4 colocados são:')
print(time[-4:])
print('-='*30)

print(sorted(time))
print('-='*30)

print('O Chapecoense tá na posição ', time.index('Chapecoense')+1)
print('-='*30)