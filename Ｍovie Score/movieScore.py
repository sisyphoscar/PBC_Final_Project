from bs4 import BeautifulSoup
import requests
import pandas as pd

# Yahoo 電影期待度

# 獲得 HTML
def getHtml(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def getScore(block):
    result = []
    for movie in block:
        # 期待度
        if movie.find("span") == None or movie.find("span").get_text() == "0":
            score = "No Record"
        else:
            score = movie.find("span").get_text()

        # 片名
        name = movie.find("a").get_text(strip = True)

        result.append([name, score])
    return result

# def getDataFrame(result):

# main
if __name__ == "__main__":
    result = pd.DataFrame()
    for page in range(1,11):
        url = f"https://movies.yahoo.com.tw/movie_intheaters.html?page={page}"
        soup = getHtml(url)
        block = soup.find_all("div", "release_movie_name")
        score = getScore(block)
        single_result = pd.DataFrame(score, columns = ["名稱", "期待度"])
        result = pd.concat([result, single_result], axis = 0)
    result = result.reset_index(drop = True)
    result.to_csv("MovieScore.csv")
    print("finished")