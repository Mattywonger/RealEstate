

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re as re
import time
import pandas as pd
from linkedin_scraper import Person, actions
import pymongo
from pymongo import MongoClient
import requests
from requests import get
from bs4 import BeautifulSoup



if __name__ == "__main__":
  
    response = get('https://sfbay.craigslist.org/search/eby/apa?hasPic=1&availabilityMode=0') #get rid of those lame-o's that post a housing option without a pic using their filter
    print(response.status_code)
    html_soup = BeautifulSoup(response.text, 'html.parser') #response.text accesses the html portion of the response object of the get request
    posts =html_soup.find_all(html_soup.find_all(class_='results cl-results-page'))
    post1= posts[0]
    priceinfo = post1.find('div', class_='price')
    price_text = priceinfo.get_text(strip=True)
    print(price_text)
  

