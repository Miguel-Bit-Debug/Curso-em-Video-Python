"""n1 = float(input('Primeiro seguimento: '))
n2 = float(input('Segundo seguimento: '))
n3 = float(input('Terceiro seguimento: '))

print(20*'\033[1;34m-=-\033[m')
print('analisando seguimentos')
print(20*'\033[1;34m-=-\033[m')

if n1 == n2 and n2 == n3:
    print('De acordo com os seguimentos o triângulo é um EQUILÁTERO')
elif n1 != n2 and n2 == n3:
    print('De acordo com os seguimentos o triângulo é um ISÓCELES')
else:
    print('De acordo com os seguimentos o triângulo é um ESCALENO')"""

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES')
else:
    print('Os seguimentos acima nao podem formar um triangulo')
