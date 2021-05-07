from flask import Flask, render_template, request
from scrapping import scrapSongs, scrapLyrics
from musicals import analyze, Song, Musical, musicals

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", musicals=musicals)


# @app.route('/songs', methods=['GET'])
# def songs():
#     songs = scrapSongs(musicals[request.args.get('musical', '')])
#     return render_template("index.html", musicals=musicals)


@app.route('/analyze', methods=['GET'])
def lyrics():
    musical = musicals[request.args.get('musical', '')]
    song = musical.songs[request.args.get('song', '')]
    lyrics = scrapLyrics(song.url)
    song.analyze(lyrics)
    return render_template("analyze.html", song=song)


if __name__ == '__main__':
    app.run()
