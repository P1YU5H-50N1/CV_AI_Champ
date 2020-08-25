# Description

This repository contains scripts and code for four tasks:  
1. Download 50 public profile PDFs of your connections (randomly) from LinkedIn.  
2. Extract text from the above PDFs and store them in a CSV.  
3. For every profile data (text), find out the most frequent words and essential words used. It
shouldn’t contain stop words (like is, the, an, etc.).  
4. Create two web APIs using flask/Django or another framework of your choice.
    * The first web API should take a PDF file as input and return the text in it in JSON
    format.  
    * The second web API should take text data as input and return the most frequent
    words and important words (as mentioned in 3) in JSON format.  

# Files And Directory Structure
#### PDFScraper.py
PDF Scraper, obviously, scrapes PDFs of one's LinkedIn connections. Certain variables like username and password needs to be provided by the user. It uses selenium (yes, it is a testing suite but here is being hacked a web scraper ) and Google Chrome.  
#### pdfToCSV.py
This script contains two functions and uses pandas and pdftotext library from PyPI. First it takes Directory Path where LinkedIn resumes are stored in a format like Profile.pdf, Profile (1).pdf ...upto Profile (N).pdf. In our case, N = 50.  
#### RemoveStopWords.py
This script contains functions which remove stop words( Words used too often in language) from corpus, it happens to be text from LinkedIn profile, in our case. RemoveStopWords extract words from csv contained in a give path, removes symbols, then removes stopwords which are contained in NLTK. Still, there would remain a few words which behave like stop words. It also removes those words which are above 95 percentile of word counts.
# Prerequisites

* Selenium<br/>
* Python 3<br/>
* Google Chrome<br/>
* pdftotext<br/>
* Pandas<br/>
* NLTK<br/>
 
