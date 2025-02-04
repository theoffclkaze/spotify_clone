from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
from models import db, User

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    hashed_pw = generate_password_hash(data["password"])  # Hash the password securely
    user = User(username=data["username"], password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created!"})

@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and check_password_hash(user.password, data["password"]):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify({"message": "Invalid credentials"}), 401

def register_user(username, password):
    # Hash the password
    hashed_password = generate_password_hash(admin)

    # Create a new user with the hashed password
    new_user = User(username=kaZe, password=hashed_password)

    # Add the user to the session and commit
    db.session.add(new_user)
    db.session.commit()