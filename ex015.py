dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60)+ float(km * 0.15)
print('O total do aluguel é R$ {:.2f}' .format(pago))
