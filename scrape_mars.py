 # Dependencies
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
from splinter import Browser
import time


def mars_data():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    #put info from mars news and puts in master function that we call in browser
    title,description = mars_news(browser)

    dictionary = {
        "mars_newstitle": title,
        "mars_newsdecription": description,
        "jpl_link": mars_images(browser),
        #"mars_tweet": twitter(browser)
        #"mars_facts": mars_facts(browser)
        #"hemispheres_info": hemisphere_image_urls(browser)
    }
    return dictionary


def mars_news(browser):
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')

    article_one = soup.find_all('div', class_="slide")[0]
    title = article_one.find('div', class_="content_title").a.text
    description = article_one.find('div', class_="rollover_description_inner").text

    return(title,description)

def mars_images(browser):
    # URL of page to be scraped
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    link_url = 'https://www.jpl.nasa.gov'

    #splinter accessing the website and this appears in the splinter browser
    browser.visit(jpl_url)

    #tell splinter to find the button and click using find by id method and store result in variable
    image_button = browser.find_by_id("full_image")
    image_button.click()

    #tell splinter to click more info button however need page to load first
    time.sleep(2)
    browser.click_link_by_partial_text("more info")

    #Grab the html page that splinter is on
    html = browser.html
    jpl_soup = BeautifulSoup(html, 'html.parser')

    img_src = jpl_soup.find("img", class_="main_image")["src"]
    new_src = link_url + img_src
    return(new_src)

# def twitter(browser):
#     # URL of page to be scraped
#     mars_twitter_url = 'https://twitter.com/marswxreport?lang=en'
#
#     # Retrieve page with the requests module
#     twitter_response = requests.get(mars_twitter_url)
#     twitter_soup = BeautifulSoup(twitter_response.html, 'html.parser')
#
#     tweets = twitter_soup.find('ol', class_='stream-items')
#     mars_weather = tweets.find('p', class_="tweet-text")
#
#     return(mars_weather)


# def mars_factsfunction(browser):
#     facts_url = "https://space-facts.com/mars/"
#     facts_response = requests.get(facts_url)
#     facts_soup = BeautifulSoup(facts_response.text, 'html.parser')


#     diagram_table = facts_soup.find('table', class_='tablepress tablepress-id-comp-mars blue-table')
#     column1 = diagram_table.find_all('td', class_='column-1')
#     column2 = diagram_table.find_all('td', class_='column-2')
#     column3 = diagram_table.find_all('td', class_='column-3')

#     Col_1s = []
#     Col_2s = []
#     Col_3s = []

#     for row in column1:
#         row_1s = row.text.strip()
#         Col_1s.append(row_1s)

#     for row in column2:
#         row_2s = row.text.strip()
#         Col_2s.append(row_2s)

#     for row in column3:
#         row_3s = row.text.strip()
#         Col_3s.append(row_3s)


#     mars_facts = pd.DataFrame({
#         "Mars - Earth Comparison":Col_1s,
#         "Mars":Col_2s,
#         "Earth": Col_3s
#         })

#     mars_facts_html = mars_facts.to_html(header=False, index=False)
#     return(mars_facts)


# def hemi(browser):

#      # URL of page to be scraped
#     hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

#     #splinter accessing the website and this appears in the splinter browser
#     browser.visit(hemi_url)

#     #tell splinter to find the button and click using find by id method and store result in variable
#     #want loop to iterate 4 times

#     #push objects into list
#     hemisphere_image_urls = []


#     for i in range(4):
#         image_library = {}

#         image_button = browser.find_by_tag("h3")
#         image_button[i].click()
#         #beautiful soup each page
#         # URL of page to be scraped
#         html = browser.html
#         page_soup = BeautifulSoup(html, 'html.parser')

#         img_url = browser.find_by_id("fgdcLink")
#         img_title = browser.find_by_tag("title")

#         hemisphere_image_urls.append(img_url)
#         hemisphere_image_urls.append(img_title)


#         #store link and title in dictionary
#         #hemisphere_image_urls.append({"title": hemisphere_image_title, "img_url": hemisphere_image_urls})

#         browser.back()

#     return(hemisphere_image_urls)
