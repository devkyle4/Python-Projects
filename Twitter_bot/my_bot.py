import tweepy as tweepy
import time

print('Hello World')

CONSUMER_KEY = 'fR82Boe7XAzNAQuahkrSC5NHW'
CONSUMER_SECRET = 'HtxL7GI6IoKMC6UFJDCOwfz5R1tY2ITx1pFQ8sxkqX4CiPbEcO'
ACCESS_TOKEN = '1543310432278118401-HcyC56YUPg9V0R1adIUCGBs6eVGZfI'
ACCESS_TOKEN_SECRET = 'COyYcp4ZVl9AmBVsIXROEy9sMcH6u9rFeL8ZV6UJOktyH'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
mentions = api.mentions_timeline()
LAST_SEEN_ID_FILE = 'last_seen_id.txt'
TARGET_PHRASE = "#Peaceuntotheworld"

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_peace():
    print('retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(LAST_SEEN_ID_FILE)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(last_seen_id,
        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, LAST_SEEN_ID_FILE)
        if TARGET_PHRASE in mention.full_text.lower():
            print('found #Peaceuntotheworld!')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name +
                              '#PeaceUntoTheWorld!!, Thank You!!', mention.id)
        else:
            print("nothing")


while True:
    reply_to_peace()
    time.sleep(2)


