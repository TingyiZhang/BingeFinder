from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import json

# Instantiates a client
client = language.LanguageServiceClient()

def pullTweets():
    with open('tweet.json', 'r') as tweet_file:
        # Instantiates a plain text document.
        showData = json.load(tweet_file)
        return showData

showData = pullTweets()
sentimentData = {}
# The text to analyze
for show in showData:
    tweetsArray = showData[show]
    allTweetsForShow = ''
    for tweet in tweetsArray:
        allTweetsForShow = allTweetsForShow + '\n' + tweet
    
    document = types.Document(
        content=allTweetsForShow,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    sentimentObj = {}
    sentimentObj['score'] = sentiment.score
    sentimentObj['magnitude'] = sentiment.magnitude
    sentimentObj['other'] = str(sentiment)
    sentimentData[show] = sentimentObj
    with open('sentiment.json', 'w') as outfile:
        json.dump(sentimentData, outfile, indent=2, sort_keys=True)
    print('Text: {}'.format(show))
    print('Sentiment: score: {}, magnitude: {}'.format(sentiment.score, sentiment.magnitude))
