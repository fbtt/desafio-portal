#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Fernando Battisti 
<ferbattisti.eng@gmail.com>
"""

###########
# imports

import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
import nltk
from nltk.tokenize import word_tokenize # nltk.download('punkt')
from nltk.corpus import stopwords
import os

###########
# paths

folder_local = os.getcwd()
path_load_data = folder_local + '/data/list_google_dict_responses.data'
folder_save_fig = folder_local + '/results/'

###########
# functions

def clean_text(dirty_text: str):
    """This function clean a text converting all uppercase characters to lowercase and removing unnecessary characters

    Parameters:
        dirty_text (str): A string you want to clean

    Returns:
        str: Return a string containing the cleaned text

   """

    cleantext = (dirty_text
                .lower()
                .replace('\n', '')
                .replace('\r', '')
                .replace('\t', '')
                .replace('|', '')
                .replace('/', '')
                .replace('?', '')
                .replace('!', '')
                .replace('(', '')
                .replace(')', '')
                .replace(',', '')
                .replace('.', '')
                .replace(':', '')
                .replace(';', '')
                )

    return cleantext

def remove_stopwords(list_of_tokens: list):
    """This function remove the stopwords from a list of tokens

    Parameters:
        list_of_tokens (list): A list with the tokens

    Returns:
        list: Return a list with the stopwords removed

    """

    clean_tokens = list_of_tokens[:]

    for token in list_of_tokens:
        if token in stopwords.words('portuguese'):
            clean_tokens.remove(token)

    return clean_tokens

###########
# load the data

with open(path_load_data, 'rb') as filehandle:
    list_google_dict_responses = pickle.load(filehandle)

###########
# extract the domains from the url's

list_enderecos = [item['endereco_completo'] for item in list_google_dict_responses]

list_aux1 = [item.replace('https://www.', '') for item in list_enderecos]
list_aux2 = [item.replace('http://www.', '') for item in list_aux1]
list_aux3 = [item.replace('https://', '') for item in list_aux2]
list_aux4 = [item.replace('http://', '') for item in list_aux3]
list_aux5 = [item.replace('www1.', '') for item in list_aux4]
list_aux6 = [item.replace('www2.', '') for item in list_aux5]
list_aux7 = [item.replace('www3.', '') for item in list_aux6]

list_domains = [item.split('/')[0] for item in list_aux7]

###########
# get the most frequent domains

df = pd.DataFrame(data=list_domains, columns=['domains'])
df_value_counts = df['domains'].value_counts(ascending=False)

df_most_frequent = df_value_counts.iloc[0:10]

list_most_frequent = list(df_value_counts.index)
print(list_most_frequent)

###########
# plot the most frequent domains

fig = plt.figure(figsize=[10, 5])
df_most_frequent.plot.bar()
plt.title('Domínios mais frequentes', fontsize=14)
plt.xlabel('Domínio', fontsize=14)
plt.xticks(rotation=60)
plt.ylabel('Frequência', fontsize=14)
plt.tight_layout()

# save fig
path_save_fig = folder_save_fig + 'dominios_mais_frequentes_google.png'
plt.savefig(path_save_fig)

###########
# remove stopwords like de, não, por, a, o, etc...

# join all text in the sites and put in the variable all_text
all_text = [item['conteudo_completo'] for item in list_google_dict_responses]
all_text = " ".join(all_text)
len(all_text)

# clean the text
my_clean_text = clean_text(all_text)
len(my_clean_text)

# get the tokens of the cleaned text
tokens = word_tokenize(my_clean_text, 'portuguese')
len(tokens)

# remove stopwords from the tokens
tokens_without_sw = remove_stopwords(tokens)
len(tokens_without_sw)

# calculate the frequency of the tokens
freq = nltk.FreqDist(tokens_without_sw)

# plot word x count
fig = plt.figure(figsize=[10, 5])
freq.plot(20, cumulative=False) # plot the frequency
plt.title('Palavras mais frequentes', fontsize=14)
plt.xlabel('Palavra', fontsize=14)
plt.xticks(rotation=90)
plt.ylabel('Contagem', fontsize=14)
plt.tight_layout()

# save fig
path_save_fig = folder_save_fig + 'paravras_mais_frequentes_google.png'
plt.savefig(path_save_fig)

# list with the 100 more common words
list_more_common = list(freq.most_common())[:100]
list_more_common = [item[0] for item in list_more_common]
print(list_more_common)