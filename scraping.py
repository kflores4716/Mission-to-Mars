# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

# Define a new 'scrape_all' function
def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    # Set our news title and paragraph variables
    news_title, news_paragraph = mars_news(browser)
    hemisphere_image_urls = hemisphere(browser)
    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": hemisphere_image_urls,
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data


# Set executable path
# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser('chrome', **executable_path, headless=False)

# Insert below code into a function
def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    # url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Set up HTML Parser, convert to soup object
    html = browser.html
    news_soup = soup(html, 'html.parser')
    
    # Add try/except for error handling
    try:
        # Begin Scraping
        slide_elem = news_soup.select_one('div.list_text')

        # Find specific data within our slide_elem variable
        # slide_elem.find('div', class_='content_title')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p

# ### Featured Images

# Declare and Define function for Featured Image
def featured_image(browser):

    # Visit URL
    url = 'https://spaceimages-mars.com'
    # url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    # img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url



# ## Mars Facts

# Define our function
def mars_facts():
    # Add try/except for error handling
    try:
        # Using pd.read_html() to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
        # df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    

    # Convert DataFrame back into HTML-ready code
    return df.to_html(classes = "table table-striped")

# CHALLENGE: Create function for scraping hemisphere data
def hemisphere(browser):
    # Visit the url
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    # Create empty list
    hemisphere_image_urls = []
    # Get list of all hemispheres
    links = browser.find_by_css('a.product-item img')

        # Create the for loop
    for i in range(len(links)):
        
        #create empty dictionary
        hemispheres = {}
        
        # Find the elements on each loop 
        browser.find_by_css('a.product-item h3')[i].click()
        
        # Find Sample image anchor tag --> extract href
        element = browser.links.find_by_text('Sample').first
        # Store href in img_url variable
        img_url = element['href']
        
        # Get the titles and store in title variable
        title = browser.find_by_css("h2.title").text
        
        # Add the two variables to the hemispheres dictionary 
        hemispheres["img_url"] = img_url
        hemispheres["title"] = title
        
        # Append the hemisphere_image_urls list with the hemispheres dictionary
        hemisphere_image_urls.append(hemispheres)
        
        # Navigate backwards
        browser.back()
    # Return the image urls list of dictionaries
    return hemisphere_image_urls



if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())
    