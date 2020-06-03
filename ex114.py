'''import requests

def url(msg='', show=False):
    resposta = requests.get('http://pudim.com.br/')
    if resposta.status_code:
        show = True
        print(msg)

try:
    site = url('\033[33mConsegui acessar o site pudim com sucesso!\033[m')
except (ImportError):
    print('\033[31mO site pudim não está acessivel no momento.\033[m')

'''

