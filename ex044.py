"""compra = float(input('Digite o valor a ser pago: '))
pagamento = str(input('Digite a forma de pagamento: '))

dinheiro = compra - (compra * 10 / 100)
cartao = compra - (compra * 5 / 100) #pode ser debito ou credito
duas_vezes = compra / 2# normal em 2x vezes
tres_vezes = (compra + (compra * 20 / 100)) / 3

if pagamento == 'dinheiro':
    print('A vista seu produto de R${:.2f} sai com 10% de desconto e fica R${:.2f}'.format(compra, dinheiro))
elif pagamento == 'cartao de credito' or compra == 'cartao de debito':
    print('A vista no cartão sua compra de R${:.2f} sai com 5% de desconto e fica R${:.2f}'.format(compra, cartao))
elif pagamento == 'duas vezes' or compra == 'duas vezes no cartao':
    print('Você parcelando em duas vezes a compra de R${:.2f} fica R${:.2f}'.format(compra, duas_vezes))
else:
    print('Você parcelando em três vezes a compra de R${:.2f} ')and ''
    print('fica três parcelas de {:.2f} somando 20% de juros'.format(compra, tres_vezes))"""

#codigo curso e video



print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$'))
print('''FOMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO INVALIDA DE PAGAMENTO TENTE NOVAMENTE')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))
