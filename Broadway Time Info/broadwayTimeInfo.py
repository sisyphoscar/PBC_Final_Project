from bs4 import BeautifulSoup
import requests
import pandas as pd

# Broadway 影城

# 獲得 HTML
def getHtml(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


# 抓取資訊
def getName(soup):
    # 電影名稱
    names = []
    movies = soup.find_all("div", "col-sm-8 wthree-news-info")  # 內容版面
    for movie in movies:
        names.append(movie.find("h3").get_text())
    return names

def getTime(soup):
    # 電影場次
    result = []
    movies = soup.find_all("div", "col-sm-8 wthree-news-info")
    for movie in movies:
        single_movie = []

        # 電影場次
        shows = movie.find_all("span", "badge badge-danger")
        for show in shows:
            if show.get_text() != "":
                single_movie.append(show.get_text())

        # 加入一組電影場次
        result.append(single_movie)
    return result

def getImg(soup):
    # 電影封面
    imgs = soup.find_all("img")
    result = []
    for img in imgs[1:]:
        imgId = img["src"]
        img = "https://broadway-cineplex.azurewebsites.net/" + str(imgId)
        result.append(img)
    return result



# Output
def list2sheet2(names, times, imgs):
    # 單個名稱 - 單個時刻
    movie_info = []
    for i in range(len(names)):
        for j in range(1, len(times[i])):
            movie_info.append([names[i], times[i][j], imgs[i]])

    result = pd.DataFrame(movie_info, columns = ["名稱", "場次", "封面"])
    return result

def getDataFrame(names, times, imgs):
    # 單個名稱 - 多個時刻
    movie_info = []
    for i in range(len(names)):
        name = names[i]
        time_set = []
        for j in range(1, len(times[i])):
            time_set.append(times[i][j])
        img = imgs[i]
        movie_info.append(["百老匯", name, time_set, img])
    result = pd.DataFrame(movie_info, columns = ["影城", "電影", "場次", "封面"])
    return result

# main
if __name__ == "__main__":
    url = "https://broadway-cineplex.azurewebsites.net/moviePage.aspx"
    soup = getHtml(url)
    names = getName(soup)
    times = getTime(soup)
    imgs = getImg(soup)
    result = getDataFrame(names, times, imgs)
    result.to_csv("broadway.csv")
    print("finished")