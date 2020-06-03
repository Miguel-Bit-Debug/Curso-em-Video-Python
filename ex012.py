produto=float(input('Qual o preço do produto?'))
desconto= produto*5/100
total=produto-desconto
print('Voce pagou R${:.2f} com mais 5% de desconto você so paga o total de R${:.2f}'.format(produto, total,))






#============


# codigo curso em video

preço=float(input('Qual é o preco do produto? R$'))
novo=preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção de 5% vai custar R${}'.format(preço, novo))
