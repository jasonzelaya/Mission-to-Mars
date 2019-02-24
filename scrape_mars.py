# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    
    return Browser("chrome", **executable_path, headless=True)

# Create Mission to Mars global dictionary that can be imported into Mongo
mars_info = {}


# Step 2.1 - MongoDB


def scrape_mars_latest_news():
    try:
        browser = init_browser()   
        
        mars_news_url = "https://mars.nasa.gov/news/"
        browser.visit(mars_news_url)
        
        html = browser.html
        
        soup = BeautifulSoup(html, "html.parser")
        
        latest_news_title = soup.find("div", class_="content_title").text
        latest_news_para = soup.find("div", class_="article_teaser_body").text
        
        mars_info["news_title"] = latest_news_title
        mars_info["news_paragraph"] = latest_news_para
        
        return mars_info
    
    finally:
        browser.quit()

def scrape_mars_latest_news():
    try:
        browser = init_browser()   
        
        latest_news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
        browser.visit(latest_news_url)
        
        html = browser.html
        
        soup = BeautifulSoup(html, "html.parser")
        
        news_title = soup.find("div", class_="content_title").text
        news_p = soup.find("div", class_="article_teaser_body").text
        
        # Dictionary entry
        mars_info["news_title"] = news_title
        mars_info["news_paragraph"] = news_p
        
        return mars_info
    
    finally:
        browser.quit()


# JPL Mars Space Images - Featured Image
def scrape_mars_featured_image():
    try: 
        browser = init_browser()

        img_search_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(img_search_url)
 
        html_image = browser.html

        soup = BeautifulSoup(html_image, 'html.parser')

        # Retrieve background image url
        featured_image_url = soup.find("article")["style"].replace("background-image: url(","").replace(");", "")[1:-1]

        main_url = "https://www.jpl.nasa.gov"

        # Concatenate website url with scraped route
        featured_image_url = main_url + featured_image_url

        featured_image_url 

        # Dictionary entry
        mars_info['featured_image_url'] = featured_image_url 
        
        return mars_info
    
    finally:

        browser.quit()

# Mars Weather
def scrape_mars_weather():
    try: 

        browser = init_browser()

        weather_url = "https://twitter.com/marswxreport?lang=en"
        browser.visit(weather_url)
         
        html_weather = browser.html

        soup = BeautifulSoup(html_weather, "html.parser")

        # Find all elements that contain tweets
        latest_weather_tweets = soup.find_all("div", class_="js-tweet-text-container")

        # Retrieve all elements that contains news title in a specified range and look for entries that display weather related words to exclude non weather related tweets
        for tweet in latest_weather_tweets:
            mars_weather = tweet.find("p").text
            if "Sol" and "pressure" in weather_tweet:
                print(weather_tweet)
                break
            else:
                pass

        # Dictionary entry
        mars_info["mars_weather"] = mars_weather
        
        return mars_info
    
    finally:

        browser.quit()

# Mars Facts
def scrape_mars_facts():

    # Visit Mars facts url 
    mars_facts_url = "https://space-facts.com/mars/"

    mars_facts = pd.read_html(mars_facts_url)

    mars_facts_df = mars_facts[0]

    mars_facts_df.columns = ["description", "value"]

    mars_facts_df.set_index("description", inplace=True)

    # Save html code
    mars_facts_df.to_html()

    # Dictionary entry
    mars_info["mars_facts"] = data
   
    return mars_info

# Mars Hemispheres
def scrape_mars_hemispheres():
    try: 
        # Initialize browser 
        browser = init_browser()

        hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(hemispheres_url)

        html_hemispheres = browser.html

        soup = BeautifulSoup(html_hemispheres, "html.parser")

        items = soup.find_all("div", class_="item")

        hemisphere_img_urls = [] 

        hemispheres_main_url = "https://astrogeology.usgs.gov" 

        for i in items:
            # Store title
            title = i.find("h3").text
    
            # Store link that leads to the full image website
            partial_img_url = i.find("a", class_="itemLink product-item")["href"]
    
            # Visit the link that contains the full image website
            browser.visit(hemispheres_main_url + partial_img_url)
    
            # HTML object of individual hemisphere information website
            partial_img_html = browser.html
    
            # Parse HTML for every individual hemisphere information website
            soup = BeautifulSoup(partial_img_html, "html.parser")
    
            # Retrieve the full image source
            img_url = hemispheres_main_url + soup.find("img", class_="wide-image")["src"]
    
            # Append the retrieved information into a list of dictionaries
            hemisphere_img_urls.append({"title" : title, "img_url" : img_url})

        mars_info['hemisphere_img_urls'] = hemisphere_img_urls

        # Return mars_info dictionary
        return mars_info
    
    finally:

        browser.quit()