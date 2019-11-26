# -*- coding: utf-8 -*-

"""
created by Fernando Battisti
ferbattisti.eng@gmail.com
"""

# libraries importing
from TwitterSearch import *
import json

# number of tweets to get
NUMBER_OF_TWEETS = 1000

# get the credentials
with open('/home/sirius/Documents/desafio-portal/twitter_credentials.json', 'r') as json_file:
    data = json.load(json_file)
    
    CONSUMER_KEY = data['CONSUMER_KEY']
    CONSUMER_SECRET = data['CONSUMER_SECRET']
    ACCESS_TOKEN = data['ACCESS_TOKEN']
    ACCESS_SECRET = data['ACCESS_SECRET']

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['telemedicina']) # let's define all words we would like to have a look for

#    tso.set_include_entities(False) # and don't give us all those entity information

    # create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = CONSUMER_KEY,
        consumer_secret = CONSUMER_SECRET,
        access_token = ACCESS_TOKEN,
        access_token_secret = ACCESS_SECRET
     )

    list_dict_responses = [] # save the 
    for tweet in ts.search_tweets_iterable(tso):
        list_dict_responses.append(
                {'user': tweet['user']['screen_name'],
                 'date_hour': tweet['created_at'],
                 'text': tweet['text']}
        )

        # the maximum amount of tweets we want is NUMBER_OF_TWEETS
        if (len(list_dict_responses)==NUMBER_OF_TWEETS):
            break

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)