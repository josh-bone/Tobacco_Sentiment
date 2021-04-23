import snscrape.modules.twitter as sntwitter
import pandas as pd

user_handles = pd.read_csv('Twitter_user_handles_to_predict.csv')
maxTweets = 100
start_ID = 1  # IMPORTANT: Refresh this every time the script is restarted
end_ID = 6250  # Also adjust this based on your assigned segment
num_csv = 0
df = pd.DataFrame()

# loop through twitter handles
for j,user in enumerate(user_handles['Username'][start_ID:end_ID]):

    print(f"\nReading tweets of {user}... (#{user_handles['ID'][start_ID + j]})\n")

    tweets_list = []
    try:
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:'+user).get_items()): # make sure gets 100 if the user has that many
            if i >= maxTweets:
                break
            tweets_list.append([tweet.username, tweet.content, tweet.date])

        # Save final (last 10k or less) tweets from the user 
        cur_df = pd.DataFrame(tweets_list, columns=['Username','Text','Date'])
        df = df.append(cur_df)

        if (j+1)%500==0: #save every 500 queries
            print("----Saving----\n")
            df.to_csv("Scraped_tweets_" + str(num_csv) + ".csv", index=False)
            num_csv += 1
            df = pd.DataFrame()
    except:
        pass
