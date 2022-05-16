from http import client
from urllib import response
import tweepy
import config

# Authenticate to Twitter
client = tweepy.Client(consumer_key=config.API_KEY,
                       consumer_secret=config.API_KEY_SECRET,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET
                       )

response = client.create_tweet(text='teste')


