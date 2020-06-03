'''from time import sleep

print('+-----------------+')
print('|Ola Eu Sou Watson|')
print('+-----------------+')
sleep(1)

c = 0
n = 0
s = 0
while n < 999:
    n = int(input('Digite um número: '))
    if n == 999:
        c -= 1
    c += 1
    if n != 999:
        s = n + n
print('Voce digitou {} numeros, e a soma deles é {}'.format(c, s))
'''

#codigo curso em video

num = cont = soma = 0
num = int(input('Digite um numero: [999 para parar]'))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input('Digite um numero: [999 para parar]'))
print('Você digitou {} números e a soma entre eles foi {} '.format(cont, soma))
65