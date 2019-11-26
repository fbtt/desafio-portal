#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by Fernando Battisti
ferbattisti.eng@gmail.com
"""

# libraries importing
from googlesearch import search
  
# word to searh
query = 

# list of dict to save the responses
list_dict_responses = []

# get the responses
count = 1
for endereco_completo in search(query="telemedicina", tld="co.in", num=10, start=0, stop=100, pause=2): 
    list_dict_responses.append(
            {'posicao': count,
             'endereco_completo': endereco_completo}
    )

#    print("count = %d | endereco: %s" % (count, endereco_completo))
    count = count + 1