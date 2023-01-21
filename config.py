import pymongo
import certifi


connection_str = "mongodb+srv://jtbarn2:jtbarn2@cluster0.nhcjkoy.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_str, tlsCAFile=certifi.where() )
db = client.get_database("OnlineStore")