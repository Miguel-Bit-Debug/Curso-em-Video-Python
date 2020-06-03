'''situacao = {'nome': str(input('Nome: ')), 'Média': float(input('Média: '))}
print(f'O nome é igual a {situacao["nome"]}')
print(f'Sua média é igual a {situacao["Média"]}')
if situacao['Média'] <= 5:
    print('Situação: reprovado')
elif situacao['Média'] > 5 <= 6:
    print('Situação: Recuperação')
elif situacao['Média'] > 6 >= 10:
    print('Situação: Aprovado')'''


aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
