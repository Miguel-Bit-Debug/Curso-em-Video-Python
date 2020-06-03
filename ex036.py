"""from time import sleep

casa = float(input('Valor da casa que deseja comprar: '))

salario = float(input('Digite o valor do seu salário: '))

mensalidade = int(input('Em quantos anos você quer pagar? '))

print('\033[4;31mAnalisando...\033[m')

sleep(1.5)

prestacao = casa / (mensalidade*12)

total = salario * 30 / 100

if prestacao > total:
    print('\033[31mCom seu salario de R${:.2f} a mensalidade é R${:.2f} você nao pode comprar a casa\033[m'.format(salario, total))
else:
    print('\033[34mCom o salario de R${:.2f} a mensalidade é {:.2f} você pode comprar a casa.\033[m'.format(salario, mensalidade))"""

#codigo curso em video

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação sera de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo negado')
