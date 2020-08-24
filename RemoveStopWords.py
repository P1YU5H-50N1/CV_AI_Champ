import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def RemoveStopWords(CSV_path):

    stop_Words = set(stopwords.words('english')) 
    df = pd.read_csv(CSV_path)
    words = [str(word).lower() for row in range(50) for word in df.loc[row] if pd.notnull(word)]
    RefinedWords = [word for word in words if not word in stop_Words]
    return RefinedWords

if __name__ == '__main__':

    Directory = 'CSVs/Resumes.csv'
    RefinedWords = RemoveStopWords(Directory)

    print(len(RefinedWords))