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


# 獲得 時刻表 URL
def getTimePage(moviepage):
    soup = getHtml(moviepage)  # 電影資訊page
    block = soup.find("div", "movie_tab")
    url_set = block.find_all(("a", "gabtn"))
    result = url_set[3].get("href")  # 時刻表
    return result

# # 主頁
# # for moviepage in url_set:
# #     timePage = getTimePage(moviepage)
# s = getTimePage(url_set[0])
# soup2 = getHtml(s)




url = "https://movies.yahoo.com.tw/movie_intheaters.html"
soup = getHtml(url)
url_set = getMoviepages(soup)
url = url_set[0]
soup = getHtml(url)
s = soup.find("div", "level_name").get_text(strip = True)
print(s)