"""div = 0
for c in range(1, 10):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        print()"""

#codigo curso em video

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('Por isso ele é Primo')
else:
    print('Por isso ele não é Primo')
