from bs4 import BeautifulSoup
import requests
from musicals import Song

def scrapSongs(url):
    # html = requests.get(url).text
    # soup = BeautifulSoup(html, 'lxml')
    return [Song("Beautiful", "https://genius.com/Heathers-the-musical-ensemble-beautiful-lyrics"),
            Song("Candy Store", "https://genius.com/Heathers-the-musical-ensemble-candy-store-lyrics")]


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
