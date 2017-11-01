# -*- coding: utf-8 -*-

import os
import re

from datetime import datetime, timedelta
from urllib import parse
import twitter
import psycopg2


oath_key_dict = {
    "consumer_key": "tvYsqXcTYbxFtt9RAE3hElL7H",
    "consumer_secret": "2WNXt2Xw9uwAeS2WOKSwHniICTE8MZUgkODFYNhUkesPTH6S3F",
    "access_token": "920973082130444288-cuNmbIaeHwaVCGS7jyD2J6OkugxasRA",
    "access_token_secret": "ztebRO91VhlYGNyihQpJBllf9sZhm4WYVgcEBsQ5stuMJ"
}

def connectPostgres():
    parse.uses_netloc.append("postgres")
    url = parse.urlparse(os.environ["DATABASE_URL"])

    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    return conn

def storeProgress(conn,progress):
    date=datetime.now().strftime("%Y-%m-%d")
    storeProgress=selectProgress(conn,date)
    if len(storeProgress) == 0:
        cur=conn.cursor()
        cur.execute('INSERT INTO nagoyan_sakura VALUES (%s,%s)',[date,progress])
        conn.commit()
        cur.close()
    else:
        cur=conn.cursor()
        cur.execute("UPDATE nagoyan_sakura SET progress=(%s) WHERE date=(%s)",[progress,date])
        conn.commit()
        cur.close()
    return
        
    
def selectProgress(conn,date):
    cur = conn.cursor()
    cur.execute('SELECT * FROM nagoyan_sakura where date=(%s)',[date])
    progress = cur.fetchall()
    cur.close()
    return progress

def deltaProgress(conn):
    today = datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    todayProgress = selectProgress(conn,today)[0][1]
    yesterdayProgress = selectProgress(conn,yesterday)[0][1]
    return todayProgress - yesterdayProgress

def getAuth():
    auth = twitter.OAuth(consumer_key=oath_key_dict["consumer_key"],
                  consumer_secret=oath_key_dict["consumer_secret"],
                  token=oath_key_dict["access_token"],
                  token_secret=oath_key_dict["access_token_secret"]
                  )
    t = twitter.Twitter(auth=auth)
    return t

def getAuthUpload():
    auth = twitter.OAuth(consumer_key=oath_key_dict["consumer_key"],
                  consumer_secret=oath_key_dict["consumer_secret"],
                  token=oath_key_dict["access_token"],
                  token_secret=oath_key_dict["access_token_secret"]
                  )
    t = twitter.Twitter(auth=auth,domain='upload.twitter.com')
    return t
    

def getUserProgress(twitter,screen_name):
    user = twitter.users.lookup(screen_name=screen_name)
    user_name = user[0]['name']
    return re.search('([0-9]+).*/[0-9]*',user_name).group(1)


def postTweet(twitter,delta):
    t_upload = getAuthUpload()
    if delta > 0:
        message="@nagoyan240 今日の進捗は{}話です".format(delta)
        id_img = t_upload.media.upload(media=imagedata)["smile.jpg"]
    elif delta <= 0:
        message="@nagoyan240 進捗ありません"
        id_img = t_upload.media.upload(media=imagedata)["anger.jpg"]
    twitter.statuses.update(status=message, media_ids=id_img)

def postTweetDummy(twitter,delta):
    t_upload = getAuthUpload()
    if delta > 0:
        with open("smile.jpg", "rb") as imagefile:
            imagedata = imagefile.read()
        message="今日の進捗は{}話です".format(delta)
        id_img = t_upload.media.upload(media=imagedata)["smile.jpg"]
    elif delta <= 0:
        with open("anger.jpg", "rb") as imagefile:
            imagedata = imagefile.read()
        message="進捗ありません"
        id_img = t_upload.media.upload(media=imagedata)["anger.jpg"]
    twitter.statuses.update(status=message, media_ids=id_img)


def main():
    twitter = getAuth()
    screen_name = 'nagoyan240'
    progress = getUserProgress(twitter,screen_name)
    conn = connectPostgres()
    storeProgress(conn,progress)

    delta = deltaProgress(conn)
    postTweetDummy(twitter,delta)

main()


