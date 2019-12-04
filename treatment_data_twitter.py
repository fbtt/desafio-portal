#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Fernando Battisti 
<ferbattisti.eng@gmail.com>
"""

###########
# imports

import pandas as pd
from dateutil import parser
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

###########
# paths

folder_local = '/home/sirius/Documents/'
folder_save_fig = folder_local + 'desafio-portal/results/'

###########
# functions

def barplot(series, figsize: list, title: str, xlabel: str, ylabel: str, rotation: int):
    """ This funtion plot a barplot based on data in the series parameter

    Parameters:
            series (pd.Series): A pd.Series with the data to plot
            figsize (list): A list with the values of the figure
            title (str): A string with the title of the figure
            xlabel (str): A string with the xlabel of the figure
            ylabel (str): A string with the ylabel of the figure
            rotation (int): A int value with the number of degrees to rorate the xlabels

    Returns:
            None
    """

    plt.figure(figsize=figsize)
    series.plot.bar()
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=14)
    plt.xticks(rotation=rotation)
    plt.ylabel(ylabel, fontsize=14)
    plt.tight_layout()

    return None

###########
# build the dataframe

columns = ['datetime', 'screen_name', 'statuses_count']
df = pd.DataFrame(columns=columns)

df['datetime'] = [item['datetime'] for item in list_dict_responses]
df['screen_name'] = [item['user']['screen_name'] for item in list_dict_responses]
df['statuses_count'] = [item['user']['statuses_count'] for item in list_dict_responses]

###########
# calculate the users that most posted

df_value_counts = df['screen_name'].value_counts(ascending=False)
series_most_frequent = df_value_counts.iloc[0:50]

list_user_more_posts = list(df_value_counts.index)

# plot 'user' per 'number of posts'

barplot(series=series_most_frequent,
        figsize=[10, 5],
        title="Usuários que mais twittaram",
        xlabel='Usuário',
        ylabel='Número de postagens',
        rotation=90
        )

# save fig
path_save_fig = folder_save_fig + 'usuarios_que_mais_twittaram.png'
plt.savefig(path_save_fig)

###########
# calculate the number of tweets per day
# ps: analysis may be wrong because the data are unbalanced.

series_day_of_week = df['datetime'].apply(lambda x: x[0:3])
series_tweets_per_day = series_day_of_week.value_counts()

# plot 'day of week' per 'number of tweets'

barplot(series=series_tweets_per_day,
        figsize=[10, 5],
        title='Número de tweets por dia',
        xlabel='Dia da semana',
        ylabel='Número de tweets',
        rotation=90
        )

# save fig
path_save_fig = folder_save_fig + 'numero_de_tweets_por_dia.png'
plt.savefig(path_save_fig)

###########
# calculate number of tweets per hour
# ps: analysis may be wrong because the data are unbalanced.

df['datetime'] = df['datetime'].apply(lambda x: parser.parse(x))

series_hours = df['datetime'].apply(lambda x: '{}'.format(x.hour))
series_tweets_per_hour = series_hours.value_counts()

# plot 'number of tweets' per 'hour'

barplot(series=series_tweets_per_hour,
        figsize=[15, 10],
        title='Número de tweets por hora',
        xlabel='hora',
        ylabel='Número de tweets',
        rotation=45
        )

# save fig
path_save_fig = folder_save_fig + 'numero_de_tweets_por_hora.png'
plt.savefig(path_save_fig)