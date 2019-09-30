import json

def pullSentimentScores():
    with open('sentiment.json', 'r') as tweet_file:
        showData = json.load(tweet_file)
        return showData

if __name__ == '__main__':
    showData = pullSentimentScores()
    showScores = []
    for show in showData:
        showScore = {}
        showScore['name'] = show
        showScore['score'] = showData[show]['score']
        showScore['magnitude'] = showData[show]['magnitude']
        showScores.append(showScore)
    # print(showScores)
    sortedList = sorted(showScores, key=lambda i: (i['score'], i['magnitude']) )
    topShows = sortedList[-5:]
    topShows.reverse()
    controversialShows = sortedList[0:5]
    print("\nTop Loved Shows:")
    i=0
    while i<5:
        print(str(i+1) + ". " + topShows[i]['name'])
        i+=1

    print("\nTop Controversial Shows:")
    i=0
    while i<5:
        print(str(i+1) + ". " + controversialShows[i]['name'])
        i+=1

        
        