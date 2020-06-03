maior_peso = 0
menor_peso = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(p)))
    if p == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('O menor peso é {:.2f}Kg e o maior peso é {:.2f}Kg'.format(menor_peso, maior_peso))

# codigo curso em video
"""maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi e {}Kg'.format(peso))"""


