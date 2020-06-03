"""from time import sleep
import emoji

sleep(1)
for c in range(10, 0, -1):
    sleep(1)
    print('\033[1;31m{}\033[m'.format(c))
print('\033[1;31mBooouuuum!!!\033[m \033[1;34mBooouum!!!\033[m', end=' ')
print('\033[1;35mXablaaaaaaup\033[m \033[1;33mPooooow\033[m', end=' ')
print('Fim')"""

from time import sleep
print('-=-'*20)
print('A queima de fogos começa em...')
print('-=-'*20)
sleep(1)
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('Buuuum')