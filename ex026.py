#frase = (input('digite uma frase: ')).strip()

#frase2 = frase.count('a', 0, 100)

#posicao = frase.find('a')
#posicao2 = frase.rfind('a')

#print('{} Tem {} letras a'.format(frase, frase2))

#print('E estão na posição {} e na posição {} '.format(posicao, posicao2))

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))
