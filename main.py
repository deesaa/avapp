import mysql.connector as sql
import requests
import pymongo as mongo
from GrabbersPool import GrabbersPool
from ItemsExtractor import ItemsExtractor
from lxml import etree

GrabConfig = {
    "SSD_cheap_600rub_allregions" : {
        "enable" : True,
        "url" : "https://www.avito.ru/all/tovary_dlya_kompyutera/komplektuyuschie/zhestkie_diski-ASgBAgICAkTGB~pm7gmwZw?cd=1&d=1&f=ASgBAgECAkTGB~pm7gmwZwFFxpoME3siZnJvbSI6MCwidG8iOjYwMH0&q=ssd&s=104",
        "title_exclude":{
            "Переходник", "Салазки", "Винт", "Болты", "Адаптер", "Корпус", "Комплект", "Крепления", "Шлейф"
        }
    }
}

grabbers_pool = GrabbersPool(GrabConfig)
grabber = grabbers_pool.get_grabber("SSD_cheap_600rub_allregions")
itemExtractor = ItemsExtractor()
grab = grabber.create_grab()
grab.save()
item_heads = itemExtractor.extract(grab)
item_heads_included = [x for x in item_heads if not grabber.is_exclude_item_head(x)]
items_raw = [grabber.create_item_from_head(x) for x in item_heads_included[:2]]
[x.save() for x in items_raw[:2]]

items = [itemExtractor.extract_raw_item(x) for x in items_raw]
itemExtractor.extract(items[0])


#print('\n'.join([str(x.price) for x in itemHeads2]))


# grab = ssdGrabber.create_grab()
# grab.save()


# DB_NAME = "TestDb1"


# def IsDbExists(dbname, connection):
#     return switchdict[type(connection)](dbname, connection)

# def MySqlDbExists(dbname, connection):
#     cursor = connection.cursor()
#     sqlcommand = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = %s"
#     cursor.execute(sqlcommand, (dbname,))
#     result = cursor.fetchall()
#     return result != 0

# def MongoDbExists(dbname, connection : mongo.MongoClient):
#     names = connection.list_database_names()
#     exists = dbname in names 
#     return exists

# switchdict = {sql.CMySQLConnection : MySqlDbExists, mongo.MongoClient : MongoDbExists}



# mydb = sql.connect(host="127.0.0.1", password="")
# print(IsDbExists(DB_NAME, mydb))

# client = mongo.MongoClient("mongodb://localhost:27017")
# mydb = client[DB_NAME]
# collection = mydb["users"]
# collection.ins
# print(IsDbExists(DB_NAME, client))



# cursor.execute("CREATE DATABASE TestDb1")

# print(mydb)

# mydb.close()

# import pymongo as mongo

# client = mongo.MongoClient("mongodb://localhost:27017")
# mydb = client["mongotest1"]

# print(mydb)

