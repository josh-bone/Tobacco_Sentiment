import os
import pandas as pd 

prev_df = pd.read_csv("Scraped_tweets_1.csv")

for fname in os.listdir('./'):
    if(fname[:7] == 'Scraped'):
        cur_df = pd.read_csv(fname)
        prev_df = pd.concat([prev_df, cur_df])

prev_df.drop_duplicates().reset_index(drop=True)
prev_df.to_csv("tweets_segment1.csv")