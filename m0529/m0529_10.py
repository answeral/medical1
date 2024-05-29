import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://namu.wiki/RecentChanges'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

soup = BeautifulSoup(browser.page_source,"lxml")
with open("flight.html","w",encoding="utf8") as f:
    f.write(soup.prettify())    

titles = soup.find("div",{"class":"aunJwsbN"})
title = titles.find_all("div",{"class":"b5G6-Ki+"})

urls = 'https://namu.wiki'+ title[1].a['href']


