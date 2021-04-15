import snscrape.modules.twitter as sntwitter
import pandas as pd

user_handles = pd.read_csv('Twitter_user_handles_to_predict.csv')
print(user_handles.head)

tweets_list = []

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:JayHolz410').get_items()):
    if i > 100:
        break
    tweets_list.append([tweet.content])

for tweet in tweets_list:
    print(tweet)
