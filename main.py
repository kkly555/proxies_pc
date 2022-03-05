import csv
import re
import requests
import time
from bs4 import BeautifulSoup
import numpy


def main():
    base_url = "https://www.kuaidaili.com/free/inha/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62",
        "Cookie": "channelid=0; sid=1646181252771994; _gcl_au=1.1.392979150.1646182866; _ga=GA1.2.352508075.1646182866; _gid=GA1.2.749179900.1646443746; _gat=1; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1646182866,1646443746,1646447614; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1646447614"
    }
    with open("data.csv", 'w', encoding='UTF-8', newline="") as D:
        csv_head = ['IP', 'NMD', 'Position']
        csv_write = csv.DictWriter(D, fieldnames=csv_head)
        csv_write.writeheader()
        for i in range(4490):
            i = i + 1
            url = base_url + str(i) + "/"
            ask_url(url, headers, csv_write)
            time.sleep(10)


def ask_url(url, headers, csv_write):  # 发送请求，获得html
    html = requests.get(url=url, headers=headers)
    get_result(html, csv_write)


def get_result(html, csv_write):  # 爬取html数据
    soup = BeautifulSoup(html.content, "html.parser")
    # print(soup)
    find_rule1 = re.compile(r'<td data-title="IP">(.*?)</td>')
    find_rule2 = re.compile(r'<td data-title="匿名度">(.*?)</td>')
    find_rule3 = re.compile(r'<td data-title="位置">(.*?)</td>')
    item = soup.find_all("table")
    item = str(item)
    IP = re.findall(find_rule1, item)  # IP
    print(IP)
    NMD = re.findall(find_rule2, item)  # 匿名度
    Position = re.findall(find_rule3, item)  # ip地址
    for i in range(len(IP)):
        save_csv(IP[i], NMD[i], Position[i], csv_write)


def save_csv(IP, NMD, Position, csv_write):
    csv_write.writerow(
        {
            "IP": IP,
            "NMD": NMD,
            "Position": Position
        }
    )


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
