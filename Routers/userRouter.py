from flask import Blueprint, request, jsonify
from Models import User

user_bp = Blueprint('user_bp', __name__)



@user_bp.route('/submit', methods=['POST'])
def submit_user():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')

    
    # if not name or not email or not phone or not password:
    #     return jsonify({"error": "Missing data"}), 400

    user_id = User.create(name, email, phone, password)
    # on sucessful submission get a alert that data submitted
    
    return jsonify({"message": "Data submitted successfully", "user_id": user_id}), 201

@user_bp.route('/getall', methods=['GET'])
def get_all_users():
    users = User.get_all() 
    return jsonify(users), 200

@user_bp.route('/update/<user_id>', methods=['PUT'])
def update_user(user_id):
    update_data = request.json
    
    if not update_data:
        return jsonify({"error": "No data provided for update"}), 400

    try:
        updated = User.update(user_id, update_data)
        if updated:
            return jsonify({"message": "User updated successfully"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        # Log the exception e
        return jsonify({"error": "An error occurred during the update"}), 500
    

@user_bp.route('/delete/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        deleted = User.delete(user_id)
        if deleted:
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        # Log the exception e
        return jsonify({"error": "An error occurred during the deletion"}), 500