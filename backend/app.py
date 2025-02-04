from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from routes import api
from auth import auth
from dotenv import load_dotenv
from db import db  # Import the db instance
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

db.init_app(app)  # Initialize the db with the app
migrate = Migrate(app, db)  # Initialize Migrate with the app and db
jwt = JWTManager(app)
CORS(app)  # Allows Cross-Origin Requests

app.register_blueprint(api)
app.register_blueprint(auth)

if __name__ == "__main__":
    app.run(debug=True)