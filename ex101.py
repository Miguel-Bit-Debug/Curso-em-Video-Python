'''from datetime import date
def voto():
    atual = date.today().year
    print('-'*35)
    nasc = int(input('Em que ano você nasceu? '))
    idade = atual - nasc
    if idade >= 18 <= 64:
        print(f'Você tem {idade} anos. ', end='')
        print('Voto obrigatorio')
    elif idade < 18:
        print(f'Você tem {idade} anos. ', end='')
        print('Voto Negado')
    elif idade > 65:
        print(f'Você tem {idade} anos. ', end='')
        print('Voto Opcional')
voto()'''

#codigo curso em video

'''def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos: NÃO VOTA.'
    elif idade >= 16 < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        f'COM {idade} anos: VOTO OBRIGATÓRIO'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))'''

from datetime import date

def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif idade >= 16 < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))