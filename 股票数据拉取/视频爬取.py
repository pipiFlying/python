import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

headers = {
    "User-Agent": "Mozilla/5.0",
    "authorization": "Basic cGM6MTU2ODE5MTMxMzc6d1BxVGJvUk58MXxSQ1N8MTc3MDM2MzE5NTAyNHxKT2ExMW9GbVFpOF84UWhQMGtId0EuMGZqZ1JwSUJ3ZVduMFhqYzlEWThSWGxGOXZEcldJVFVCNUkzM0daNXJ3eW1RSGNTZzc0SU42aFc2Mi45VHNfcFRTdGRYQ3BidXBVbGZOWEM4NmFKcWZEMEZWX1hOU09kbjRzdzNnUUk2N1JJa3J6aGR1eHV3UmlaZS5IbEc5WWNfRDE2RjJsU21kWUVKLmZMQ2plcnct",
    "x-yun-app-channel": "10000034",
    "x-yun-client-info": "||9|7.17.0|chrome|143.0.0.0|||windows 10||zh-CN|||dW5kZWZpbmVk||",
    "yun-encrypt-index": "20_5",
    "yun-encrypt-key": "045626d6d814a34e356bcdac10f7a8dd806c253a5e87dd9ec4693affcbe51a52092b3bf8d55f6bb12b95322ae9d0c71bb72e788f3c7de1feea66cbf9efa05f858ae37eab11318de39950105b59b684ac25b2d179c96f134b6bab759c3b685632ae02ce0bf2e98e55c0f8d844e4b3d889fd"
}

url = "https://yun.139.com/w/#/vplay?contentID=FmlXyg8USVi0JqPBpIFBN1Iw8s8hUEkUt&from=groupFile&contentSortType=0&sortDirection=1&groupID=1231470110798583823&path=root%3A%2FFp_yohan7Irt7v2EGkB9A_LGV6c44-zG7%2FFlXqBd1KVMboe03mCKARLwIMTwDzDlSK6%2FFtBEkVIP5O2cBLtdlG3hKqKJ4ZR8S-Shn&catalogID=FtBEkVIP5O2cBLtdlG3hKqKJ4ZR8S-Shn"

# 1. 请求页面
resp = requests.get(url, headers=headers, timeout=10)
resp.raise_for_status()

print(resp.text)

html_s = ''

# 2. 解析 HTML
soup = BeautifulSoup(resp.text, "html.parser")

# 3. 查找 video 标签
video = soup.find("video")

if not video:
    print("未找到 video 标签")
    exit()

video_url = video.get("src")
video_url = urljoin(url, video_url)

print("视频地址：", video_url)

# 4. 下载视频
video_data = requests.get(video_url, headers=headers, stream=True)

with open("video.mp4", "wb") as f:
    for chunk in video_data.iter_content(chunk_size=8192):
        f.write(chunk)

print("下载完成：video.mp4")
