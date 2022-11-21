import snscrape.modules.twitter as sntwitter
from datetime import date
import datetime
import threading

TWEETS = []
WAIT_TIME = 5

def check_for_tweets(username):
    print("Searching for tweet" + str(datetime.datetime.now()))

    # Not hardcoding the start date.
    today = date.today()
    query = "(from:"+username+") since:"+str(today)
    limit = 1

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        #Check if its new tweet.
        if len(TWEETS) == limit:
            if TWEETS[0] != tweet.content:
                TWEETS[0] = tweet.content
                print(str(TWEETS) + str(datetime.datetime.now()))
                
                ##USE CODE TO TURN ON FLAMETHROWER
                
                break
            break
        else:
            TWEETS.append(tweet.content)
            print(str(TWEETS) + str(datetime.datetime.now()))
            break
        break
    
#Loop the function for WAIT_TIME seconds
ticker = threading.Event()
while not ticker.wait(WAIT_TIME):
    check_for_tweets("elonmusk")
