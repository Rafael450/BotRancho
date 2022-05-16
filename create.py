from http import client
import tweepy
import datetime
import config, read

def meal_tweet(meal):
    client = tweepy.Client(consumer_key=config.API_KEY,
                        consumer_secret=config.API_KEY_SECRET,
                        access_token=config.ACCESS_TOKEN,
                        access_token_secret=config.ACCESS_TOKEN_SECRET
                        )

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
    
