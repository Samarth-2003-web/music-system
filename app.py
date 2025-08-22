
import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Path to your static music folder
MUSIC_FOLDER = os.path.join("static", "music")

@app.route("/")
def index():
    songs = []
    # scan static/music for mp3, wav, etc.
    for filename in os.listdir(MUSIC_FOLDER):
        if filename.lower().endswith((".mp3", ".wav", ".ogg")):
            songs.append({
                "title": os.path.splitext(filename)[0],  # song name without extension
                "file": url_for('static', filename=f"music/{filename}")  # serve via Flask
            })

    return render_template("index.html", songs=songs)


if __name__ == "__main__":
    app.run(debug=True)
import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Path to your static music folder
MUSIC_FOLDER = os.path.join("static", "music")

@app.route("/")
def index():
    songs = []
    # scan static/music for mp3, wav, etc.
    for filename in os.listdir(MUSIC_FOLDER):
        if filename.lower().endswith((".mp3", ".wav", ".ogg")):
            songs.append({
                "title": os.path.splitext(filename)[0],  # song name without extension
                "file": url_for('static', filename=f"music/{filename}")  # serve via Flask
            })

    return render_template("index.html", songs=songs)


if __name__ == "__main__":
    app.run(debug=True)
