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
    PDF_DIRECTORY = 'PDFs'
    CSV_FILE = 'CSVs/Resumes.csv'
    NUMBER_OF_PDFs = 50
    print('Starting the job.....')
    for i in range(NUMBER_OF_PDFs):
        if i != 0:
            Path = PDF_DIRECTORY + '/Profile (' + str(i) + ').pdf'
        else:
            Path = PDF_DIRECTORY + '/Profile.pdf'
        
        Corpus.append(' '.join(pdfToWords(Path)))

    csv = pd.DataFrame(Corpus)
    f = open(CSV_FILE,'w')
    f.close()
    csv.to_csv(CSV_FILE,index = False)
    print("Completed Successfully...")