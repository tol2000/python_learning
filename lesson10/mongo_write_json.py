import json
from datetime import datetime
import pymongo

add_json = False

"""
in mongosh:
    db.json_table.find({text:{$regex:'смарт',$options:'i'}})
    
    manual aggregation
    db.one_from_json.aggregate([
        {
            $lookup: {
                from:'json_table',localField:'json_table_id',foreignField:'_id',as:'json_data'
            }
        }
    ])
    
    aggregation by DBRef
    Does not work!!!
    db.one_from_json.aggregate([
        {
            $lookup: {
                from:'json_ref.$ref',localField:'json_ref.$id',foreignField:'_id',as:'json_data'
            }
        }
    ])

group by year, order by year    
db.json_table.aggregate([
    {
        $group: {
            _id: {
                'date': {
                    $slice: [ { $split: ['$date', ' '] }, 3, 1 ]
                }
            },
            count:{$sum:1}
        }
    },
    { $sort: {_id: 1} },
])
    
"""

client = pymongo.MongoClient("mongodb://localhost:27017/")
json_db = 'json_db'
db = client[json_db]

json_table = db['json_table']

if add_json:
    # json_file_name = '/home/tolic/gitrepo/learn_and_try/stuff/site_parser/articles.json'
    # json_file_name = '/home/tolic/gitrepo/github/my_python_projects/learn_and_try/' \
    #                  'stuff/site_parser/done/articles_from_hitech.json'
    json_file_name = '/home/tolic/gitrepo/github/my_python_projects/' \
                     'learn_and_try/stuff/site_parser/articles.json'
    json_table.drop()
    with open(json_file_name, 'r') as json_file:
        json_arr = json.load(json_file)
        json_table.insert_many(json_arr)

dt = datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
# dynamic_table = db[f'collection_{dt}']
# dynamic_table.insert_one({dt: dt})

# print(json_table.find_one({}))
# print(json_table.count_documents({}))

one_from_json = db['one_from_json']
one_from_json.delete_many({})
json_table_id = json_table.find_one({})['_id']
one_from_json.insert_one(
    {
        'json_ref': {
            '$ref': 'json_table',
            '$id': json_table_id,
            '$db': json_db,
        },
        'json_description': 'Ref to record in json_table',
        'json_table_id': json_table_id,
    }
)
