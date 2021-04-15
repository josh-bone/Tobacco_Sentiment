import snscrape.modules.twitter as sntwitter
import pandas as pd

user_handles = pd.read_csv('Twitter_user_handles_to_predict.csv')
last_finished_ID = 5  # IMPORTANT: Refresh this every time the script is restarted

# loop through twitter handles
for user in user_handles['Username'][last_finished_ID:]:

    print(f"\nReading tweets of {user}...\n")

    tweets_list = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:'+user).get_items()):
        # TODO: decide on what tobacco-related keywords we want to monitor
        tweets_list.append([tweet.username, tweet.content, tweet.date])

        # Monitor progress
        if i % 1000 == 0:
            #print(f"{i/1000}k'th tweet from {user}")
            #print(tweet.content)
            pass
        
        # save progress to file (every 10k tweets)
        if i % 10000 == 0:
            print("\n----Saving----\n")
            cur_df = pd.DataFrame(tweets_list, columns=['Username','Text','Date'])
            prev_df = pd.read_csv("Scraped_tweets.csv")
            final_df = pd.concat([prev_df, cur_df]).drop_duplicates().reset_index(drop=True)
            final_df.to_csv("Scraped_tweets.csv")
            tweets_list = []

    print(f"\nFinished with {user}\n")
    #last_finished_ID = user_handles['ID'][i]

    # Save final (last 10k or less) tweets from the user 
    cur_df = pd.DataFrame(tweets_list, columns=['Username','Text','Date'])
    prev_df = pd.read_csv("Scraped_tweets.csv")
    final_df = pd.concat([prev_df, cur_df]).drop_duplicates().reset_index(drop=True)
    final_df.to_csv("Scraped_tweets.csv")