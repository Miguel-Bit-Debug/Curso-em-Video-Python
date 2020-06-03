'''c = 0
n = 1
soma = 0
while True:
    n1 = int(input(f'Digite {n}º número: '))
    n += 1
    if n1 == 999:
        break
    c += 1
    soma += n1
print(f'Você digitou {c} e a soma deles é {soma}')'''

#codigo curso em video
cont = 0
num = soma = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}')