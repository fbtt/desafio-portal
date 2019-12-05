# -*- coding: utf-8 -*-

"""
created by Fernando Battisti
ferbattisti.eng@gmail.com
"""

###########
# imports

from TwitterSearch import TwitterSearchOrder, TwitterSearch, TwitterSearchException
import json
import pickle
import os

###########
# paths

folder_local = os.getcwd()
path_credentials = folder_local + '/twitter_credentials.json'
path_save_data = folder_local + '/data/list_twitter_dict_responses.data'

###########
# number of tweets to get

NUMBER_OF_TWEETS = 1000

###########
# get twitter credentials

with open(path_credentials, 'r') as json_file:
    data = json.load(json_file)

    CONSUMER_KEY = data['CONSUMER_KEY']
    CONSUMER_SECRET = data['CONSUMER_SECRET']
    ACCESS_TOKEN = data['ACCESS_TOKEN']
    ACCESS_SECRET = data['ACCESS_SECRET']

###########
# get the tweets and put in the list list_twitter_dict_responses

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['telemedicina'])

    ts = TwitterSearch( # create a TwitterSearch object
        consumer_key = CONSUMER_KEY,
        consumer_secret = CONSUMER_SECRET,
        access_token = ACCESS_TOKEN,
        access_token_secret = ACCESS_SECRET
     )

    # insert the results in a list of dictionaries

    list_twitter_dict_responses = [] 
    for tweet in ts.search_tweets_iterable(tso):
        list_twitter_dict_responses.append(
                {'user': tweet['user'],
                 'datetime': tweet['created_at'],
                 'text': tweet['text']}
        )

        # check if we reached the maximum amount of tweets we want
        
        if (len(list_twitter_dict_responses)==NUMBER_OF_TWEETS):
            break

except TwitterSearchException as error:
    print('ERRO:', error)
    
###########
# save the data

with open(path_save_data, 'wb') as filehandle:
    pickle.dump(list_twitter_dict_responses, filehandle)