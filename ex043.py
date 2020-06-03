"""nome = str(input('Digite seu nome: ')).capitalize().strip()
peso = float(input('Digite seu peso {}: '.format(nome.capitalize().strip())))
altura = float(input('Digite sua altura {}: '.format(nome)))

imc = peso / (altura*altura)
if imc <= 18.5:
    print('Seu IMC é {:.2f}'.format(imc))
    print('{} você está abaixo do peso procure um nutricionista para cuidar da sua saúde!'.format(nome))

elif imc == 18.6 or imc <= 25:
    print('Seu IMC é {:.2f}'.format(imc))
    print('{} Você está no seu peso ideal'.format(nome.capitalize()))

elif imc == 25 or imc <= 30:
    print('Seu IMC é {:.2f}'.format(imc))
    print('{} você está acima do peso'.format(nome.capitalize()))

elif imc == 30 or imc <= 40:
    print('Seu IMC é {:.2f}'.format(imc))
    print('{} você está obeso(a) procure se exercitar!'.format(nome.capitalize()))

else:
    print('Seu IMC é {:.2f}'.format(imc))
    print('{} você está MUITO OBESO(A) procure um nutricionista urgente! Cuide da sua saude!'.format(nome.capitalize()))"""

#codigo curso em video

peso = float(input('Qual é seu peso? (KG)'))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O imc dessa pessoas é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal.')
elif 18.5 <= imc < 25:
    print('Você está na faixa de peso normal')
elif 25 <= imc < 30:
    print('Você está em sobrepeso')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado')
