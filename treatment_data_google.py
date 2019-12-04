#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Fernando Battisti 
<ferbattisti.eng@gmail.com>
"""

# imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

# extracting the domains from the url's
list_enderecos = [item['endereco_completo'] for item in list_dict_responses]

list_aux1 = [item.replace('https://www.', '') for item in list_enderecos]
list_aux2 = [item.replace('http://www.', '') for item in list_aux1]
list_aux3 = [item.replace('https://', '') for item in list_aux2]
list_aux4 = [item.replace('http://', '') for item in list_aux3]
list_aux5 = [item.replace('www1.', '') for item in list_aux4]
list_aux6 = [item.replace('www2.', '') for item in list_aux5]
list_aux7 = [item.replace('www3.', '') for item in list_aux6]

list_domains = [item.split('/')[0] for item in list_aux7]

# getting the most frequent domains
df = pd.DataFrame(data=list_domains, columns=['domains'])
df_value_counts = df['domains'].value_counts(ascending=False)

df_most_frequent = df_value_counts.iloc[0:10]

# plotting the most frequent domains
fig = plt.figure(figsize=[10, 5])
df_most_frequent.plot.bar()
plt.title('Domínios mais frequentes', fontsize=14)
plt.xlabel('Domínio', fontsize=14)
plt.xticks(rotation=60)
plt.ylabel('Frequência', fontsize=14)
plt.tight_layout()