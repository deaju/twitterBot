import hashlib
from urllib import parse
import psycopg2
import os

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

def selectProgress(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM showprogress_history')
    progress = cur.fetchall()
    cur.close()
    return progress

def storeProgress(conn,url,title):
    cur=conn.cursor()
    cur.execute('INSERT INTO showprogress_history (url) VALUES (%s) where title = (%s)',[url,title])
    conn.commit()
    cur.close()
    return

def setURL(conn):
    progress = selectProgress(conn)
    for row in progress:
        title = row['title']
        url = hashlib.md5(title).hexdigest()
        storeProgress(conn,url,title)

def main():
    conn = connectPostgres()
    setURL(conn)

