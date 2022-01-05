import json
import pymongo

"""
in mongosh: db.json_table.find({text:{$regex:'смарт',$options:'i'}})
"""

# json_file_name = '/home/tolic/gitrepo/learn_and_try/stuff/site_parser/articles.json'
# json_file_name = '/home/tolic/gitrepo/github/my_python_projects/learn_and_try/' \
#                  'stuff/site_parser/done/articles_from_hitech.json'

json_file_name = '/home/tolic/gitrepo/github/my_python_projects/' \
                 'learn_and_try/stuff/site_parser/articles.json'

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['json_db']
json_table = db['json_table']
json_table.drop()

with open(json_file_name, 'r') as json_file:
    json_arr = json.load(json_file)
    # pprint(json_arr)
    json_table.insert_many(json_arr)
