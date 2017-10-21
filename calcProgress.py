# -*- coding: utf-8 -*-

import os
import re

from datetime import datetime
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
    progress=selectProgress(conn,date)
    if len(progress) == 0:
        cur=conn.cursor()
        cur.execute('INSERT INTO nagoyan_sakura VALUES (%s,%s)',[date,progress])
        cur.commit()
    else:
        cur=conn.cursor()
        cur.execute('UPDATE nagoyan_sakura SET progres=(%s) WHERE date=(%s)',[progress,date])
        cur.commit()
    return
        
    
def selectProgress(conn,date):
    cur = conn.cursor()
    cur.execute('SELECT * FROM nagoyan_sakura where date=(%s)',[date])
    progress = cur.fetchall()
    return progress

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




