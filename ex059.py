'''n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
print(Escolha uma opção:
[ 1 ]Somar
[ 2 ]Multiplicar
[ 3 ]Maior
[ 4 ]Novos Número
[ 5 ]Sair do programa.center(10))
menu = [1, 6]
escolha = int(input('Digite sua escolha: '))
while escolha not in menu:
    if escolha == 1:
        escolha = n1 + n2
    if escolha == 2:
        escolha = n1 * n2
    if escolha == 3:
                print(n1)
    if escolha == 4:
        print('')'''

'''from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print(Escolha uma opção:
    [ 1 ]Somar
    [ 2 ]Multiplicar
    [ 3 ]Maior
    [ 4 ]Novos Número
    [ 5 ]Sair do programa)
    opcao = int(input('Qual sua opção? '))
    sleep(1)
    if opcao == 1:
        soma = n1 +n2
        print('{} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('{} x {} = {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('entre {} e {} O maior número é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando')
    else:
        print('Opção invalida. Tente novamente')
    print('-=-'*10)
    sleep(1)
print('Fim do programa. Volte sempre')'''

from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('''Escolha uma opção:
    [ 1 ]Somar
    [ 2 ]Multiplicar
    [ 3 ]Maior
    [ 4 ]Novos Número
    [ 5 ]Sair do programa''')
menu = [1, 6]
opcao = 0
while opcao != 5:
    opcao = int(input('Escolha uma opção acima: '))
    if opcao == 1:
        soma = n1 + n2
        print('+--------------+\n'
              '|              |\n'
              '|  {} + {} = {}  |\n'
              '|              |\n'
              '+--------------+'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        produto = n1 * n2
        print('+--------------+\n'
              '|              |\n'
              '|  {} x {} = {}  |\n'
              '|              |\n'
              '+--------------+'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        opcao = 3
        if n1 > n2:
            print('+--------------+\n'
                  '|   O maior    |\n'
                  '|   Número é   |\n'
                  '|     {}        |\n'
                  '+--------------+'.format(n1))
        if n1 < n2:
            print('+--------------+\n'
                  '|   O maior    |\n'
                  '|   Número é   |\n'
                  '|      {}       |\n'
                  '+--------------+'.format(n2))
        if n1 == n2:
            print('O maior numero é...')
            sleep(2)
            print('Não existe o maior número, os dois são iguais.')
    elif opcao == 4:
        opcao = 4
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opcao == 5:
        opcao = 5
        print('Finalizando...')
        sleep(1.2)
    else:
        print('Opção invalida tente novamente')
print('Volte sempre!')