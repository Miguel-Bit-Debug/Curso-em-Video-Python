'''jogador = {}
lista = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas ele jogou? '))
numpartida = 1
totgol = 0
for gol in range(partidas):
    numgol = int(input(f'Quantos gols ele fez na {numpartida} partida? '))

    lista.append(numgol)
    jogador['gol'] = lista[:]
    numpartida += 1
lista.clear()
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for p in range(partidas):
    print(f'Na partida {p+1} ele fez ')'''

#codigo curso em video

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c+1}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'    => na partida {i} fez {v} gols')
print(f'Foi o total de {jogador["total"]} gols')