from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from spotify import find_song

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'jpg','png','jpeg', 'PNG', 'JPG'}

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('files[]')
        artist = request.form.get('artist')
        title = request.form.get('title')

        for file in files:
            if file.filename == '':
                flash('No selected file')
                continue
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        find_song(title, artist)

        return render_template("index.html")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
