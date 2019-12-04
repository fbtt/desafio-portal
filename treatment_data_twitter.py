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

# build the dataframe
columns = ['datehour', 'screen_name', 'statuses_count']
df = pd.DataFrame(columns=columns)

df['datehour'] = [item['datehour'] for item in list_dict_responses]
df['screen_name'] = [item['user']['screen_name'] for item in list_dict_responses]
df['statuses_count'] = [item['user']['statuses_count'] for item in list_dict_responses]

# calculate the users that most posted
df_value_counts = df['screen_name'].value_counts(ascending=False)
df_most_frequent = df_value_counts.iloc[0:50]

list_user_more_posts = list(df_value_counts.index)

# plot user x number of posts
fig = plt.figure(figsize=[10, 5])
df_most_frequent.plot.bar()
plt.title("Usuários que mais twitaram contendo o termo 'telemedicina'", fontsize=14)
plt.xlabel('Usuário', fontsize=14)
plt.xticks(rotation=90)
plt.ylabel('Número de postagens', fontsize=14)
plt.tight_layout()