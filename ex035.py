print('Analisador de Triangulos')
r1 = float(input('primeiro seguimento: '))
r2 = float(input('segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo')
else:
    print('Os seguimentos acima nao podem formar um triângulo')
