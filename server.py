from flask import Flask, render_template, flash, request, redirect, url_for
from spotify import find_song

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
        artist = request.form.get('artist')
        title = request.form.get('title')
        find_song(title, artist)

        return render_template("index.html")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
