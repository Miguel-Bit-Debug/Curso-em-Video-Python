from datetime import date

date = date.today().year
for c in range(1, 8):
    nascimento = int(input('Digite sua data de nascimento: '))
    if date - nascimento <= 17:
        print('Você é menor de idade')
    elif date - nascimento <= 21:
        print('Você é maior de idade')