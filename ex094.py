'''dados = {}
idade = []
mulher = []
soma = media = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [F/M]: '))
    while dados['sexo'] not in 'FfMm':
        dados['sexo'] = str(input('Tente Novamente. Sexo [F/M]: '))
    if dados['sexo'] == 'fF':
        mulher.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    soma = soma + dados['idade']
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'nN':
        break

print('Ao todo foram cadastras {} pessoas'.format(len(dados['nome'])))
media = soma / len(idade)
print(f'A média de pessoas do grupo é {media}')
print(f'As mulheres cadastradas foram {mulher}')
print(f'Lista de pessoas que estao acima da media e suas idades: ')
for p in idade:
    if p['idade'] > media:
        print(f'{dados["nome"]} = {dados["idade"]}')'''

#codigo curso em video

galera = []
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'mMfF':
            break
        print('Erro, Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]:')).upper()[0]
        if resp in 'SN':
            break
        print('Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista de pessoas com idade acima da media: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('Encerrado')