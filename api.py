from flask import Flask, send_file
from flask_restful import reqparse, abort, Api, Resource
from PIL import Image

import twitter as tw
import stubFunctions as s
import ffmpeg as ff

import glob
import os
import os.path
import queue
import requests
import threading

app = Flask(__name__)
api = Api(app)

def noKeys():
    allTweets = s.getTweets() #get saved tweets from json file
    twitter_handle = s.pickHandle() #pick one of the saved twitter handles
    resp = s.generateResponse(allTweets, twitter_handle) #generate api response
    return resp #return the response

def videoProcessor(handlesQ, f):
    while(True):
        handle = handlesQ.get() #get a twitter handle from the queue
        if handle is not None: #if there is a twitter handle in the queue
            imgCount = len(glob.glob1(r"videoFiles/", handle + r"*.png")) #number of images in the folder
            if imgCount < 20: #if there are less than 20 images, add the handle back to the queue
                handlesQ.put(handle)
            else: #if there are enough image frames
                f.createVideo(handle) #create a video
        handlesQ.task_done() #indicate that the video for this twitter handle has been created

def tweetsToPics(tweetsQ, f):
    while(True):
        tweet = tweetsQ.get() #get the next tweet
        if tweet is not None: #if there is a tweet
            f.createImage(tweet[0], tweet[1], tweet[2], tweet[3]) #convert it to an image
        tweetsQ.task_done() #unblock join call from addTweets() once all tweets have been turned to image frames

def getTweets(tweetsQ, myHandle, myPic, myTweets):
    for count, tweet in enumerate(myTweets):
        tweetsQ.put([myHandle, myPic, tweet, count]) #add tweet to the queue
    tweetsQ.join() #block until all tweets have been turned into images

class Video(Resource):
    def get(self, myHandle):

        try: #try to get twitter keys from keys file
            t = tw.twitter("keys")
        except: #no keys exist, run the stub functions
            resp = noKeys()
            return resp

        f = ff.ffmpeg() #create an ffmpeg object
        numTweets = 20 #number of tweets to get

        handlesQ = queue.Queue() #queue to hold twitter handles in the order the api received the handle
        tweetsQ = queue.Queue() #queue to hold tweets in the order they were tweeted by the handle
        #imagesQ = queue.Queue() #queue to hold tweet images

        handlesQ.put(myHandle) #add twitter handle to queue

        myPic = t.get_profilePic(myHandle) #get the handles profile picture
        myTweets = t.get_tweets(myHandle, numTweets) #get the handles tweets

        #thread to get the tweets
        t1 = threading.Thread(name="producer", target=getTweets, args=(tweetsQ, myHandle, myPic, myTweets))
        t1.setDaemon(True)
        t1.start()

        #thread to convert tweets to images
        t2 = threading.Thread(name="imageConverter", target=tweetsToPics, args=(tweetsQ, f))
        t2.setDaemon(True)
        t2.start()

        #thread to convert the images to video
        t3 = threading.Thread(name="videoCreator", target=videoProcessor, args=(handlesQ, f))
        t3.setDaemon(True)
        t3.start()

        handlesQ.join() #block until the video is created

        myFile = os.getcwd() + '/' + myHandle + '_' + r'twitter_feed.mp4'
        return send_file(myFile)

#Resources
api.add_resource(Video, '/<myHandle>')

if __name__ == '__main__':
    app.run(debug=True)
