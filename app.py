#Imports ALL of peewee
from peewee import *
#imports date function
import datetime
#Database connection
db = PostgresqlDatabase('Bookmarks', user='lexleach', password='', host='localhost', port=5432)
#Database Base model
class BaseModel(Model):
    class Meta:
        database = db
#Database Schema
class Bookmark(BaseModel):
    name = CharField()
    link = CharField()
    date_added = DateField()
#starts connection to database
db.connect()
#Drops tables in Bookmark
db.drop_tables([Bookmark])
#Creates new tables in Bookmark
db.create_tables([Bookmark])
#Variable to add bookmarks
google = Bookmark(name='Google', link='https://www.google.com', date_added=datetime.datetime.now()).save()
reddit = Bookmark(name='Reddit', link='https://www.reddit.com', date_added=datetime.datetime.now()).save()
steam = Bookmark(name='Steam', link='https://store.steampowered.com/', date_added=datetime.datetime.now()).save()
humble_bundle = Bookmark(name='Humble Bundle', link='https://www.humblebundle.com/', date_added=datetime.datetime.now()).save()
#Function to list App options
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
#Function to list current bookmarks in the database
def list_Bookmarks():
    bookmarks = Bookmark.select()
    print('==========༼ つ ◕_◕ ༽つ=========')
    print('======You Has Bookmarks=======')
    for bookmark in bookmarks:
        print('===========================')
        print(f'Name: {bookmark.name} \n Link: {bookmark.link} \n Date Added {bookmark.date_added}')
        print('===========================')

    Bookmark_List()
#Function to find a bookmark by name
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
#Function to create a new bookmark
def create_Bookmark():
    new_name = input('What would you like to name the Bookmark?: \n' )

    new_link = input('Paste or type the URL to the new Bookmark: \n')

    add_bookmark = Bookmark(name=new_name, link=new_link, date_added=datetime.datetime.now()).save()

    find_bookmark = Bookmark.select().where(Bookmark.name == new_name)

    print('Bookmark successfully added!')

    for bookmark in find_bookmark:
        print('===========================')
        print(f'Name: {bookmark.name} \n Link: {bookmark.link} \n Date Added: {bookmark.date_added}')
        print('===========================')

    Bookmark_List()
#Function to update a bookmark current in the database
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
#Function call for Bookmark_List
Bookmark_List()