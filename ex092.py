'''from datetime import date

atual = date.today().year
dados = {}
dados['nome'] = str(input('Nome: '))
dados['idade'] = int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contrataçao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['idade'] = atual - dados['idade']
    dados['aposentadoria'] = dados['idade'] + 35
    for chaves, valores in dados.items():
        print(f'{chaves} tem o valor {valores}')
else:
    dados['idade'] = atual - dados['idade']
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')'''

'''atual = date.today().year
dados = {'nome': str(input('Nome: ')),
         'idade': int(input('Ano de nascimento: ')),
         'ctps': int(input('Carteira de trabalho (0 não tem): ')),
         'contratação': int(input('Ano de contratação: ')),
         'salário': int(input('Salário: ')),}
dados['idade'] = atual - dados['idade']
dados['apsoentadoria'] = dados['idade'] + 35
if dados['ctps'] != 0:'''

from datetime import datetime

'''dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimentos: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salario: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

print('-='*30)
for k, v in dados.items():
    print(f'-{k} tem o valor {v}')'''

dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho: '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-='*30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
