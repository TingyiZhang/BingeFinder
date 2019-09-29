#exclude retweet, pictures and video
#and it shows how many tweets in total
from TwitterSearch import *
from twittersearchKey import keys
import json


# reload(sys)
# sys.setdefaultencoding('utf-8')

ts = TwitterSearch(
    consumer_key = keys['consumer_key'],
    consumer_secret = keys['consumer_secret'],
    access_token = keys['access_token'],
    access_token_secret = keys['access_token_secret']
)
tso = TwitterSearchOrder() # create a TwitterSearchOrder object
tso.set_language('en')
tso.set_include_entities(True)
tso.set_count(20) 

def getTweetsForKeyword(searchKeyword):
    i=0
    tweets = []
    # doc=open('tweet.txt','w+')

    try:
        tso.set_keywords([searchKeyword]) # let's define all words we would like to have a look for
        

    # remove tweets with URL and ReTweets
        for tweet in ts.search_tweets_iterable(tso):
            if (not tweet['retweeted']) and ('RT @' not in tweet['text']) and ('https://' not in tweet['text']):
                # doc.write(str(i))
                # doc.write('.%s\n\n' %(tweet['text']))
                tweets.append(tweet['text'])
                i+=1
        print(searchKeyword + " there are %d tweets in total"%i)
        return(tweets)
    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)



keywords = ['#BigBangTheory', '#GameOfThrones', '#Castle', '#StrangerThings']
showData = {};
for showName in keywords:
    tweets = getTweetsForKeyword(showName)
    showData[showName] = tweets
    
with open('tweet.json', 'w') as outfile:
    json.dump(showData, outfile)