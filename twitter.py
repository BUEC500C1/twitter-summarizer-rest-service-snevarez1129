import configparser
import tweepy

class twitter():

    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path) #get path to keys file
        auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(), config.get('auth', 'consumer_secret').strip())
        auth.set_access_token(config.get('auth', 'access_token').strip(), config.get('auth', 'access_token_secret').strip())
        self.api = tweepy.API(auth) #authenticate

    def get_profilePic(self, myHandle):
        try:
            profile = self.api.get_user(myHandle) #get user profile
            return profile.profile_image_url_https #return profile picture
        except tweepy.error.TweepError as e:
            print(e)
            return ""

    def get_tweets(self, myHandle, numTweets):
        try:
            tweets = self.api.user_timeline(screen_name=myHandle, count=numTweets) #get the tweets
            return tweets
        except tweepy.error.TweepError as e:
            print(e)
            return ""
