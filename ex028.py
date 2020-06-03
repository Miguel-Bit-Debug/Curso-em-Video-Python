#from random import randint

#numero = int(input('Digite um número: '))

#num = randint(0, 5)

#if num == numero:
  #  print('Parabens voce acertou')
 #   print('O número escolhido foi {}'.format(num))
#else:
   # print('Trouxa KKKLLKLFKFLKLKLL você errou o número escolhido foi {}'.format(num))

from random import randint
from time import sleep
computador = randint(0,5) #faz o computador "pensar"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5 tente adivinhar...')
print('-=-'*20)
jogador = int((input('Em que número eu pensei? '))) #Jogador tenta adivinhar
print('Processando...')
sleep(2)
if jogador == computador:
    print('Parabéns! você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador,jogador))