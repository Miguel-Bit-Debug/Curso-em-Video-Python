'''palavra = ('guarana',
            'python',
            'escola',
            'refrigerante',
            'gato',
            'coemputador',
            'jogo',
            'monitor')
for p in palavra:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')'''


'''palavras = ('guarana',
            'python',
            'escola',
            'refrigerante',
            'gato',
            'computador',
            'jogo',
            'monitor')

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos ', end='')
    for letras in palavra:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')'''


palavras = ('guarana',
            'python',
            'escola',
            'refrigerante',
            'gato',
            'computador',
            'jogo',
            'monitor')

for palavra in palavras:
        print(f'\nNa palavra {palavra} temos ', end='')
        for letra in palavra:
            if letra.lower() in 'aeiou':
                print(f'{letra}', end=' ')