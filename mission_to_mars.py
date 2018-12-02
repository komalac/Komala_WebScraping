
## Importing needed libraries

import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from splinter import Browser

def scrape_fn():
    scrape_dic = {}

    # ## Scrape latest news from NASA Mars News

    # opening browser through Selenium
    # options = Options()
    driver = webdriver.Chrome()                        
    driver.get('https://mars.nasa.gov/news/')
    time.sleep(3)
    pg_source = driver.page_source
    driver.quit

    # render html BeautifulSoup
    soup = BeautifulSoup(pg_source, "html.parser")


    # retrieve latest new title
    news_title = soup.find("div", {"class": "content_title"}).text.strip()
    # news_title
    scrape_dic.update({'news_title':news_title})

    # retrieve latest news info
    news_info = soup.find("div", {"class": "article_teaser_body"}).text.strip()
    # news_info
    scrape_dic.update({'news_info':news_info})

######################################################################################################
    ## Scrape images from JPL Mars Space Images

    # executable_path = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **executable_path, headless=False)
    # url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    # browser.visit(url)
    # browser.click_link_by_partial_text('FULL IMAGE')

    # render html BeautifulSoup
    # html = browser.html
    # soup = BeautifulSoup(html, "html.parser")
    # img_url = url.split('?')[0]
    # Img_info = soup.find("img", {"class": "fancybox-image"})['src'].split('/')

    # for i in range(2, len(Img_info)-1):
    #     img_url = img_url + Img_info[i] +'/'
        
    # featured_image_url = img_url + Img_info[len(Img_info)-1]

    # scrape_dic.update({'featured_image_url':featured_image_url})

    # featured_image_url

#########################################################################################################

    # ### Mars Weather



    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    # render html BeautifulSoup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # retrieve latest new title
    mars_weather = soup.find("p", {"class": "TweetTextSize"}).text
    # mars_weather

    scrape_dic.update({'mars_weather':mars_weather})

    # ### Mars Facts

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'http://space-facts.com/mars/'
    browser.visit(url)

    # render html BeautifulSoup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    mars_facts = [] # store all of the records in this list
    for row in soup.findAll('tr'):
        col = row.findAll('td')
        title = col[0].text.strip()
        data = col[1].text.strip()
        fact = (title, data) 
        mars_facts.append(fact)

    scrape_dic.update({'mars_facts':mars_facts})

    # mars_facts


    # ## Mars Hemispheres

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # render html BeautifulSoup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    mainlink = "https://astrogeology.usgs.gov"
    hemis_list = []
    for i in soup.find_all('div', {'class': 'item'}):
        hemis_info = {            
            'title':  i.find('img')['alt'],
            'imgsrc': mainlink + i.find('img')['src']
        }
        hemis_list.append(hemis_info)
    
    scrape_dic.update({'hemis_list':hemis_list})

    # hemis_list

    return scrape_dic;