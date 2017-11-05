

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import re

baseURL = 'https://anime.dmkt-sp.jp/animestore/'
topURL = 'tp_pc'
loginURL = 'login?next_url=https%3A%2F%2Fanime.dmkt-sp.jp%2Fanimestore%2Ftp_pc'
historyURL = 'mpa_hst_pc?workType=0&editModeFlag=0&selectPage=1'
id=os.environ["ID"]
pass=os.environ["PASS"]

#driver = webdriver.Chrome()

#header=driver.find_element_by_id('topHeader')
#header.find_element_by_class_name('login').click()
#driver.switch_to.window(driver.window_handles[1])

def login(driver,url):
    driver.get(url)
    driver.find_element_by_name('authid').send_keys(id)
    driver.find_element_by_name('authpass').send_keys(pass)
    driver.find_element_by_name('subForm').click()

def getHistory(driver,url):
    driver.get(url)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html,'lxml')
    content = soup.find(class_='contentsWrapper').find_all(class_='itemModule')
    return content

def getAnimeInfo(elemnt):
    title=element.find(class_='line2').text
    elementNum=element.find(class_='textContainerIn').find(class_='number').text;
    number=re.search('([0-9]+)',elementNum).group(0)
    elementProgress=element.find(class_='progressCompleted').attrs['style']
    progress=re.search('([0-9]+)',elementProgress).group(0)
    return [title,number,progress]

    
def main():
    driver = webdriver.PhantomJS()
    driver.set_window_size(1500, 850)
    login(driver,baseURL+loginURL)
    getHistory(driver,baseURL+historyURL)
