import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests

tracks=[]
with open('track_list.txt','r') as f:
    titles_list=f.readlines( )
    titles=[titles.strip() for titles in titles_list]



# Setup Selenium WebDriver

titles_mini=titles[0:5]
genre_t=[]

i=0
for title in titles_mini:
    genre=[]
    url=f'https://www.imdb.com/title/{title}/'
    response=requests.get(url,headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
})
    soup=BeautifulSoup(response.content,'html.parser')
    genres=soup.find_all('a',class_='ipc-chip ipc-chip--on-baseAlt',limit=3)
    for tags in genres:
        genre.append(tags.text)
    genre_t.append(genre)
    print(i)
    i+=1
    

