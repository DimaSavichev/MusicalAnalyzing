class Musical:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.songs = dict()


class Song:
    def __init__(self, name, url, lyrics):
        self.name = name
        self.lyrics = lyrics


def analyze(lyrics):
    pass


musicals = [Musical("Heathers", "https://genius.com/artists/Heathers-the-musical-ensemble")]