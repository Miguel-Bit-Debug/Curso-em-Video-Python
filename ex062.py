primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} ➡'.format(termo), end='')
        termo = termo + razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressao finalizada com {} termos'.format(total))