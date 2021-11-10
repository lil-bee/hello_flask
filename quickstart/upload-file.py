from flask import Flask, app, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload')
def show_upload_form():
    return render_template('upload.htm')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files[file]
        f.save(secure_filename(f.filename))
        return 'file uploaded'