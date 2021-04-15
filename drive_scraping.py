import snscrape.modules.twitter as sntwitter
import pandas as pd

user_handles = pd.read_csv('Twitter_user_handles_to_predict.csv')

# loop through twitter handles
for user in user_handles['Username']:
    print()
    print(f"Reading tweets of {user}")

    tweets_list = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:'+user).get_items()):

        # Monitor progress
        if i % 500 == 0:
            print(tweet.content)

        # TODO: only save the tweets if they contain relevant keywords
        # TODO: decide on what tobacco-related keywords we want to monitor
        tweets_list.append([tweet.username, tweet.content, tweet.date])

    cur_df = pd.DataFrame(tweets_list, columns=['Username','Text','Date'])
    prev_df = pd.read_csv("Scraped_tweets.csv")
    final_df = pd.concat([prev_df, cur_df]).drop_duplicates().reset_index(drop=True)

    final_df.to_csv("Scraped_tweets.csv")