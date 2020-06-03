a = input('Digite algo:')
print('O tipo primitivo de {} é'.format(a), type(a))
print('É um número? {}'         .format(a), a.isnumeric())
print('É alfanumérico? {}'      .format(a), a.isalnum())
print('É alfabético? {}'        .format(a), a.isalpha())
print('Esta em maiusculas?{}'   .format(a), a.isupper())
print('Esta em minusculas? {}'  .format(a), a.islower())


b = int(input('Digite um número:'))
print('O tipo primitivo de {} é'.format(b), type(b))


