from builtins import filter
from datetime import datetime
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
print('client:', client)

print('client.list_database_names():', client.list_database_names())

DB_PROJ = "proj"

db = client[DB_PROJ]

print('db:', db)
print('db.list_collection_names():', db.list_collection_names())

db1 = client['local']
print('db1:', db1)
print('db1.list_collection_names():', db1.list_collection_names())

cur1 = db1['startup_log'].find({})
print('cur1:', cur1)
print(15*'-')
for row in cur1:
    print(row)
print(15*'-')

# res = db["demo"].insert_one({ "foo": "bar "})
# print(res, res.inserted_id)
#
# COLLECTION_USERS = "users"
#
#
# def user_factory(username: str, age: int) -> dict:
#     """
#     :param username:
#     :param age:
#     :return:
#     """
#     return {
#         "age": age,
#         "username": username,
#         "created_at": datetime.now(),
#     }
#
#
# users_collection = db[COLLECTION_USERS]
#
# admin_user = user_factory("admin", 20)
# admin_user["is_admin"] = True
#
# res = users_collection.insert_one(admin_user)
# print(res, res.inserted_id)
#
#
# users = [user_factory("sam", 22), user_factory("john", 24)]
# results = users_collection.insert_many(users)
# print(results, results.inserted_ids)
#
# user_admin = users_collection.find_one({"username": "admin"})
# print(user_admin, user_admin["_id"], user_admin["username"])
#
# res = db["demo"].insert_one({
#   "user_admin" : user_admin["_id"],
# })
#
# print(res, res.inserted_id)
#
#
# # queries
#
# """js
#
# db.getCollection('users').aggregate([
#     {
#         $group: {
#             _id: {
#                 "username": "$username",
#             },
#             count: { $sum: 1 },
#             names: { $push: { firstName: "$firstName", lastName: "$lastName"} },
#         },
#     },
#     {
#         $match: {
#             count: { $gte: 2 },
#         },
#     },
# ])
#
# db.getCollection('demo').aggregate([
#     {
#         $lookup: {
#            from: "users",
#            localField: "user_admin",
#            foreignField: "_id",
#            as: "users_admins",
#         },
#     }
# ])
# """