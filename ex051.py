"""s = int(input('Informe um número: '))
for c in range(1, s, 2):
    s = c + 1
    print(s)"""

#codigo curso em video
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' ¬ ')
print('Acabou')