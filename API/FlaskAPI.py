from flask import Flask, render_template, request, jsonify
import pdftotext
import sys

sys.path.append('../')
from RemoveStopWords import serverSnippet

app = Flask(__name__,template_folder='template')
app.config['UPLOAD_FOLDER'] = '/API_Test'
app.config['MAX_CONTENT_PATH'] = 100000000000000000000000000000

@app.route('/significantWords',methods = ['POST'])
def impWords():
    if request.method == 'POST':

        text = request.form['textdata']
        text = str(text)
        response = dict()
        response['Imp_Words'] = serverSnippet(text)
        return jsonify(response)

@app.route("/",methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/uploadWords',methods = ['GET'])
def uploadText():
    return render_template('submitText.html')

@app.route('/uploadPDF',methods = ['GET'])
def upload_file():
    return render_template('uploadPDF.html')

@app.route('/textExtractor', methods = ['GET','POST'])
def text_Extractor():
    if request.method == 'POST':
        
        response = dict()
        CurrentdocCorpus = ''
        pdf = pdftotext.PDF(request.files['file'])
        
        for page in pdf:
            CurrentdocCorpus = CurrentdocCorpus + '\n' + page
            
        response['text'] = CurrentdocCorpus
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug = True)