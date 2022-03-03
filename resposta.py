"""pip install requests
   pip install beautifulsoup4"""

import requests
import os
import time
from bs4 import BeautifulSoup


def status_da_response():
    print('Status code:', response.status_code)


def cabecalho_da_pagina():
    print('Header')
    print(response.headers)


def conteudo_da_pagina():
    print('\n Content')
    print(response.content)

    

link = str(input('digite um link:\n'))
response = requests.get(link)

status_da_response()
#cabecalho_da_pagina()
#conteudo_da_pagina()


site = BeautifulSoup(response.text, 'html.parser')
teste = site.find('div')
print(teste)

#attrs={'class': ''}
