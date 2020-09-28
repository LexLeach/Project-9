from peewee import *
import datetime

db = PostgresqlDatabase('Bookmarks', user='lexleach', password='', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Bookmark(BaseModel):
    name = CharField()
    link = CharField()
    date_added = DateField()

db.connect()
db.drop_tables([Bookmark])
db.create_tables([Bookmark])

google = Bookmark(name='Google', link='https://www.google.com', date_added=datetime.datetime.now()).save()
reddit = Bookmark(name='Reddit', link='https://www.reddit.com', date_added=datetime.datetime.now()).save()
steam = Bookmark(name='Steam', link='https://store.steampowered.com/', date_added=datetime.datetime.now()).save()
humble_bundle = Bookmark(name='Humble Bundle', link='https://www.humblebundle.com/', date_added=datetime.datetime.now()).save()

def Bookmark_List():
    print('Please select an option: \n (L)ist Bookmarks \n (F)ind Bookmark \n (C)reate a Bookmark \n (U)pdate a Bookmark \n (E)xit App')

    choice = str(input('Enter a Choice: '))

    if choice == 'L' or choice == 'l':
        list_Bookmarks()
    elif choice == 'F' or choice == 'f':
        find_Bookmark()
    elif choice == 'C' or choice == 'c':
        create_Bookmark()
    elif choice == 'U' or choice == 'u':
        update_Bookmark()
    else:
        print('Goodbye! (◞థ౪థ)ᴖ')
        exit()

def list_Bookmarks():
    bookmarks = Bookmark.select()
    print('==========༼ つ ◕_◕ ༽つ=========')
    print('======You Has Bookmarks=======')
    for bookmark in bookmarks:
        print('===========================')
        print(f'Name: {bookmark.name} \n Link: {bookmark.link} \n Date Added {bookmark.date_added}')
        print('===========================')

    Bookmark_List()

Bookmark_List()