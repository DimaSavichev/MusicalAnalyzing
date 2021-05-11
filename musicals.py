import string
import re

class Musical:
    def __init__(self, name, url):
        self.name = name
        self.url = url


class Song:
    def __init__(self, name, url):
        self.name = name
        self.url = url


class Character:
    def __init__(self, name):
        self.name = name
        self.paragraphs = []


def ispunct(ch):
    return ch in string.punctuation


def getNames(s):
    i = 0

    # while i < len(s) and (s[i].isupper() or s[i] in " .'") and (not ispunct(s[i]) or s[i] == '.'):
    #     i += 1
    s = s.replace("’", "'")
    result = re.findall(r"\b[A-Z .']+\b", s)
    for i in range(len(result)):
        result[i] = result[i].strip()

    # result = list(filter(lambda x: x != '', result))
    print(result)
    return result


def parseCharacters(lyrics):
    characters = dict()
    while lyrics.find("[") != -1:
        header = lyrics[lyrics.find("[") + 1: lyrics.find("]")]
        names = getNames(header)
        lyrics = lyrics[lyrics.find("]") + 1:].strip()
        paragraph = lyrics[: lyrics.find("[")].strip()
        if paragraph != '':
            for name in names:
                if name not in characters.keys():
                    characters[name] = Character(name)
                characters[name].paragraphs.append(paragraph)

        lyrics = lyrics[lyrics.find("["):].strip()

    return characters


def count_words(character):
    return sum([sum([i.strip(string.punctuation).isalpha() for i in j.split()]) for j in character.paragraphs])


def count_substrs(character, substr):
    return sum([i.count(substr) for i in character.paragraphs])


def count_unfinished(character):  # считает количество параграфов, в конце которых нет знака препинания
    return sum([not ispunct(i[-1]) for i in character.paragraphs])


def emotionality(character):
    all_endings = count_substrs(character, ".") + count_substrs(character, "?") + count_substrs(character, "!") + count_unfinished(character)
    if all_endings != 0:
        return count_substrs(character, "!") / all_endings
    else:
        return 0


def analyze(lyrics):
    characters = parseCharacters(lyrics)
    for name, character in characters.items():
        character.word_count = count_words(character)
        character.emotionality = emotionality(character)


    return characters


musicals = {"Heathers": Musical("Heathers", "https://genius.com/albums/Heathers-the-musical-ensemble/Heathers-the-musical-world-premiere-cast-recording"), "Hamilton": Musical("Hamilton", "https://genius.com/albums/Lin-manuel-miranda/Hamilton-an-american-musical-original-broadway-cast-recording")}