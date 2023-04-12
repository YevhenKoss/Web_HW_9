import json

import requests
from bs4 import BeautifulSoup

base_url = "https://quotes.toscrape.com"


def get_urls(url: str = "", all_pages=None) -> list[str]:
    all_pages = all_pages if all_pages else []
    response = requests.get(base_url + url)
    soup = BeautifulSoup(response.text, "lxml")
    pagination = soup.find("ul", class_="pager").find("li", class_="next")
    if pagination:
        link = pagination.find("a").get("href")
        all_pages.append(base_url + link)
        get_urls(link, all_pages)
    else:
        all_pages.insert(0, base_url)
    return all_pages


def spider(urls):
    quotes = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        content = soup.find_all("div", class_="quote")
        for item in content:
            tags = item.find("div", class_="tags").find("meta", class_="keywords").get("content")
            tags = tags.split(",")
            author = item.find("small", class_="author").text
            quote = item.find("span", class_="text").text[1:-2]
            quotes.append({"tags": tags, "author": author, "quote": quote})
    return quotes


if __name__ == "__main__":
    urls = get_urls()
    data = spider(urls)
    with open('DB/quotes.json', 'w', encoding='utf-8') as fd:
        json.dump(data, fd, ensure_ascii=False)
