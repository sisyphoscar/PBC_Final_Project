import json
import requests
import pandas as pd
import datetime

# 票房

# 計算日期
def getday(y,m,d, delta):
    today = datetime.datetime(y,m,d)
    result_date = today + datetime.timedelta(days = delta)
    return result_date

today = datetime.date.today()
start = getday(today.year, today.month, today.day, - (today.weekday() + 7))  #上週一
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
column = ["電影", "票房", "金額"]
boxOffice = []
for movie in movie_info:
    boxOffice.append([movie["name"], movie["totalTickets"], movie["totalAmounts"]])

# Output
result = pd.DataFrame(boxOffice, columns = column)
result.to_csv("票房資訊.csv")

print("finished")