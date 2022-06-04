import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import json
# pip install lxml

def check_req_url(url): 
    resp = requests.get(url) 
    if resp.status_code != 200:  
        print('Invalid url:', resp.url) 
        return "fail" 
    else:
        return resp.text
def get_week_new_movies(webpage): #抓取電影資訊
    soup = BeautifulSoup(webpage, 'html.parser') #網頁解析
    movies = [] #域設電影資訊存這裡 
    rows = soup.find_all('div', 'release_info')
    foto_items = soup.find_all('div', 'release_foto')
    #print(rows)
    pt = []
    for foto in foto_items:
        poster = foto.find('img').get('src')
        pt.append(poster) 
    for i in range(len(rows)):
        data_movie = dict() #存成{"key":"value"}格式
        #電影名稱
        data_movie['電影名稱'] = rows[i].find('div', 'release_movie_name').a.text.strip()
        #場次
        tt = rows[i].find('ul', 'theater_time').text.strip().split('\n')
        newtt = []
        for j in tt:
            if j != '':
                newtt.append(j.strip()) 
        data_movie['電影場次'] = newtt
        #評分
        data_movie['電影評分'] = rows[i].find('div', 'leveltext').span.text.strip()
        #預告片
        data_movie['預告片'] = rows[i].find('a','btn_s_vedio').get('href')
        data_movie['封面'] = pt[i]
        movies.append(data_movie) 
    return movies
#影城網址
yahoo_movie_url = ['https://movies.yahoo.com.tw/theater_result.html/id=30',
                  'https://movies.yahoo.com.tw/theater_result.html/id=29',
                  'https://movies.yahoo.com.tw/theater_result.html/id=37',
                  'https://movies.yahoo.com.tw/theater_result.html/id=112',
                  'https://movies.yahoo.com.tw/theater_result.html/id=53',
                  'https://movies.yahoo.com.tw/theater_result.html/id=154',
                  'https://movies.yahoo.com.tw/theater_result.html/id=168?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAH5DxlFszWktpGryqJGte-zdzKKEyA50uN9DfYwcvV9AyNNqF1_on5bRtkSreaxF8cdfilYeDWmwyzC8EJ3C4RR-CkpC3LBUS_gB-6xeibaxS2-feCTY0HuBqVPLyn8rEn9QwYmnGhMW0e6VYQoXFnOA5i2VJijaT0qHULc4Ty-e',
                  'https://movies.yahoo.com.tw/theater_result.html/id=45',
                  'https://movies.yahoo.com.tw/theater_result.html/id=128',
                  'https://movies.yahoo.com.tw/theater_result.html/id=42',
                  'https://movies.yahoo.com.tw/theater_result.html/id=214',
                  'https://movies.yahoo.com.tw/theater_result.html/id=220',
                  'https://movies.yahoo.com.tw/theater_result.html/id=118',
                  'https://movies.yahoo.com.tw/theater_result.html/id=254',
                  'https://movies.yahoo.com.tw/theater_result.html/id=261',
                  'https://movies.yahoo.com.tw/theater_result.html/id=193',
                  'https://movies.yahoo.com.tw/theater_result.html/id=185',
                  'https://movies.yahoo.com.tw/theater_result.html/id=251',
                  'https://movies.yahoo.com.tw/theater_result.html/id=31',
                  'https://movies.yahoo.com.tw/theater_result.html/id=152',
                  'https://movies.yahoo.com.tw/theater_result.html/id=32',
                  'https://movies.yahoo.com.tw/theater_result.html/id=35',
                  'https://movies.yahoo.com.tw/theater_result.html/id=36',
                  'https://movies.yahoo.com.tw/theater_result.html/id=41',
                  'https://movies.yahoo.com.tw/theater_result.html/id=38',
                  'https://movies.yahoo.com.tw/theater_result.html/id=52',
                  'https://movies.yahoo.com.tw/theater_result.html/id=144',
                  'https://movies.yahoo.com.tw/theater_result.html/id=50',
                  'https://movies.yahoo.com.tw/theater_result.html/id=191',
                  'https://movies.yahoo.com.tw/theater_result.html/id=237',#30
                  'https://movies.yahoo.com.tw/theater_result.html/id=259',
                  'https://movies.yahoo.com.tw/theater_result.html/id=56',
                  'https://movies.yahoo.com.tw/theater_result.html/id=57',
                  'https://movies.yahoo.com.tw/theater_result.html/id=126',
                  'https://movies.yahoo.com.tw/theater_result.html/id=186',
                  'https://movies.yahoo.com.tw/theater_result.html/id=247'
                  ]
theater = ['欣欣秀泰','國賓（長春）','今日秀泰',' 國賓大戲院(西門)','東南亞秀泰','板橋秀泰','誠品電影院','信義威秀',
           '板橋大遠百威秀','喜滿客絕色影城','樹林秀泰','土城秀泰','京站威秀','松仁威秀','中和環球威秀','林口威秀',
           '新莊國賓','淡水國賓','台北光點','華山光點','台北美麗華大直影城','台北新光影城','台北in89豪華數位影',
           '台北真善美劇院','台北樂聲影城','百老匯數位影城','台北新民生戲院','哈拉影城','美麗新大直皇家影城','美麗新淡海',#30
           '美麗新宏匯影城','鴻金寶麻吉影城','三重天台戲院','梅花數位影院','喜樂時代影城南港店','喜樂時代影城永和店'
           ]
site = ['台北市中山區林森北路247號4樓','台北市長春路176號', '台北市萬華區成都路88號','台北市西門町峨眉街52號4樓','台北市中正區羅斯福路四段 136巷3號',
        '新北市板橋區縣民大道2段3號','台北市信義區菸廠路80號B2','台北市信義區松壽路18號','新北市板橋區新站路28號10樓','台北市萬華區漢中街52號10、11樓',
        '238新北市樹林區樹新路40-6號','新北市土城區學府路二段210號1樓','台北市大同區市民大道一段209號5樓','台北市信義區松仁路58號10樓','新北市中和區中山路三段122號4樓',
        '新北市林口區文化三路一段356號3樓','新北市新莊區五工路66號3F','新北市淡水區中正路一段2號(禮萊廣場)','台北市中山區中山北路2段18號','臺北市100中正區八德路一段1號',
        '台北市中山區敬業三路22號6樓','台北市萬華區西寧南路36號4樓','台北市萬華區武昌街二段89號','台北市萬華區漢中街116號7樓','台北市萬華區武昌街二段85號',
        '台北市文山區羅斯福路四段200號4樓','台北市松山區民生東路五段190號3樓','台北市內湖區康寧路三段72號6樓','台北市中山區北安路780號B2','新北市淡水區義山路2段303號2樓',#30
        '新北市新莊區新北大道4段3號8樓','新北市新莊區民安路188巷5號','新北市三重區重新路二段78號4F','台北市和平東路3段63號2F','台北市南港區忠孝東路7段299號',
        '新北市永和區中山路一段238號4F'
        ]
price = [290,320,400,280,280,290,290,340,330,270,290,290,340,370,310,370,300,290,260,270,
         330,280,300,270,280,280,260,290,650,290,300,260,270,270,310,300
         ]


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

#Output

# 票房
# 計算日期
def getday(y,m,d, delta):
    today = datetime.datetime(y,m,d)
    result_date = today + datetime.timedelta(days = delta)
    return result_date

def getBoxOffice():
    today = datetime.date.today()
    start = getday(today.year, today.month, today.day, -(today.weekday() + 14))
    end = getday(start.year, start.month, start.day, 6)

    # 轉成 URL 所需的 string
    start = f"{start.year}/{start.month}/{start.day}"
    end = f"{end.year}/{end.month}/{end.day}"

    # 進入json檔網址
    url = f"https://boxoffice.tfi.org.tw/api/export?start={start}&end={end}"
    response = requests.get(url)

    # 轉成json
    data = json.loads(response.text)

    # 轉成 DataFrame
    movie_info = data["list"]
    column = ["電影名稱", "票房", "金額"]
    boxOffice = []
    for movie in movie_info:
        boxOffice.append([movie["name"], movie["totalTickets"], movie["totalAmounts"]])

    # Output
    result = pd.DataFrame(boxOffice, columns = column)
    return result


def getMovieClass():
    result = pd.DataFrame()
    page = 1
    while True:
        url = f"https://movies.yahoo.com.tw/movie_intheaters.html?page={page}"
        soup = getHtml(url)
        url_set = getMoviepages(soup)
        movie_tag = getMovieTags(url_set)
        single_result = pd.DataFrame(movie_tag, columns = ["電影名稱","分類"])
        result = pd.concat([result, single_result], axis = 0).reset_index(drop = True)
        if page == 4:
            print('66%loading')
        if soup.find("li", "nexttxt disabled") == None:
            page += 1
        else:
            break
        print(f"page:{page}")
    return result

def getTimeInfo():
    fin = pd.DataFrame()
    for i in range(len(yahoo_movie_url)):
        webpage = check_req_url(yahoo_movie_url[i])    
        #if webpage:
        movies = get_week_new_movies(webpage)
        movies = pd.DataFrame(movies)
        movies['影城'] = theater[i]
        movies['地址'] = site[i]
        movies['票價'] = price[i]
        fin = pd.concat([fin,movies],axis=0)
    fin = fin.explode('電影場次')
    # fin.to_csv("電影總覽.csv")
    return fin

if __name__ == "__main__":
    try:
        print('loading...')
        table1 = getTimeInfo()
        print('33%loading...')
        table2 = getMovieClass()
        result = pd.merge(table1, table2, on = ["電影名稱"])
        table3 = getBoxOffice()
        result = pd.merge(result, table3, on = ["電影名稱"])
        result.to_csv("電影資訊.csv")
        print("finished")
    except Exception as e:
        print(e)