import string
class Musical:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.songs = dict()


class Song:
    def __init__(self, name, url, lyrics):
        self.name = name
        self.lyrics = lyrics

def ispunct(ch):
    return ch in string.punctuation


def getName(s):
    i = 0
    while i < len(s) and (s[i].isupper() or s[i] == ' ' or s[i] == '.') and (not ispunct(s[i]) or s[i] == '.'):
        i += 1
    return s[:i].strip()


def analyze(lyrics):
    characters = dict()
    while lyrics.find("[") != -1:
        header = lyrics[lyrics.find("[") + 1: lyrics.find("]")]
        name = getName(header)
        lyrics = lyrics[lyrics.find("]") + 1:].strip()
        paragraph = lyrics[: lyrics.find("[")].strip()
        if paragraph != '':
            if name not in characters.keys():
                characters[name] = []
            characters[name].append(paragraph)

        lyrics = lyrics[lyrics.find("["):].strip()

    for key, value in characters.items():
        print(key + ": ", value)

musicals = [Musical("Heathers", "https://genius.com/artists/Heathers-the-musical-ensemble")]