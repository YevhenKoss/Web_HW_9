import json

import requests
from bs4 import BeautifulSoup

from quotes_data import get_urls, base_url


def get_author_urls(urls):
    author_urls = set()
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        content = soup.find_all("div", class_="quote")
        for item in content:
            author = item.find("a").get("href")
            author_urls.add(base_url + author)
    return author_urls


def spider(author_urls):
    authors = []
    for url in author_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        author_details = soup.find("div", class_="author-details")
        fullname = author_details.find("h3", class_="author-title").text
        fullname = fullname.strip()
        born_date = author_details.find("span", class_="author-born-date").text
        born_location = author_details.find("span", class_="author-born-location").text
        born_location = born_location.strip()
        description = author_details.find("div", class_="author-description").text
        description = description.strip()
        authors.append(
            {"fullname": fullname, "born_date": born_date, "born_location": born_location, "description": description})
    return authors


if __name__ == '__main__':
    urls = get_urls()
    author_urls = get_author_urls(urls)

    data = spider(author_urls)
    with open('DB/authors.json', 'w', encoding='utf-8') as fd:
        json.dump(data, fd, ensure_ascii=False)
