from TwitterSearch import *
import os
import sys

doc=open('tweet.txt','w+')

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['keyword']) # let's define all words we would like to have a look for
    tso.set_language('en')
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = '',
        consumer_secret = '',
        access_token = '',
        access_token_secret = ''
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )


except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
    output=sys.stdout
    sys.stdout=doc


