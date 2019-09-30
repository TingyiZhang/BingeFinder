# Binge Finder

Recommend TV Shows and Movies based on sentiment analyze results of tweets.

## Product Mission
The Binge Finder is an easy to use recommender.

Unlike endless and sometimes unobjective recommendations on Netflix，Binge Finder recommends you Top 5 loved and Top 5 controversial TV shows based on Twitter comments analyze.

### Target Users

For TV shows Lovers who want recommendation based on popularity and real public reviews on Twitter.

## User Stories

1. As an audience, I want recommendation of top 5 TV shows that are most loved on Twitter.

2. As an audience, I want recommendation of top 5 TV shows that are the most controversial on Twitter.  

## Architecture

<img src="https://github.com/TingyiZhang/mini-project1-twitter-feeds-library/blob/master/Binge_FInder.jpg">

## Installation Instructions

1. Install Python 3.6+, corresponding pip(usually included)
2. clone this repository using:
> git clone https://github.com/TingyiZhang/mini-project1-twitter-feeds-library.git
3. Create a virtual environment using venv(usually included with Python) as:
>python3 -m venv env
4. Activate your virtual environment
 >source env/bin/activate
5. Install required packages with command:
>pip install -r requirements.txt
6. Run:
>python getRecommendation.py


## Advanced Users

To use the Twitter and Google API's, please follow the following instructions  

### To Pull tweets from Twitter

1. Create a file "twittersearchKey.py"

2. Add the following contents:

    keys = {
    'consumer_key' : '',
    'consumer_secret' : '',
    'access_token' : '',
    'access_token_secret' : ''
    }


### To Do Sentiment Analysis

1. Analyses tweets from the file - tweet.json
2. Export your google Natural Language Developer key by running in terminal:
>export GOOGLE_APPLICATION_CREDENTIALS="path to your_key.json"
2. Outputs sentiment analyzer score to - sentiment.json

## Some thoughs
### What we found interesting?
It's amazing that we can get all those data through Twitter API and analyze it through Google. These two APIs are very easy to use and very easy to customized.

### Things we can improve
We tryed to get TV shows list through iMDb API at first, but the iMDb API only support moives searching. In the future we can try to rank the movie too and rank them for each genre.

### Things we will avoid
Clarify our needs befor getting started

