import random

n1 = str(input('Primeiro aluno: '))
n2 = str (input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação sera ')
print(lista)



print(20*'=')


#=========================






from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno'))
aleatorio = [n1, n2, n3, n4]
shuffle(aleatorio)
print('A ordem de apresentacao sera {}'.format(aleatorio))