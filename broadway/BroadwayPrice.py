from bs4 import BeautifulSoup
import requests
import pandas as pd

# Broadway 影城

# 獲得 HTML
def getHtml(url):
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def getInfoBlock(soup):
    result = soup.find("table", "table table-striped")
    return result


def getTicketColumn(block):
    # 票種資訊
    ticketType = block.find_all("th")
    result = []
    for info in ticketType:
        result.append(info.get_text())
    return result



def getTicketInfo(block):
    temp_result = []
    ticketInfo = block.find_all("td")
    for info in ticketInfo:
        temp_result.append(info.get_text())

    # 再整理
    result = [0] * 2
    result[0] = temp_result[0:6]
    result[1] = temp_result[6:12]
    # print(result)
    # print(temp_result)
    return result

if __name__ == "__main__":
    url = "https://broadway-cineplex.azurewebsites.net/tickeyPage.aspx"
    soup = getHtml(url)
    block = getInfoBlock(soup)
    columns =  getTicketColumn(block)
    ticketInfo = getTicketInfo(block)

    result = pd.DataFrame(ticketInfo, columns = columns)
    result.to_csv("BroadwayPrice.csv")
    print("finished")