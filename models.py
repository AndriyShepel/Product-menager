from peewee import *


db = SqliteDatabase("db.sqlite")

class Basemodel(Model):
    class Meta:
        database = db

class Product(Basemodel):
    name = TextField()
    price = FloatField()
    category = TextField()

def _init_db():
    db.connect()
    db.create_tables([Product])