from peewee import *
import datetime

db = PostgresqlDatabase('Bookmarks', user='lexleach', password='', host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Bookmark(BaseModel):
    name = CharField()
    link = CharField()
    date_added = DateField()

db.drop_tables([Bookmark])
db.create_tables([Bookmark])

google = Bookmark(name='Google', link='https://www.google.com', date_added=datetime.datetime.now()).save()
reddit = Bookmark(name='Reddit', link='https://www.reddit.com', date_added=datetime.datetime.now()).save()
steam = Bookmark(name='Steam', link='https://store.steampowered.com/', date_added=datetime.datetime.now()).save()
humble_bundle = Bookmark(name='Humble Bundle', link='https://www.humblebundle.com/', date_added=datetime.datetime.now()).save()

