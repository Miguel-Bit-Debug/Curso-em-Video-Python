'''from random import randint
from time import sleep

computador = randint(0, 11)
jogador = int(input('Em que número eu pensei? '))
print('+---------------+''\n'
      '|               |''\n'
      '|  processando  |''\n'
      '|               |''\n'
      '+---------------+''\n'.center(10))
sleep(1.5)
tentativas = 0
while jogador != computador:
    jogador = int(input('Tente novamente '))
    tentativas += 1
print('Você ganhou')
print('O número de tentativas foram {}'.format(tentativas))
'''

'''from random import randint
computador = randint(0, 10)
print('Sou seu computador acabei de pensar em um numero entre 0 e 10')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez')
        elif jogador > computador:
            print('Menos...tente mais uma vez')
print('Acertou com {} tentativas'.format(palpites))'''



'''from random import randint
from time import sleep

computador = randint(0, 11)
jogador = int(input('Em que número eu pensei? '))
print('+---------------+''\n'
      '|               |''\n'
      '|  processando  |''\n'
      '|               |''\n'
      '+---------------+''\n'.center(10))
sleep(1.5)
tentativas = 1
while jogador != computador:
    if jogador < computador:
        print('Mais..tente novamente')
    if jogador > computador:
        print('Menos...Tente novamente')
    jogador = int(input('Tente novamente '))
    tentativas += 1
print('Você ganhou')
print('O número de tentativas foram {}'.format(tentativas))'''


from time import sleep
from random import randint

computador = randint(0, 11)
tentativas = 1
print('Agora eu vou pensar em um número')
jogador = int(input('Em que numero eu pensei? '))
print('Processando')
sleep(1)
while jogador != computador:
    if jogador < computador:
        print('Mais...Tente novamente')
        tentativas += 1
        jogador = int(input('Em que numero eu pensei'))
    if jogador > computador:
        print('Menos...tente novamente')
        tentativas += 1
        jogador = int(input('Em que numero eu pensei'))
print('Oh nao você me venceu')
print('Com {} tentativas'.format(tentativas))