from bs4 import BeautifulSoup
import requests


def scrapSongs(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')


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
