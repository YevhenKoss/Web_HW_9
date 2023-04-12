import json
from models import Author, Quote
import connect

authors_file = "authors.json"
quotes_file = "quotes.json"

with open(authors_file, "r", encoding="utf-8") as fh:
    authors = json.load(fh)

with open(quotes_file, "r", encoding="utf-8") as fh:
    quotes = json.load(fh)

if __name__ == '__main__':

    for author in authors:
        user = Author(fullname=author["fullname"], born_date=author["born_date"], born_location=author["born_location"],
                      description=author["description"])
        user.save()
        for quote in quotes:
            if quote["author"] == author["fullname"]:
                record = Quote(tags=quote["tags"], author=user, quote=quote["quote"])
                record.save()



