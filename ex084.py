'''nome_peso = list()
pesadas = leves = pessoas = 0

while True:
    nome_peso.append(str(input('Nome: ')))
    nome_peso.append(float(input('Peso: ')))
    r = str(input('Quer continuar? [S/N]: '))
    pessoas += 1
    if r in 'nN':
        break
print(f'Você cadastrou {pessoas} pessoas')'''

#codigo curso em video

'''temp = list()
princ = list()
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break

print(f'Ao todo você cadastrou {princ} pessoas.')
print(f'O maior peso foi de {mai}Kg')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'O menor peso foi de {men}Kg')'''


temp = []
pessoas = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = str(input('Quer Continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')

print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')