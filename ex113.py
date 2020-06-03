def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'Entrada de dados interrompida pelo usuario')
            break
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print(f'ERRO! O usuario deve informar apenas valores reais')
        except (ZeroDivisionError):
            print('Não é possivel fazer divisão por zero!')
            continue
        else:
            return n


num1 = leiaint('Digite um numero inteiro: ')
num2 = leiafloat('Digite um numero Real: ')
print(f'O número digitado foi {num2}')
print(f'O número digitado foi {num1}')