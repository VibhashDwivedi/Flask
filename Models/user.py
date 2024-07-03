from flask_pymongo import ObjectId
from db import mongo
from bson.json_util import dumps

class User:
    @staticmethod
    def create(name, email, phone, password):
        user_id = mongo.db.users.insert_one({
            "name": name,
            "email": email,
            "phone": phone,
            "password": password,
        }).inserted_id
        return str(user_id)

    @staticmethod
    def find(user_id):
        return mongo.db.users.find_one({"_id": ObjectId(user_id)})
    
    @staticmethod
    def get_all():
        users = mongo.db.users.find()
        return dumps(users)  # Convert the cursor to a JSON string
    
    @staticmethod
    def update(user_id, update_data):
        result = mongo.db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
        )
        return result.matched_count > 0
    
    @staticmethod
    def delete(user_id):
        result = mongo.db.users.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0
