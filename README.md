# Electric-Guitar-Price-Prediction: Project Overview
I am plannig to buy a electric guitar in the future, but I do not know what are things I should consider. Therefore, I decided to make some data analysis to understand the what are the important features of an electric guitar that impact the cost, and train a machine learning model to predict the cost of an electric guitar. In order to tackle this problem I performed the following steps:
* I searched the Internet to find a good dataset, but I could not find. So that, I scraped the www.findmyguitars.com and collect approximately 1600 electric guitars.
* I performed some data analysis to gain insights from the data.
* I trained various machine learning algorithms to get the best performance. Performance metrics for the best one:
  * Mean Squared Error: 187.6$
  * Mean Absolute Error: 134.5$
* * Mean Absolute Percentage Error: 14% (Maybe this one is a better indicator, since the errors for 2000$ electric guitar and 500$ will be different.)
* Lastly, I productionarize the model with Streamlit library on heroku, so that anyone can enter the site before searching on the internet for electric guitars, and get some general idea about the price for the features that s/he wants. Web site is hosted on https://electric-guitar-price-pred.herokuapp.com/.
## Web Scraping
## Data Cleaning
## Exploratory Data Analysis
## Model Building
## Application
