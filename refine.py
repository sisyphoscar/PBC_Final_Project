import requests
from bs4 import BeautifulSoup
import pandas as pd

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
    fin = fin.reset_index(drop=True)
    fin.to_csv("電影總覽.csv")
    print('finish')
    return fin

print(getTimeInfo())