import json
import random

def getTweets():
    #open json file
    with open("offlineTweets.json", "r") as f:
        data = f.read()
        json_obj = json.loads(data) #read from json file
    return json_obj #return object

def pickHandle():
    availableHandles = ["BarackObama", "Cristiano", "TheEllenShow", "realDonaldTrump", "busnowtm"] #list of hard coded twitter handles
    idx = random.randrange(0, 4, 1) #pick one of the handles
    return availableHandles[idx] #return the chosen handle

def generateResponse(json_obj, twitter_handle):
    header = {
        "ERROR": 401, 
        "ERRORtext": 
        "There were no keys available so your request could not be completed.", 
        "savedText": "However, so you don't go home empty handed, here is a sample tweet that was previously saved."
    }
    data = json_obj[twitter_handle]
    resp = [header, data]
    return resp
    