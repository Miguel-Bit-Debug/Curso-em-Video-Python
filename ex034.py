"""salario = float(input('Quanto voce ganha? '))
aumento = salario + (salario * 15 / 100)
aumento2 = salario + (salario * 10 / 100)
if salario <= 1250:
    print('Seu salario aumentou 15% e agora você recebe R${:.2f}'.format(aumento))
else:
    print('Seu salário aumentou 10% e agora você recebe R${:.2f}'.format(aumento2))"""

salario = float(input('Qual é o salário do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))
