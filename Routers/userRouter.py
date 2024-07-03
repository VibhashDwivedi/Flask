from flask import Blueprint, request, jsonify
from Models import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/submit', methods=['POST'])
def submit_user():
    name = request.json.get('name')
    email = request.json.get('email')
    phone = request.json.get('phone')
    
    if not name or not email or not phone:
        return jsonify({"error": "Missing data"}), 400

    user_id = User.create(name, email, phone)
    return jsonify({"message": "Data submitted successfully", "user_id": user_id}), 201

@user_bp.route('/getall', methods=['GET'])
def get_all_users():
    users = User.get_all() 
    return jsonify(users), 200