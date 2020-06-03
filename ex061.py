primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
while c <= 10:
    print('{} ➡'.format(termo), end='')
    termo = termo + razao
    c += 1
print('FIM')