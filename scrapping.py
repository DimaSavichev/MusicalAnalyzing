from bs4 import BeautifulSoup
import requests
from musicals import Song, musicals


def scrapSongs(url):
    html = requests.get(url).content
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    song_tags = soup.find_all("div", {"class": "chart_row"})
    soup = BeautifulSoup('\n'.join(list(map(str, song_tags))), 'lxml')

    for x in soup.find_all("span"):
        x.extract()
    song_tags = soup.find_all("a")
    songs = []
    for tag in song_tags:
        songs.append(Song(tag.get_text(), tag['href']))

    return songs


def scrapLyrics(url):
    while True:  # рандомно возвращает 1 из двух типов кодов. в одном все плохо. Матожидание нужного кода: 2
        try:
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'lxml')
            body = soup.find_all("div", {"class": "song_body-lyrics"})[0]
            break
        except IndexError:
            pass

    body = body.get_text()
    body = body.replace("More on Genius", "")
    # print(body)

    return body
