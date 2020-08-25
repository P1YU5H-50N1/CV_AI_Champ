from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__,template_folder='template')
app.config['UPLOAD_FOLDER'] = '/API_Test'
app.config['MAX_CONTENT_PATH'] = 100000000000000000000000000000


@app.route('/', methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug = True)