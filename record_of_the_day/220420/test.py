# import requests
# from bs4 import BeautifulSoup as bs

# url = 'https://github.com/khyunchoi/Rikey'
# response = requests.get(url)

# soup = bs(response.content, 'html.parser')

# print(soup)

from markdownify import markdownify

file = open("html2.txt", "r", encoding="utf-8").read()
html = markdownify(file, heading_style="ATX")

print(html)