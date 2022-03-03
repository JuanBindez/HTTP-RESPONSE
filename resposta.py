import requests


def statos_da_response():
    print('Status code:', response.status_code)


def cabecalho_da_pagina():
    print('Header')
    print(response.headers)


def conteudo_da_pagina():
    print('\n Content')
    print(response.content)


link = str(input('digite um link:\n'))
response = requests.get(link)

statos_da_response()
cabecalho_da_pagina()
#conteudo_da_pagina()

