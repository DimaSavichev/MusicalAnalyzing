import unittest
from musicals import musicals, analyze
import scrapping


class TestScrappingCase(unittest.TestCase):

    def test_scrap_songs(self):
        url = musicals['Hamilton'].url
        songs = scrapping.scrapSongs(url)
        assert len(songs) == 46

    def test_scrap_lyrics(self):
        url = "https://genius.com/Lin-manuel-miranda-and-phillipa-soo-best-of-wives-and-best-of-women-lyrics"
        lyrics = scrapping.scrapLyrics(url)
        with open('test_song', 'r', encoding='utf-8') as song:
            local_lyrics = song.read()

        assert lyrics.strip() == local_lyrics.strip()


class TestAnalyzingCase(unittest.TestCase):
    def setUp(self):
        with open('test_song', 'r', encoding='utf-8') as song:
            lyrics = song.read()

        self.characters = analyze(lyrics)
        assert 'ELIZA'

    def tearDown(self):
        self.characters = {}

    def test_character(self):
        assert 'ELIZA' in self.characters.keys()

    def test_word_count(self):
        assert self.characters['HAMILTON'].word_count == 38


if __name__ == '__main__':
    unittest.main()