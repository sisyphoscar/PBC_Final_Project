import pandas as pd

column = ["影城", "廳型", "全票", "優待","早場", "愛心/敬老", "午夜優惠", "會員"]
price = [
    ["西門絕色", "2D", "270", "240", "200", "135", "200", "210"],
    ["西門絕色", "3D", "330", "300", "260", "165", "260", "270"]
    ]

result = pd.DataFrame(price, columns = column)
result.to_csv("喜滿客絕色票價.csv")
print("finished")