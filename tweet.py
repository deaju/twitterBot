# -*- coding: utf-8 -*-

import os
from datetime import datetime

import twitter

oath_key_dict = {
    "consumer_key": "tvYsqXcTYbxFtt9RAE3hElL7H",
    "consumer_secret": "2WNXt2Xw9uwAeS2WOKSwHniICTE8MZUgkODFYNhUkesPTH6S3F",
    "access_token": "920973082130444288-cuNmbIaeHwaVCGS7jyD2J6OkugxasRA",
    "access_token_secret": "	ztebRO91VhlYGNyihQpJBllf9sZhm4WYVgcEBsQ5stuMJ"
}

api = twitter.Api(consumer_key=os.environ["consumer_key"],
                  consumer_secret=os.environ["consumer_secret"],
                  access_token_key=os.environ["access_token"],
                  access_token_secret=os.environ["access_token_secret"]
                  )
api.PostUpdate("system time is %s" % datetime.now())
