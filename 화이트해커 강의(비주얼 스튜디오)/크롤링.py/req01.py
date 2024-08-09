import requests
from bs4 import BeautifulSoup


url = "https://n.news.naver.com/article/082/0001226860"


req =requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
print(soup)