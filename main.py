import mysql.connector as sql
import requests
import pymongo as mongo
from Executor import Executor
from ItemsListGrabber import DeniedIpException

try:
    Executor.DoGrab()
except DeniedIpException as e:
    print("DENIED IP: " + e.log_text)
    

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

