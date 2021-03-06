import tweepy
import datetime
import config, mod_read.read as read

def meal_tweet(meal):
    client = tweepy.Client(consumer_key=config.API_KEY,
                        consumer_secret=config.API_KEY_SECRET,
                        access_token=config.ACCESS_TOKEN,
                        access_token_secret=config.ACCESS_TOKEN_SECRET)

    date = datetime.datetime.today().date().strftime('%d/%m/%Y')
    if meal == 1:
        mealstr = 'o almoço'
    else:
        mealstr = 'a janta'

    food = read.read_meal(meal)
    tweet = """Data: {0}
No rancho d{1} de hoje temos: {2} e {3}.
Bom rancho a todos.""".format(date, mealstr, food[0], food[1])

    response = client.create_tweet(text=tweet)
    print(response)
    
def time_checker():
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
    tweets = client.get_users_tweets(id=config.USER_ID, tweet_fields=['text', 'created_at'], max_results=5)
    print(datetime.datetime.now().hour)
    for tweet in tweets.data:
        if tweet.text[0:4] == "Data":
            print(tweet.created_at.replace(tzinfo=None))
            if (datetime.datetime.now()-tweet.created_at.replace(tzinfo=None)).total_seconds()/3600+3 >= int(config.IDLE_TIME) and 18 > datetime.datetime.now().hour >= 16:
                meal_tweet(2)
            elif (datetime.datetime.now()-tweet.created_at.replace(tzinfo=None)).total_seconds()/3600+3 >= int(config.IDLE_TIME) and 13 > datetime.datetime.now().hour >= 9:
                meal_tweet(1)
            break