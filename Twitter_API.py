import tweepy

consumer_key = "x4H8SPPanmn3QdJEF0y2p2T3N"
consumer_secret = "3H3P2QGGWqUrZeab84v26R7l4oLqmI3BgJAaWLMDfxQv8c9PBZ"
access_token = "1171903935805677569-b7y0ymd3ePWJUAZ6KLYDUu4Lpm5Mjb"
access_token_secret = "FgwrAKuOZ3NRZMghDeqFsWFQ510f4N6m0Rcvb4nbRv8q4"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


search_results = api.search(q='keyword',count=100)


for tweet in search_results:
    print(tweet.text)
