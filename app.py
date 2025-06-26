from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from email_validator import validate_email, EmailNotValidError
from bson import ObjectId
from bson.json_util import dumps

app = Flask(__name__)
# Database configuration - using default port
app.config["MONGO_URI"] = "mongodb://mymongo_1:27017/college"

# Initialize extensions
db = PyMongo(app)
pw_hasher = Bcrypt(app)

# Helper to verify email format (.com only)
def check_email_validity(email_address):
    try:
        validation_result = validate_email(email_address)
        if not validation_result.email.endswith(".com"):
            return False
        return True
    except EmailNotValidError:
        return False

@app.route("/users", methods=["GET"])
def fetch_all_users():
    """Retrieve all student records without sensitive data"""
    user_records = db.db.students.find({}, {"password": 0})
    return dumps(user_records), 200

@app.route("/users/<id>", methods=["GET"])
def fetch_single_user(id):
    """Get individual user by document ID"""
    user_data = db.db.students.find_one({"_id": ObjectId(id)}, {"password": 0})
    if user_data is None:
        return jsonify({"error": "User not found"}), 404
    return dumps(user_data), 200

@app.route("/users", methods=["POST"])
def add_new_user():
    """Create new student account"""
    payload = request.get_json()
    # Validate required fields exist
    required_fields = ["name", "email", "password"]
    if not all(field in payload for field in required_fields):
        return jsonify({"error": "All fields are required"}), 400

    email = payload["email"]
    if not check_email_validity(email):
        return jsonify({"error": "Invalid email format (must end in .com)"}), 400
    
    # Securely process password
    raw_password = payload["password"]
    hashed_password = pw_hasher.generate_password_hash(raw_password).decode("utf-8")
    
    new_student = {
        "name": payload["name"],
        "email": email,
        "password": hashed_password
    }
    
    insert_result = db.db.students.insert_one(new_student)
    return jsonify({
        "message": "User created",
        "id": str(insert_result.inserted_id)
    }), 201

@app.route("/users/<id>", methods=["PUT"])
def modify_user(id):
    """Update existing user information"""
    update_data = request.get_json()
    update_fields = {}
    
    # Process valid fields
    if "name" in update_data:
        update_fields["name"] = update_data["name"]
    
    if "email" in update_data:
        if not check_email_validity(update_data["email"]):
            return jsonify({"error": "Invalid email format (must end in .com)"}), 400
        update_fields["email"] = update_data["email"]
    
    if "password" in update_data:
        hashed_pw = pw_hasher.generate_password_hash(update_data["password"]).decode("utf-8")
        update_fields["password"] = hashed_pw
    
    # Only update if changes exist
    if update_fields:
        result = db.db.students.update_one(
            {"_id": ObjectId(id)},
            {"$set": update_fields}
        )
        if result.matched_count == 0:
            return jsonify({"error": "User not found"}), 404
    
    return jsonify({"message": "User updated"}), 200

@app.route("/users/<id>", methods=["DELETE"])
def remove_user(id):
    """Permanently delete user record"""
    deletion_result = db.db.students.delete_one({"_id": ObjectId(id)})
    if deletion_result.deleted_count < 1:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted"}), 200

# Main entry point
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)