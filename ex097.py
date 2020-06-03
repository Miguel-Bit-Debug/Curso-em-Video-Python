'''def escreva():
    digite = str(input('Digite: '))
    print('-' * len(digite), end='')
    print(f'\n{digite}')
    print('-'*len(digite))

escreva()'''

#codigo curso em video

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~'*tam)

escreva('miguel')
escreva('jhonson')
