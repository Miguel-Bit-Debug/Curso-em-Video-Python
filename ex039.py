"""from datetime import date

nome = str(input('Digite seu nome: ')).capitalize().strip()
idade = int(input('Digite a idade que vai fazer ou que ja tem: '))
date = date.today().year
if idade <= 17:
    print('Você ainda é muito jovem{}'.format(nome))
elif idade == 16:
    print('Voce é um garoto ainda, faltam 2 anos para você se alistar {}'.format(nome))
elif idade > 18:
    print('Você ainda não se alistou? Que péssimo exemplo {}'.format(nome))
else:
    print('Está na hora perfeita para você se alistar {}'.format(nome))"""

from datetime import date

atual = date.today().year           #ano atual
nascimento = int(input('Ano de nascimento: '))      #ano de nascimento
idade = atual - nascimento          #calcular a idade
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))

elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
