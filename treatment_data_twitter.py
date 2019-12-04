#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Fernando Battisti 
<ferbattisti.eng@gmail.com>
"""

# imports
import pandas as pd
from dateutil import parser
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

# build the dataframe
columns = ['datetime', 'screen_name', 'statuses_count']
df = pd.DataFrame(columns=columns)

df['datetime'] = [item['datetime'] for item in list_dict_responses]
df['screen_name'] = [item['user']['screen_name'] for item in list_dict_responses]
df['statuses_count'] = [item['user']['statuses_count'] for item in list_dict_responses]

# calculate the users that most posted
df_value_counts = df['screen_name'].value_counts(ascending=False)
df_most_frequent = df_value_counts.iloc[0:50]

list_user_more_posts = list(df_value_counts.index)

# plot 'user' per 'number of posts'
fig = plt.figure(figsize=[10, 5])
df_most_frequent.plot.bar()
plt.title("Usuários que mais twittaram", fontsize=14)
plt.xlabel('Usuário', fontsize=14)
plt.xticks(rotation=90)
plt.ylabel('Número de postagens', fontsize=14)
plt.tight_layout()

# number of tweets for each day
# ps: analysis may be wrong because the data are unbalanced.
series_day_of_week = df['datetime'].apply(lambda x: x[0:3])
series_tweets_per_day = series_day_of_week.value_counts()

# plot 'number of tweets' per 'day of the week'
fig = plt.figure(figsize=[10, 5])
series_tweets_per_day.plot.bar()
plt.title('Número de tweets por dia', fontsize=14)
plt.xlabel('Dia da semana', fontsize=14)
plt.xticks(rotation=90)
plt.ylabel('Número de tweets', fontsize=14)
plt.tight_layout()

# number of tweets per hour
# ps: analysis may be wrong because the data are unbalanced.

df['datetime'] = df['datetime'].apply(lambda x: parser.parse(x))

series_hours = df['datetime'].apply(lambda x: '{}-{}'.format(x.day, x.hour))
series_tweets_per_hour = series_hours.value_counts()

# plot 'number of tweets' per 'hour'
fig = plt.figure(figsize=[15, 10])
series_tweets_per_hour.plot.bar()
plt.title('Número de tweets por hora', fontsize=14)
plt.xlabel('dia-hora', fontsize=14)
plt.xticks(rotation=45)
plt.ylabel('Número de tweets', fontsize=14)
plt.tight_layout()