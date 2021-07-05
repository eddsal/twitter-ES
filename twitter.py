import tweepy
import re
import io
import csv

# Credentials
consumer_key = "xxxxxxxxx"
consumer_secret =  "xxxxxxxxx"
access_token =  "xxxxxxxxx"
access_token_secret =  "xxxxxxxxx"

# create OAuthHandler object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access token and secret
auth.set_access_token(access_token, access_token_secret)
# create tweepy API object to fetch tweets
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('file-name', 'a')
csvWriter = csv.writer(csvFile)

print('Enter your keyword:')
search_words = input()      # enter your words
new_search = search_words + " -filter:retweets"

count = 0

for tweet in tweepy.Cursor(api.search,q=new_search,count=20,lang="en", since_id=0).items():
    count = count + 1
    print('tweet number', count)
    if count <= 20:
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
    else:
        break;