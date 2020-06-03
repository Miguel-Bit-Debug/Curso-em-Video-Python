#velocidade= float(input('Qual é avelocidade atual do carro? '))
#limite = (80)
#multa = (7)
#multa2 = (velocidade - limite) * multa
#if velocidade > limite:
  #  print('Você ultrapassou os limites permitidos')
 #   print('Sua velocidade foi {:.2f} e voce vai pagar R${:.2f}'.format(velocidade, multa2))
#else:
    #print('Você está dentro da velocidade')


#codigo do curso em video

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é 80km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança')