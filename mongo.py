
import pymongo

import os


MONGODB_URI = os.getenv("MONGO_URI")

DBS_NAME = "mytestdb"

COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):

    try:

        conn = pymongo.MongoClient(url)

        print("Mongo is connected!")

        return conn

    except pymongo.errors.ConnectionFailure as e:

        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)


coll = conn[DBS_NAME][COLLECTION_NAME]

#new_doc={'first': 'douglas', 'last': ' adams', 'dob': '11/01/1978','hair_color': 'not much','occupation': 'writer','nationality': 'english'}
# coll.insert_one(new_doc)

#documents = coll.find()

# print all record in DB
# for doc in documents:

#  print(doc)

# insert a new record
#  new_doc={'first': 'douglas', 'last': ' adams', 'dob': '11/01/1978','hair_color': 'not much','occupation': 'writer','nationality': 'english'}

# coll.insert(new_doc)
# documents=coll.find()

# insert a few  new records
#new_doc1=[{'first': 'douglas', 'last': ' adams', 'dob': '11/01/1978','hair_color': 'not much','occupation': 'writer','nationality': 'english'},{'first': 'terry', 'last': ' prat', 'dob': '11/01/1978','hair_color': 'greyh','occupation': 'writer','nationality': 'english'}]
# coll.insert(new_doc1)
# documents=coll.find()

# to find specific data
# documents=coll.find({'first': 'douglas'})


# to remove specific data
# documents=coll.remove({'first': 'douglas'})
# documents=coll.find()
# for doc in documents:
# print(doc)


# to update specific data
coll.update_one({'nationality': 'american'}, {
                '$set': {'hair_color': 'maroon'}})
documents = coll.find({'nationality': 'american'})
for doc in documents:
    print(doc)
