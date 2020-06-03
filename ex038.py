"""valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
print(20*'\033[1;34m==\033[m')
print('\033[1;33mAnalisando\033[m')
print(20*'\033[1;34m==\033[m')

if valor1 > valor2:
    print('O primeiro valor é \033[34mMaior\033[m')
elif valor1 < valor2:
    print('O segundo valor é \033[1;34mMaior\033[m')
else:
    print('Não existe valor maior, os dois são \033[1;34mIguais\033[m')"""

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O primeiro número é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Os dois valores são iguais')
