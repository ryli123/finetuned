from flask import Flask, render_template, flash, request, redirect, url_for, session
from flask_session import Session
from werkzeug.utils import secure_filename
from tempfile import mkdtemp
import os
from spotify import find_song
from genius import calc_sentiment, find_lyrics
from phototest import song_to_image


UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'jpg','png','jpeg'}

app = Flask(__name__)
Session(app)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


Session(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        return redirect('/start')

    return render_template("index.html")

@app.route('/start', methods=["GET", "POST"])
def start():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('files[]')

        file_list=[]
        for file in files:
            if file.filename == '':
                flash('No selected file')
                continue
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(path)
                file_list.append(path)

        session["images"] = file_list
        
        return redirect(url_for('song'))

    return render_template("start.html")


@app.route('/song', methods=["GET", "POST"])
def song():
    if request.method == 'POST':
        artist = request.form.get('artist')
        title = request.form.get('title')

        session["song_info"] = find_song(title, artist)
        # check if this is correct
        session['sentiment_num'] = calc_sentiment(find_lyrics(title, artist))
        return redirect(url_for("edited"))

    if session.get("images") is None:
        return redirect('/start')

    return render_template("song.html", images=session["images"])


@app.route('/edited', methods=["GET", "POST"])
def edited():
    
    if request.method == 'POST':
        session.clear()
        return redirect('/start')

    if session.get("images") is None:
        return redirect('/start')
    elif session.get("song_info") is None:
        return redirect('/song')

    images = []
    for image in session["images"]:
        #images.append(song_to_image(image, session["song_info"]))
        images.append(song_to_image(image, session["song_info"], session['sentiment_num'])) #pass in sentiment_num set of (pos, neg, neutral) as well
    return render_template("edited.html", images=images)




if __name__ == "__main__":
    app.run(debug=True)
