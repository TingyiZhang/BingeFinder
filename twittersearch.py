#exclude retweet, pictures and video
#and it shows how many tweets in total
from TwitterSearch import *
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

i=0
doc=open('tweet.txt','w+')

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['#GOT']) # let's define all words we would like to have a look for
    tso.set_language('en')
    tso.set_include_entities(True) 

    ts = TwitterSearch(
        consumer_key = '',
        consumer_secret = '',
        access_token = '',
        access_token_secret = ''
     )

    for tweet in ts.search_tweets_iterable(tso):
        if (not tweet['retweeted']) and ('RT @' not in tweet['text']) and ('https://' not in tweet['text']):
            doc.write(str(i))
            doc.write('.%s\n\n' %(tweet['text']))
            i+=1
    print("there are %d tweets in total"%i)
except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
