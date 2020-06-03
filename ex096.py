'''def area():
    largura = float(input('Largura [m]: '))
    comprimento = float(input('Comprimento [m]: '))
    total = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {total}m²')
area()'''

#codigo curso em video

def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg}x{comp} é de {a}m²')


print(' Controle de Terrenos')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
