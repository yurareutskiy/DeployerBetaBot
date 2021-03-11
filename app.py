import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

from s3_uploader import uploadPublicFile

UPLOAD_FOLDER = os.environ.get("APP_HOME") + '/tmp'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'ipa', 'zip', 'json'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            fullpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            flash("Filename:", fullpath)
            file.save(fullpath)
            uploadPublicFile(fullpath, "bot_test")
            # os.remove(fullpath)
            return redirect(url_for('upload_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    print(os.environ.get("PORT"))
    print(UPLOAD_FOLDER)
    port = 3000 #int(os.environ.get("PORT"), 5000)
    if not port:
        print("❌Port is not defined")
    else:
        print("✅Port", port)
        app.debug = True
    app.run(host='0.0.0.0', port = port)