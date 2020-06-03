"""nome = str(input('Digite o nome do aluno: ')).capitalize().strip()
nota1= float(input('Nota do primeiro bimestre: '))
nota2 = float(input('Nota do segundo bimestrte: '))
nota3 = float(input('Nota do terceiro bimestre: '))
nota4 = float(input('Nota do quarto bimestre: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print('A média do aluno é {}'.format(media))
if media <= 5.0:
    print('\033[1;31mO aluno {} está REPROVADO!!\033[m'.format(nome))
elif media <= 5.0 or media < 6.9:
    print('\033[1;33mO aluno {} está de RECUPERAÇÃO!!\033[m'.format(nome))
else:
    print('\033[1;34mE o aluno {} está APROVADO!!\033[m'.format(nome))"""

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O aluno está em recuperação.')
elif média < 5:
    print('O aluno está reprovado.')
elif média >= 7:
    print('O aluno está aprovado.')