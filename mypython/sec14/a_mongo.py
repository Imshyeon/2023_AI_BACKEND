from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db=client['mydb']
# print(db.list_collection_names())
collection = db['Score']
print(collection.name)
print(collection.find_one())    #collection.find_one().get('name') => aaa
print(type(collection.find_one()))

# db = MongoClient().aggregation_example
# result = db.things.insert_many(
#     [
#         {"x": 1, "tags": ["dog", "cat"]},
#         {"x": 2, "tags": ["cat"]},
#         {"x": 2, "tags": ["mouse", "cat", "dog"]},
#         {"x": 3, "tags": []},
#     ]
# )