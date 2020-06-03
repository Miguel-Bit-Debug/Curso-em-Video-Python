'''sexo = ''.capitalize()
f = 'f'.capitalize()
m = 'm'.capitalize()
while sexo == '':
    s = str(input(('Informe seu sexo [M/F]: '))).capitalize()
    if s == f:
        sexo = f
        print('Você é uma mulher')
    if s == m:
        sexo = m
        print('Você é um homem')
    else:
        print('Comando invalido tente novamente')'''

'''sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'mMfF':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} Registrado com sucesso'.format(sexo))
'''
'''sexo = ''.capitalize()
f = 'F'.capitalize()
m = M = 'M'.capitalize()
while sexo == '':
    s = str(input('Informe seu sexo: [F/M] ')).capitalize()
    if s == f:
        sexo = f
        print('Você é uma mulher')
    if s == m:
        sexo = m
        print('Você é um homem')

'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'mMfF':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} Registrado com sucesso'.format(sexo))