from bs4 import BeautifulSoup
import requests
import pandas as pd

# Yahoo 電影時刻表

# 獲得 HTML
def getHtml(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    return soup


def getMoviepages(soup):
    # 單個頁面連接到的所有電影資訊頁面
    url_block = soup.find_all("div", "release_movie_name")
    result = []
    for movie in url_block:
        result.append(movie.find("a", "gabtn").get("href"))
    return result


url = "https://movies.yahoo.com.tw/movie_intheaters.html"
soup = getHtml(url)
moviePages = getMoviepages(soup)

# 迴圈 頁面：電影資訊 ->  時刻表
url = moviePages[0]
soup = getHtml(url)
block = soup.find("div", "movie_tab")
s = block.find_all(("a", "gabtn"))
url = s[3].get("href")