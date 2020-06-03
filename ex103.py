'''def ficha(jog='desconhecido', gol=0):
    print(f'O jogador {jog} fez {gol} gols no campeonato.')

n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)'''

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} no campeonato')

jogador = str(input('Nome do jogador: '))
g = str(input('Nº de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if jogador.strip() == '':
    ficha(gol=g)

else:
    ficha(jogador, g)