# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "kfncRpqcNqSG2DULHCKMgBnll"
consumer_secret = "xwLtFescw0BjyeNAHstnp26k8oLmOFfI0bFuz9IAETgAyFUdde"
access_token = "975022447367000065-7PokYOGkInhfJwZsRNeQ8YiYcgn7gRm"
access_token_secret = "Gpey5mmAhdNQVQQQFqjyd0WnvB32errDZ4D5cJrVba1QH"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        "Can't stop. Won't stop. Chatting! This is Tweet #%s from Heroku!" %
        tweet_number)


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1
