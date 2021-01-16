from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = /templates
ALLOWED_EXTENSIONS = {'jpg','png','jpeg'}

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('files[]')

        for file in files:
            file.save("")
            print("file_received")
        
        return render_template("index.html")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
