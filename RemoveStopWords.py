import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def RemoveRemainingStopWords(WordList,WordCounts,PercentileTh):
    
    WordFreqData = pd.DataFrame(WordCounts.values())
    MaxWordCount = list(WordFreqData.quantile([PercentileTh])[0])[0]
    CustomStopWords = [stopWord for stopWord in WordCounts if WordCounts[stopWord] > MaxWordCount]
    Result = [word for word in WordList if not word in CustomStopWords]
    return Result

def CountWordFrequecy(Words):

    UniqueWords = list(set(Words))
    WordFreq = dict()
    for word in UniqueWords:
        WordFreq[word] = Words.count(word)
    return WordFreq


def RemoveSymbols(Words):

    # included @ because of emails
    alphanums = "abcdefghijklmnopqrstuvwxyz@1234567890"
    result = []
    Symbols = set()
    temp = []

    for word in Words:
        for letter in word:
            if not letter in alphanums and not letter in Symbols:
                Symbols.add(letter)
    for word in Words:
        for sym in Symbols.intersection(set(word)):
            word = word.replace(sym,' ')
        temp = word.split(' ')
        for exceptEmptyCharacters in temp:
            if exceptEmptyCharacters != '':
                result.append(exceptEmptyCharacters)

    return result

def Remove_NLTK_StopWords(CSV_path):

    stop_Words = set(stopwords.words('english')) 
    df = pd.read_csv(CSV_path)
    words = [str(word).lower() for row in range(50) for word in df.loc[row] if pd.notnull(word)]
    words = RemoveSymbols(words)
    RefinedWords = [word for word in words if not word in stop_Words]
    return RefinedWords

def Remove_NLTK_StopWords2(Text):

    stop_Words = set(stopwords.words('english')) 
    Words = Text.split()
    words = [str(word).lower() for word in Words]
    words = RemoveSymbols(words)
    RefinedWords = [word for word in words if not word in stop_Words]
    return RefinedWords

def serverSnippet(Text):
    PercentileThreshold = 0.95
    Words = Remove_NLTK_StopWords2(Text)
    WordFrequency = CountWordFrequecy(Words)
    Result = RemoveRemainingStopWords(Words,WordFrequency,PercentileThreshold)
    Result = CountWordFrequecy(Result)
    return Result

if __name__ == '__main__':

    Directory = 'CSVs/Resumes.csv'
    PercentileThreshold = 0.95
    Words = Remove_NLTK_StopWords(Directory)
    WordFrequency = CountWordFrequecy(Words)
    Result = RemoveRemainingStopWords(Words,WordFrequency,PercentileThreshold)
    print(len(Result))
    print(Result)
