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

def find_Bookmark():
    try:
        find = input('What is the name of the Bookmark you wish to find? ԅ(≖‿≖ԅ): \n')
        find_bookmark = Bookmark.select().where(Bookmark.name == find)

        for bookmark in find_bookmark:
            print('==========༼ つ ◕_◕ ༽つ=========')
            print('=======You Has Bookmark========')
            print(f'Name: {bookmark.name} \n Link: {bookmark.link} \n Date Added: {bookmark.date_added}')
            print('==============================')
    except:
        print('No Bookmark found with that name.')
        Bookmark_List()

    Bookmark_List()

def update_Bookmark():
    find = input('What is the name of the Bookmark you wish to Update?: \n')
    find_bookmark = Bookmark.select().where(Bookmark.name == find).get()

    update = input('Which field do you wish to update? name or url: \n')
    if update == 'name':
        new_name = input(f'What is the new name you wish to give {find}? (◔_◔): \n')
        find_bookmark.name = new_name
        find_bookmark.save()
        print('====ヽ(｀Д´)⊃━☆ﾟ. * ･ ｡ﾟ,====')
        print(f'Name: {find_bookmark.name} \n Link: {find_bookmark.link} \n Date Added: {find_bookmark.date_added}')
        print('==========(☝ ՞ਊ ՞)☝==========')
        print(f'{find} has successfully been updated to {new_name}! (•_•) ( •_•)>⌐■-■ (⌐■_■)')
        Bookmark_List()
    
    elif update == 'url' or update == 'URL':
        new_url = input(f'What is the new URL you wish to give {find}? (◔_◔): \n')
        find_bookmark.link = new_url
        find_bookmark.save()
        print('====ヽ(｀Д´)⊃━☆ﾟ. * ･ ｡ﾟ,====')
        print(f'Name: {find_bookmark.name} \n Link: {find_bookmark.link} \n Date Added: {find_bookmark.date_added}')
        print('==========(☝ ՞ਊ ՞)☝===========')
        print(f"{find}'s URL has successfully been updated to {new_url}! (•_•) ( •_•)>⌐■-■ (⌐■_■)")
        Bookmark_List()
    else:
        Bookmark_List()

Bookmark_List()