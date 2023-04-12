from mongoengine import *


class Author(Document):
    fullname = StringField(max_length=150, required=True)
    born_date = StringField()
    born_location = StringField(max_length=200)
    description = StringField()


class Quote(Document):
    tags = ListField(StringField(max_length=50))
    author = ReferenceField(Author)
    quote = StringField()
