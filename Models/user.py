from flask_pymongo import ObjectId
from db import mongo
from bson.json_util import dumps

class User:
    @staticmethod
    def create(name, email, phone):
        user_id = mongo.db.users.insert_one({
            "name": name,
            "email": email,
            "phone": phone
        }).inserted_id
        return str(user_id)

    @staticmethod
    def find(user_id):
        return mongo.db.users.find_one({"_id": ObjectId(user_id)})
    
    @staticmethod
    def get_all():
        users = mongo.db.users.find()
        return dumps(users)  # Convert the cursor to a JSON string