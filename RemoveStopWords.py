import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import math
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def RemoveSymbols(Words):

    # included @ because of emails
    alphanums = "abcdefghijklmnopqrstuvwxyz@ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    website_regex = r"^www.|^http:\/\/|^https:\/\/"
    result = []
    Symbols = set()
    temp = []

    for word in Words:
        for letter in word:
            if not letter in alphanums and not letter in Symbols:
                Symbols.add(letter)
    for word in Words:
        if not re.search(email_regex,word):
            if not re.search(website_regex,word):
                for sym in Symbols.intersection(set(word)):
                    word = word.replace(sym,' ')
        temp = word.split(' ')
        for exceptEmptyCharacters in temp:
            if exceptEmptyCharacters != '':
                result.append(exceptEmptyCharacters)

    return result

def topN_Words(Corpus,n):
    if type(Corpus) == str:
        Corpus = [Corpus]
    vectorizer = TfidfVectorizer(token_pattern= '(\S+)')
    response = vectorizer.fit_transform(Corpus)
    TF_Matrix = pd.DataFrame(response.toarray(),columns = vectorizer.get_feature_names())
    TFidf_Sum = TF_Matrix.sum(axis = 0)
    Result = TFidf_Sum.sort_values(ascending = False)
    Result = list(Result.index)
    Result = [word for word in Result if len(word)>1]
    Result = Result[:n]
    return Result
    
def Process_Text(CSV_path):

    N = 10
    stop_Words = set(stopwords.words('english')) 
    df = pd.read_csv(CSV_path)
    sentences = [' '.join(list(word.lower() for word in df.loc[pdf_text][0].split())) for pdf_text in range(50) ]
    sentences = [' '.join(RemoveSymbols(sentence.split())) for sentence in sentences]
    Cleaned_Corpus = [ ' '.join([word for word in sentence.split() if not word in stop_Words ]) for sentence in sentences]
    Result = topN_Words(Cleaned_Corpus,N)
    return Result

def Process_Text_For_API(Text):

    N = 10
    Text = ''.join(Text)
    stop_Words = set(stopwords.words('english')) 
    sentences = ' '.join([word.lower() for word in Text.split()])
    sentences = ' '.join(RemoveSymbols(sentences.split()))
    Cleaned_Corpus = ' '.join([word for word in sentences.split() if not word in stop_Words ])
    Result = topN_Words(Cleaned_Corpus,N)
    return Result

def serverSnippet(Text):
    if type(Text) == str:
        Text = list(Text)
    Imp_Words = Process_Text_For_API(Text)
    return Imp_Words

if __name__ == '__main__':

    DIRECTORY = 'CSVs/Resumes.csv'
    Imp_Words = Process_Text(DIRECTORY)
    print(Imp_Words)
