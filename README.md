# Mission-to-Mars

### Objective of Project
The main goal for this project was to create `.ipynb`, `.py`, and `.html` files that work together to scrape Mars data from other websites and present them on a separate webpage. We started by working out a general template of how we want the webpage to look, and then began writing our code. Starting in Jupyter Notebook, we wrote some code that would scrape the desired data from the referrenced websites and store it in a MongoDB database. We then imported that `.ipynb` file into Visual Studio Code and began transforming it into a `.py` file. Once we finished up the `.py` file, we created our `.html` file that references our scraped data in MongoDB. The `.html` file pulls in the data and formats it properly so that it's displayed according to our general template that we worked out at the beginning.

The end result is a webpage that displays the most recent article from `https://redplanetscience.com` along with a short preview of what the article is about. It also displays a table of facts about Mars and Earth that we scraped from `https://galaxyfacts-mars.com`, along with the most recent image published to `https://spaceimages-mars.com`. Lastly, at the bottom section, the page displays four labeled images, one for each of Mars' hemispheres, that was scraped from `https://marshemispheres.com/`. 

At the top of the page and right underneath the title, there is a button that, when pressed, scrapes the newest data from the referenced websites.

### Resources

##### Applications Used:
Jupyter Notebook
Visual Studio Code
MongoDB

##### Websites:
https://redplanetscience.com
https://spaceimages-mars.com
https://galaxyfacts-mars.com
https://marshemispheres.com/

##### NOTE: 
At some point, the Module started using different urls in the code than what we started with. I tried using them but ran into issues, so I commented them out and stuck with the first urls that they had us reference.

Also, for Deliverable 1 of the Module, several other students and I were working with a TA to figure out how to write the `for` loop . Ultimately, we worked it out, but there were a lot of us working together so our `for` loops are probably very similar to each other.
