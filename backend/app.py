from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes import api
from auth import auth  # <-- Add this import
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, but recommended
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  # Sicherer JWT-Key

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)  # JWT aktivieren
CORS(app)  # Allows Cross-Origin Requests

app.register_blueprint(api)
app.register_blueprint(auth)  # <-- Register the auth blueprint

if __name__ == "__main__":
    app.run(debug=True)