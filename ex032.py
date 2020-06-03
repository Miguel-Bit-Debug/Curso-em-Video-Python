#ano = str(input('Digite 0 para saber o ano em que você está ou digite o ano: '))
#bissexto = (int(ano + 4))
#if ano == '0':
  #  ano2 = input('Digite o ano em que você esta')
 #   print(' o ano em que voce esta é {}'.format(ano2))
#else:
    #print('Esse ano não é bissexto')

from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
