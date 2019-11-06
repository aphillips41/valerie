from pymongo import MongoClient

#my_mongo_1 is the name of the mongo container
client = MongoClient('valerie_mongo', 27017)

#connect to testing database
db = client['val_db']

val_collection = db.valerie

val_data = {
	'name': 'pi',
    'value': 3.14159 
}

val_collection.insert_one(val_data)
