import pandas as pd
import pdftotext

def pdfToWords(DocPath):

    with open(DocPath, "rb") as f:
        pdf = pdftotext.PDF(f)

    CurrentdocCorpus = ''

    for page in pdf:
        CurrentdocCorpus = CurrentdocCorpus + '\n' + page

    CurrentdocCorpus = CurrentdocCorpus.split()
    
    return CurrentdocCorpus


if __name__=="__main__":

    Corpus = []

    print('Starting the job.....')
    for i in range(50):
        if i != 0:
            Path = 'PDFs/Profile (' + str(i) + ').pdf'
        else:
            Path = 'PDFs/Profile.pdf'
        
        Corpus.append(pdfToWords(Path))

    csv = pd.DataFrame(Corpus)
    f = open('CSVs/Resumes.csv','w')
    f.close()
    csv.to_csv('CSVs/Resumes.csv',index = False)
    print("Completed Successfully...")