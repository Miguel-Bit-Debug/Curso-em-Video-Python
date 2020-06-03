"""from datetime import date

nome = str(input('Digite seu nome: ')).capitalize().strip()
ano = str(input('Em que ano você nasceu {}: '.format(nome)))
idade = date.today().year - int(ano)

mirim = 'Mirim'
infantil = 'Infantil'
junior = 'Junior'
senior= 'Sênior'
master = 'Master'

print('{} sua idade é {}'.format(nome, idade))


if idade <= 9:
    print('Seja bem vindo {} você faz parte da categoria {}'.format(nome, mirim))
elif idade == 10 or idade <= 14:
    print('Seja bem vindo {} você faz parte da categoria {}'.format(nome, infantil))
elif idade <= 15 or idade <= 19:
    print('Seja bem vindo {} você faz parte da categoria {}'.format(nome, junior))
else:
    print('Seja bem vindo {} você faz parte da categoria {}'.format(nome, master))"""

from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')