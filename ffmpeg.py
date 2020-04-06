from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

import datetime
import os
import requests
import subprocess
import textwrap

class ffmpeg():

    def __init__(self):
        pass #do nothing, just create an instance of the class

    def createImage(self, myHandle, myPic, myTweet, count):

        txt = myTweet.text #get the text from the tweet

        myBackground = Image.new('RGBA', (1024, 512), (255, 75, 75, 200)) #create a background for the image
        handleFont = ImageFont.truetype(r'font/Comic Sans MS.ttf', 30) #create a font for the twitter handle
        tweetFont = ImageFont.truetype(r'font/Comic Sans MS.ttf', 16) #create a font for the tweet text

        info = requests.get(myPic) #get the profile picture info
        twitterPic = Image.open(BytesIO(info.content)) #generate the image
        myBackground.paste(twitterPic, (75, 150)) #add the profile picture to the background

        myDrawing = ImageDraw.Draw(myBackground) #make background writable
        lines = textwrap.wrap(txt, width=100) #define size of a line
        x = 75 #x coord for start of text
        y = 250 #y coord for start of text

        myDrawing.text((150, 150), '@'+myHandle, font=handleFont, fill="white") #write the twitter handle
        for line in lines:
            myDrawing.text(((x), y), line, font=tweetFont, fill="white") #write the tweet
            y += 30 #move to next line
        myDrawing.text((75, y+30), 'tweet '+str(count+1), font=tweetFont, fill="white") #write the count

        myBackground.save('./videoFiles/' + str(myHandle) + str(count) + '.png') #save the final image in the folder
        
    def createVideo(self, myHandle):            
        cmd = ['ffmpeg', '-y', '-r', '1/3', '-i', './videoFiles/'+myHandle+'%d.png', '-pix_fmt', 'yuv420p', '-r',
        '25', '-loglevel', 'error', '-hide_banner', myHandle + '_twitter_feed.mp4']
        
        try:
            #launch a subprocess to create the video using the images created
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        except Exception as e:
            print("ERROR: ", e)        
        return
