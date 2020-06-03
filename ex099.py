'''def valores(*num):
    #for valor in num:
    maior = menor = 0
    print('-'*30)
    print('Analisando os valores')
    print('-'*30)
    print(f'{num}\nforam os valores informados')
    print(f'E o maior numero é {max(num)}')
    print(f'E o menor numero é {min(num)}')
    print('-'*30)
    print()

valores(7, 8, 9, 6, 2, 1, 0)
valores(7, 8, 9, 1, 0)
valores(2, 1)'''


#codigo curso em video

'''def maior(*num):
    cont = maior = 0
    print('-'*40)
    print('Analisando os valores passados')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor >= maior:
                maior = valor
        cont += 1
    print(f'Foram informador {cont} valores')
    print(f'O maior valor informado foi {maior}')

#programa principal
maior(4, 8, 9, 6, 0, 1)
maior(1, 2, 3, 4, 5, 6, 7, 8, 9)
maior(3, 4, 6, 7, 8, 9)'''

'''def maior(*num):
    cont = maior = 0
    print('-'*30)
    print('Analisando os valores')
    for valor in num:

        print(valor, end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor >= maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'E o maior valor é {maior}')
maior(8, 5, 9, 6)
maior(7,0,5,6,9)'''

def maior(*num):
    print('-' * 30)
    print('Analisando os valores')

    cont = maior = 0
    for valor in num:
        print(f'{valor}', end=' ')
        if valor == 0:
            maior = valor

        else:
            if valor >= maior:
                maior = valor
        cont += 1
    print(f'Valores: {cont}')
    print(f'Maior: {maior}')

maior(8,5,9,6,3,25,7)
maior(7,5,8,4,1,2,6)
maior(8)