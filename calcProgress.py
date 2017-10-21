# -*- coding: utf-8 -*-

import os
import re

import twitter

oath_key_dict = {
    "consumer_key": "tvYsqXcTYbxFtt9RAE3hElL7H",
    "consumer_secret": "2WNXt2Xw9uwAeS2WOKSwHniICTE8MZUgkODFYNhUkesPTH6S3F",
    "access_token": "920973082130444288-cuNmbIaeHwaVCGS7jyD2J6OkugxasRA",
    "access_token_secret": "ztebRO91VhlYGNyihQpJBllf9sZhm4WYVgcEBsQ5stuMJ"
}



def getAuth():
    auth = twitter.OAuth(consumer_key=oath_key_dict["consumer_key"],
                  consumer_secret=oath_key_dict["consumer_secret"],
                  token=oath_key_dict["access_token"],
                  token_secret=oath_key_dict["access_token_secret"]
                  )
    t = twitter.Twitter(auth=auth)
    return t

def getUserProgress(twitter,screen_name):
    user = twitter.users.lookup(screen_name=screen_name)
    user_name = user[0]['name']
    return re.search('([0-9]+).*/[0-9]*',user_name).group(1)



