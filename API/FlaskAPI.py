from flask import Flask, render_template, request, jsonify
import pdftotext

app = Flask(__name__,template_folder='template')
app.config['UPLOAD_FOLDER'] = '/API_Test'
app.config['MAX_CONTENT_PATH'] = 100000000000000000000000000000

@app.route('/textExtractor',methods = ['GET'])
def text_Extractor():
    return render_template('upload.html')

@app.route('/uploadPDF', methods = ['GET','POST'])
def upload_file():
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