from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import ffmpeg_api as ff
import twitter_api as twi

import glob
import os
import os.path
import queue
import requests
import threading
import time

app = Flask(__name__)
api = Api(app)

def noKeys():
    print("this is my stub function")
    return 7

def videoProcessor(handlesQ, f):
    while(True):
        twitter_handle = handlesQ.get() #get a twitter handle from the queue
        if twitter_handle is not None: #if there is a twitter handle in the queue
            frameCount = len(glob.glob1(r"videoFiles/", twitter_handle + r"*.png")) #how many frames in the folder
            if frameCount < 20: #if there are less than 20 frames, add the handle back to the queue
                handlesQ.put(twitter_handle)
            else: #if there are enough image frames
                f.createVideo(twitter_handle) #create a video
        handlesQ.task_done() #indicate that the video for this twitter handle has been created
        time.sleep(0.5) #sleep for half a second

def tweetsToPics(tweetsQ, f):
    while(True):
        tweet = tweetsQ.get() #get the next tweet to convert to an image
        if tweet is not None:
            #if there is a tweet, convert it to an image frame
            f.createImage(tweet[0], tweet[1], tweet[2], tweet[3]) #0 = handle, 1 = profile pic, 2 = tweet, 3 = count
        tweetsQ.task_done() #unblock join call from addTweets() once all tweets have been turned to image frames
        time.sleep(0.5) #sleep for half a second

def addTweets(tweetsQ, twitter_handle, profilePic, profileTweets):
    for count, tweet in enumerate(profileTweets):
        tweetsQ.put([twitter_handle, profilePic, tweet, count]) #add each tweet to the queue
    tweetsQ.join() #block until all tweets have been turned into images

class Video(Resource):

    def get(self, twitter_handle):
        print("Let's begin")
        
        try:
            t = twi.twitter_api("keys") #get twitter keys from keys file
        except:
            print("No keys available!")
            #s = stubs.stubFuncs() #create an object for stubs, these will be run if there are no keys available
            resp = noKeys()
            return resp

        f = ff.ffmpeg_api() #create an ffmpeg object

        handlesQ = queue.Queue() #create queue to hold twitter handles in the order the handle called the api
        tweetsQ = queue.Queue() #create queue to hold tweets in the order they were tweeted by each handle

        handlesQ.put(twitter_handle) #add twitter handle to queue
        profilePic = t.get_profilePic(twitter_handle) #get the users profile picture
        profileTweets = t.get_tweets(twitter_handle) #get the users tweets

        #thread to add tweets to tweets queue in chronological order
        t = threading.Thread(name="producer", target=addTweets, args=(tweetsQ, twitter_handle, profilePic, profileTweets))
        t.start()

        #thread to convert tweets to image frames
        t = threading.Thread(name="imageConverter", target=tweetsToPics, args=(tweetsQ, f))
        t.start()

        #thread to convert the images to a video
        t = threading.Thread(name="videoCreator", target=videoProcessor, args=(handlesQ, f))
        t.start()
        
        resp = {"file location": os.getcwd() + '/' + twitter_handle + '_' + r'twitter_feed.mp4'} #create json response for api call
        return resp

#Resources
api.add_resource(Video, '/<twitter_handle>')

if __name__ == '__main__':
    app.run()
