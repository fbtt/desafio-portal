#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by Fernando Battisti
ferbattisti.eng@gmail.com
"""

# libraries importing
from googlesearch import search
import requests
from bs4 import BeautifulSoup

# constants

NUMBER_OF_LINKS = 20
LIST_TAGS = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'li', 'table']

# functions
def make_soup(url):
    '''
        recebe a url e retorna um objeto BeatifulSoup
    '''

    html = requests.get(url).text
    return BeautifulSoup(html)

# list of dict to save the responses
list_dict_responses = []

# get the responses
count = 1
for endereco_completo in search(query="telemedicina", tld="co.in", num=10, start=0, stop=NUMBER_OF_LINKS, pause=2): 
    list_dict_responses.append(
            {'posicao': count,
             'endereco_completo': endereco_completo}
    )

#    print("count = %d | endereco: %s" % (count, endereco_completo))
    count = count + 1

#%% esse bloco de teste pega o conteudo das paginas e salva em arquivos .txt
    
# percorre todos os links
for item in list_dict_responses:
    posicao = item['posicao']
    endereco_completo = item['endereco_completo']
    soup = make_soup(endereco_completo)    
    LIST_TAGS = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'li', 'table']
    tags = soup.find_all(LIST_TAGS)

    # salva em arquivos
    path_to_save = "/home/sirius/desafio_arquivos_teste/" + str(posicao) + ".txt"
    with open(path_to_save, "w") as f:
        for tag in tags:
#            print(tag.get_text(separator=" "))
            f.write(tag.get_text(separator=" "))
            f.write('\n##########\n')
#    print("\n\n\n PASSEI AQUI \n\n\n")