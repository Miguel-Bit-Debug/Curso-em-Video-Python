#nome = (input('Digite seu nome: '))

#maiuscula = nome.upper().strip()
#quantidade = len(nome.strip())

#print('Seu nome é {} e ele tem {} letras \n'.format(maiuscula, quantidade))



#nome2 = (input('Digite seu é nome com letras maiusculas: '))

#minusculas = nome2.lower().strip()
#quantidade2 = len(nome.strip())

#print('Seu nome é {} e ele tem {} letras\n'.format(minusculas, quantidade2)


print(20*'=')


#codigo curso em video

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
