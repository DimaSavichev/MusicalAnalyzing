from flask import Flask, render_template, request
from scrapping import scrapSongs, scrapLyrics
from musicals import analyze, Song, Musical, musicals

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", musicals=musicals)


@app.route('/songs', methods=['GET'])
def songs():
    songs = scrapSongs("lol")  # musicals[request.args.get('musical', '')])
    return render_template("songs.html", songs=songs)


@app.route('/analyze', methods=['POST'])
def lyrics():
    # musical = musicals[request.args.get('musical', '')]
    print(request.values)
    song_url = request.form.get('song_url')
    lyrics = scrapLyrics(song_url)
    characters = analyze(lyrics)
    return render_template("analyze.html", characters=characters, params=["word_count", "emotionality"], song_url=song_url)


if __name__ == '__main__':
    app.run()
