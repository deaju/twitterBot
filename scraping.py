

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from urllib import parse
import psycopg2
import os
import requests
import re

baseURL = 'https://anime.dmkt-sp.jp/animestore/'
topURL = 'tp_pc'
loginURL = 'login?next_url=https%3A%2F%2Fanime.dmkt-sp.jp%2Fanimestore%2Ftp_pc'
historyURL = 'mpa_hst_pc?workType=0&editModeFlag=0&selectPage='
animeId = os.environ["ID"]
animePass = os.environ["PASS"]

#driver = webdriver.Chrome()

#header=driver.find_element_by_id('topHeader')
#header.find_element_by_class_name('login').click()
#driver.switch_to.window(driver.window_handles[1])
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

def storeProgress(conn,animeInfo):
    title = animeInfo['title']
    progress = animeInfo['progress']
    num = animeInfo['number']
    date=datetime.now().strftime("%Y-%m-%d")
    user='deaju'
    cur=conn.cursor()
    cur.execute('INSERT INTO showprogress_history (title, progress, date, "user", num) VALUES (%s,%s,%s,%s,%s)',[title,progress,date,user,num])
    conn.commit()
    cur.close()
    return

def login(driver,url):
    driver.get(url)
    driver.find_element_by_name('authid').send_keys(animeId)
    driver.find_element_by_name('authpass').send_keys(animePass)
    driver.find_element_by_name('subForm').click()

def getHistory(driver,url):
    driver.get(url)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html,'lxml')
    content = soup.find(class_='contentsWrapper').find_all(class_='itemModule')
    return content

def getAnimeInfo(element):
    title=element.find(class_='line2').text
    elementNum=element.find(class_='textContainerIn').find(class_='number').text
    number=re.search('([0-9]+)',elementNum)
    if number:
        number = number.group(0)
    else:
        number = 0
        ##number = elementNum.replace('\n','')
    elementProgress=element.find(class_='progressCompleted').attrs['style']
    progress=re.search('([0-9]+)',elementProgress).group(0)
    return {'title':title,'number':number,'progress':progress}

def getIndexHistoryPage(driver,url):
    driver.get(url)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html,'lxml')
    page = soup.find(class_='onlyPcLayout')
    return re.findall('([0-9]+)',page.getText())

def storePage(element,conn):
    for anime in element:
        animeInfo = getAnimeInfo(anime)
        storeProgress(conn,animeInfo)

def main():
    driver = webdriver.PhantomJS()
    driver.set_window_size(1500, 850)
    login(driver,baseURL+loginURL)
    conn=connectPostgres()
    pageList=getIndexHistoryPage(driver,baseURL+historyURL)
    for index in pageList:
        element=getHistory(driver,baseURL+historyURL+index)
        storePage(element,conn)
    driver.close()
