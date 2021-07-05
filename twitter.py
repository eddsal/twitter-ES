import tweepy
import re
import io
import csv


# Credentials
consumer_key = "42jQVIDXekhqAJFwx4leynRNg"
consumer_secret = "VvgjiJqHKKH2RVzQrPLIKbUn3oZWhcluGNl6F2fVI7BF6LIn5c"
access_token = "864386625752752128-0RWDGHQX1N59XIPNSwqn6fnwelegpAT"
access_token_secret = "KCh4ulCnCOqbXAjQcZUypNgWPMlUvzOtOFuJQlq9v1meb"


# create OAuthHandler object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access token and secret
auth.set_access_token(access_token, access_token_secret)
# create tweepy API object to fetch tweets
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('file-name', 'a')
csvWriter = csv.writer(csvFile)

search_words = "edd"      # enter your words
new_search = search_words + " -filter:retweets"

for tweet in tweepy.Cursor(api.search,q=new_search,count=100,
                           lang="en",
                           since_id=0).items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])