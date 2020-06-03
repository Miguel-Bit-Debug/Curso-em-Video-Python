"""soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
"""


s = 0
cont = 0

for c in range(1, 500+1, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma de todos os {} valores solicitadors é {}'.format(cont, s))
