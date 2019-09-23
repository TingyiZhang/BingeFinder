import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


search_results = api.search(q='keyword',count=100000)


for tweet in search_results:
    print tweet.text
