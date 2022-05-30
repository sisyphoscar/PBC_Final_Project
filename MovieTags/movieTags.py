from bs4 import BeautifulSoup
import requests
import pandas as pd

# Yahoo 電影分類

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


# 得到資訊list
def getMovieTags(url_set):
    result = []
    for i in range(len(url_set)):
        url = url_set[i]
        movie = getHtml(url)
        movieTags = movie.find_all("div", "level_name")
        name = movie.find("h1").get_text(strip = True)
        for tag in range(len(movieTags)):
            movieTags[tag] = movieTags[tag].get_text(strip = True)
        movieTags.remove("期待度")
        movieTags.remove("滿意度")
        result.append([name, movieTags])
    return result


def getMovieClass():
    result = pd.DataFrame()
    page = 1
    while True:
        url = f"https://movies.yahoo.com.tw/movie_intheaters.html?page={page}"
        soup = getHtml(url)
        url_set = getMoviepages(soup)
        movie_tag = getMovieTags(url_set)
        single_result = pd.DataFrame(movie_tag, columns = ["電影","分類"])
        result = pd.concat([result, single_result], axis = 0).reset_index(drop = True)
        if soup.find("li", "nexttxt disabled") == None:
            page += 1
        else:
            break
        print(f"page:{page}")
    print("finished")
    return result