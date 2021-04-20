import snscrape.modules.twitter as sntwitter
import pandas as pd

user_handles = pd.read_csv('Twitter_user_handles_to_predict.csv')
maxTweets = 100
start_ID = 1  # IMPORTANT: Refresh this every time the script is restarted
end_ID = 6250  # Also adjust this based on your assigned segment
num_csv = 0

# loop through twitter handles
for j,user in enumerate(user_handles['Username'][start_ID:end_ID]):

    print(f"\nReading tweets of {user}... (#{user_handles['ID'][start_ID + j]})\n")

    tweets_list = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:'+user+' since:2020-01-01').get_items()):
        if i >= maxTweets:
            break
        tweets_list.append([tweet.username, tweet.content, tweet.date])

    # Save final (last 10k or less) tweets from the user 
    print("----Saving----\n")
    cur_df = pd.DataFrame(tweets_list, columns=['Username','Text','Date'])
    try:
        prev_df = pd.read_csv("Scraped_tweets_" + str(num_csv) + ".csv")
        final_df = pd.concat([prev_df, cur_df]).drop_duplicates().reset_index(drop=True)
    except:
        final_df = cur_df
    final_df.to_csv("Scraped_tweets_" + str(num_csv) + ".csv")

    if j > 500:
        num_csv += 1