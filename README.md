# Binge Finder

Recommend TV Shows and Movies based on sentiment analyze results of tweets.

## Product Mission
The Binge Finder is an easy to use recommender.
- For TV shows Lovers who want recommendation based on popularity and real public reviews on Twitter.
- Unlike endless and sometimes unobjective recommendations on Netflix，Binge Finder recommends you Top 5 loved and Top 5 controversial TV shows based on Twitter comments analyze.

### Target Users

Everyone who wants to watch TV shows.

## User Stories

1. As an audience, I want recommendation of top 5 TV shows that are most loved on Twitter.

2. As an audience, I want recommendation of top 5 TV shows that are the most controversial on Twitter.  

## Architecture

<img src="https://github.com/TingyiZhang/mini-project1-twitter-feeds-library/blob/master/Binge_FInder.jpg">

## Results

Output for Recommendations: 
<img src="https://github.com/TingyiZhang/mini-project1-twitter-feeds-library/blob/master/command-line-output.JPG">

Output for Sentiment Analyze:
<img src="https://github.com/TingyiZhang/mini-project1-twitter-feeds-library/blob/feature/sentiment_analyser/senntiment-screen.JPG">


This is saved in the `sentiment.json` file


## Installation Instructions

1. Install Python 3.6+, corresponding pip(usually included)
2. clone this repository using:
>`git clone https://github.com/TingyiZhang/mini-project1-twitter-feeds-library.git`
3. Create a virtual environment using venv(usually included with Python) as:
>`python3 -m venv env`
4. Activate your virtual environment
>`source env/bin/activate`
5. Install required packages with command:
>`pip install -r requirements.txt`
6. Run:
>`python getRecommendation.py`


## Advanced Users

To use the Twitter and Google API's, please follow the following instructions  

### To Pull tweets from Twitter

1. Create a file "twittersearchKey.py"
2. Add the following contents:
```
    keys = {
    'consumer_key' : '',
    'consumer_secret' : '',
    'access_token' : '',
    'access_token_secret' : ''
    }
```


### To Do Sentiment Analysis

1. Analyses tweets from the file - tweet.json
2. Export your google Natural Language Developer key by running in terminal:
>`export GOOGLE_APPLICATION_CREDENTIALS="path to your_key.json"`
2. Outputs sentiment analyzer score to - sentiment.json


## LICENSE
MIT

## References
1. Twitter Search Library:  `https://github.com/ckoepp/TwitterSearch`
2. Google Search Library: `https://cloud.google.com/natural-language/`
3. TV Show Database: `IMDB`
4. TV Shows Twitter Tags: `https://ew.com/article/2012/10/01/twitter-hashtag-handle-tv-shows/`
>export GOOGLE_APPLICATION_CREDENTIALS="path to your_key.json"
2. Outputs sentiment analyzer score to - sentiment.json

## Some thoughts
### What we found interesting?
- It's amazing that we can get all those data through Twitter API and analyze it through Google.
- These two APIs are pretty easy to use and easy to customize.
- **Twitter API does not play very nice** - Stringent API hit limit, Google API is relatively easy to use


### Things we can improve
- **Improve the scoring mechanism** - Improve how we calculate our scores, currently very basic arithmetic.
- **Filter tweets** - Improve the sentiment analysis by removing irrelevant tweets from our input to the sentiment analyzer.
- **Extend it to movies** - In the future we can try to rank the movies too.
- **Add Feature to search by genre** - Search top content by comedy, horror, thriller, etc. 

### Things we will avoid
- **Studying the API more carefully before getting started** - We ran into many API limits for Twitter
- **IMDB API does not play nice** - We tried to get TV shows list through IMDb API at first, but the IMDb API does not support searching by popularity. 

