# Twitter API

For this part, we try to python module: tweepy and twittersearch. And we choose twittersearch eventually, because the tweets it crawls are more suitable for our needs, which is in **twittersearch.py**. And also, we exclude images, videos, retweets, only getting pure text tweets in database.  

## illustration
This line of code is to set keywords to a Tv show you want to search, for example #GOT is for Game of Thrones:
'''
tso.set_keywords(['#GOT'])
'''
 
Saving the results into a .txt file:
'''
doc=open('tweet.txt','w+')
'''

## Testing
The tweets we crawl for Modern Family are in **tweet_for_modernfamily.txt**

And feed them to the Google Natural Language API:
<img src="https://github.com/TingyiZhang/mini-project1-twitter-feeds-library/blob/feature/sentiment_analyser/sentimen_result_for_modernfamily.png">
