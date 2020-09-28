from peewee import *
import datetime

db = PostgresqlDatabase('Bookmarks', user='lexleach', password='', host='localhost', port=5432)

db.connect()

