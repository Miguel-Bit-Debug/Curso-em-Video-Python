#numeros = str(input('Digite um numero de 0 a 9999: '))

#n1 = numeros[3]
#n2 = numeros[2]
#n3 = numeros[1]
#n4 = numeros[0]
#print('Unidade: {}'.format(n1))
#print('Dezena: {}'.format(n2))
#print('Centena: {}'.format(n3))
#print('Milhar: {}'.format(n4))


print(20*'=')

#codigo curso em video

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
