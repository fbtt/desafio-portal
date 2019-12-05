#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Fernando Battisti 
<ferbattisti.eng@gmail.com>
"""

###########
# imports

import requests
import pickle
from googlesearch import search
from bs4 import BeautifulSoup
import os

###########
# paths

folder_local = os.getcwd()
path_save_data = folder_local + '/data/list_google_dict_responses.data'

###########
# constants

NUMBER_OF_LINKS = 100
LIST_TAGS = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'li', 'table']

###########
# functions

def get_request_html_status(url: str):
    """ This funtion returns the html and the status_code of a requested url
    
    Parameters:
            url (str): The url you want to request
    Returns:
            dict(str, int): Returns a dict containing a str with the html and a int with the status_code
    """

    try:
        r = requests.get(url)
    except requests.exceptions.SSLError:
        r = requests.get(url, verify=False)
        print('Ocorreu um SSLError. Abrindo a url com requests.get(url, verify=False)')
    except Exception as error:
        print('Erro:', error)
        return None
    
    html = r.text
    status_code = r.status_code
        
    return {'html': html, 'status_code': status_code}

def get_text_from_soup(soup: BeautifulSoup, list_tags: list):
    """This function extract the text of a BeatifulSoap object based in the list_tags

    Parameters:
        soup (BeautifulSoup): A BeautifulSoup object that you want to get the text without the HTML tags
        list_tags (list): List of strings. The strings need to be the tags you want to use to extract the text

    Returns:
        str: Return a string containing the text of a BeautifulSoup

   """

    tags = soup.find_all(list_tags)
    list_of_strings = [tag.get_text(separator=' ') for tag in tags]
    conteudo_textual = ' '.join(list_of_strings)

    return conteudo_textual

###########
# get the responses

list_google_dict_responses = [] # list of dict to save the responses
count = 1
for endereco_completo in search(query="telemedicina", tld="co.in", num=10, start=0, stop=NUMBER_OF_LINKS, pause=2): 
    list_google_dict_responses.append(
            {'posicao': count,
             'status_code': None,
             'endereco_completo': endereco_completo,
             'conteudo_completo': ""}
    )
    count = count + 1

###########
# armazenar conteudo completo e status_code nos elementos da lista list_google_dict_responses[]

for item in list_google_dict_responses:
    endereco_completo = item['endereco_completo']
    
    dict_response = get_request_html_status(endereco_completo)

    if (type(dict_response) != type(None)):
        
        html = dict_response['html']
        soup = BeautifulSoup(html, 'html.parser')
        
        status_code = dict_response['status_code']
            
        item['conteudo_completo'] = get_text_from_soup(soup, LIST_TAGS)
        item['status_code'] = status_code

###########
# save the data

with open(path_save_data, 'wb') as filehandle:
    pickle.dump(list_google_dict_responses, filehandle)