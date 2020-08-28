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
>/AI_Champ  
&nbsp;&nbsp;&nbsp;&nbsp;/PdFScraper.py  
&nbsp;&nbsp;&nbsp;&nbsp;/pdfToCSV.py  
&nbsp;&nbsp;&nbsp;&nbsp;/RemoveStopWords.py  
&nbsp;&nbsp;&nbsp;&nbsp;/API  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/FlaskAPI.py  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/template

#### PDFScraper   [ _Task 1 - Collect PDF for 50 LinkedIn Profiles_ ] 
PDF Scraper, obviously, scrapes PDFs of one's LinkedIn connections. Certain variables like username and password needs to be provided by the user. It uses selenium ( yes, it is a testing suite but here is being hacked a web scraper ) and Google Chrome.  
Note: The Script might be a bit slow because it pauses for 30 seconds before making another request in order to keep LinkedIn from blocking requests and having undesirable effects over your account. If you want to speed it up a bit change time.sleep(10) on line 61.(I don't recommend it.)
#### pdfToCSV   [ _Task 2 - Extracting text from CSV files collected in Task 1_ ]
This script a function and uses pandas and pdftotext library from PyPI. First it takes Directory Path where LinkedIn resumes are stored in a format like Profile.pdf, Profile (1).pdf ...upto Profile (N).pdf. In our case, N = 50.  
#### RemoveStopWords   [ _Task 3 - Preprocess text and Prints top 10 significant words_ ]
This script contains functions which remove stop words( Words used too often in language) from corpus, it happens to be text from LinkedIn profile, in our case. RemoveStopWords extract words from csv contained in a give path, removes symbols, then removes stopwords which are contained in NLTK. 
Then we use TF-IDF in order to find the most significant words from the corpus. This file also contains the function which will be used in API to find most significant words.
### API/   [ _Task 4 - API which extracts text from PDF and Return top 10 significant words_ ]
#### FlaskAPI
This is the api which is required in task 4 using flask framework. The api has 4 routes:  
 * /uploadPDF  
    Here is form to upload file which then makes api request to the "/textExtractor" which the perfoms text extraction from pdf with functions from "RemoveStopWords.py".
 * /textExtractor  
    This is the route where the actual extraction of text happens.
 * /uploadWords  
    This route renders the template containing the form to recive text input to extract the most significant and important words. On submit, it makes request to "/significantWords".
 * /significantWords  
    It is the api route which take input 'textdata' as POST request and return the most important words along with there count.
#### templates 
Templates contain the html templates for routes presented to the user.

# Setting up
Just make sure the Google Chrome is already installed on your system and we're good to go.
After that you will need to download chrome driver from [Google Storage API](https://chromedriver.storage.googleapis.com/index.html) and store it somewhere, preferably in the same folder as of project.  
I have used version 2.24. You want to choose which version to download.  
You want to run the scripts in the order in which they are listed here except the API.
### Setting up and running PDFScraper
If you have python3 installed that is well and good but if not, then you will need to install it.  
Then install selenium but executing
```
pip install selenium
```
After selenium is installed you will need to change a few variables in PDFScraper.py
>DOWNLOAD_DIR = Path where the pdfs should be downloaded( for me it was AI_Champ/PDFs )  
CHROME_EXECUTABLE = Path to the chrome driver  
Email = Your LinkedIn Email
Password = Your LinkedIn Password

Once those are set up you can execute
```
python3 PDFScraper.py
```
### Setting up and running pdftoCSV
First of all to install pdftotext execute :  
```
pip install pdftotext
```
If it shows any error then try again after installing it's dependencies which are listed in [PY PI](https://pypi.org/project/pdftotext/)  
Changes the following variables in pdfToCSV
>PDF_DIRECTORY = Path to where the pdfs are located or DOWNLOAD_DIR in PDFScraper  
CSV_FILE = Path to where the CSV should be stored  
NUMBER_OF_PDFs = Total number of pdfs in PDF_DIRECTORY  

Then execute the following and everything should work like a charm.
```
python3 pdfToCSV.py
```
If it shows up an error then you might want to check the variables once again.
### Setting up and running RemoveStopWords
It requires NLTK. So, execute :
```
pip install nltk
```
Variables you might want to change :  
>DIRECTORY = Path to the csv file generated via previous script or value CSV_FILE in pdfToCSV  

Then run the script by executing
```
python3 RemoveStopWords.py
```
### Setting up and running the api
Install flask via pip install and then run 
```
cd API
python3 FlaskAPI.py
```
The API should be up and running by now you can try it by opening http://127.0.0.1:5000/uploadWords or http://127.0.0.1:5000/uploadPDF in your browser.


# Prerequisites

* Selenium<br/>
* Python 3<br/>
* Google Chrome<br/>
* pdftotext<br/>
* Pandas<br/>
* NLTK<br/>
* Flask<br/>
 
