# Grundgerüst: Flask & React Symphony

## 1. Projektstruktur aufsetzen  
✅ **Ordner erstellen:**  
```
spotify-clone/
├── backend/  (Flask API)
├── frontend/ (React App)
```

✅ **In den Ordner wechseln & Git initialisieren:**  
```bash  
mkdir spotify-clone && cd spotify-clone  
git init  
```

---  

## 2. Backend mit Flask einrichten  
✅ **Python-Umgebung erstellen (optional, aber empfohlen):**  
```bash  
cd backend  
python -m venv venv  
source venv/bin/activate  # (Windows: venv\Scripts\activate)  
```

✅ **Flask & Abhängigkeiten installieren:**  
```bash  
pip install flask flask-restful flask-cors flask-jwt-extended sqlalchemy psycopg2  
```

✅ **Flask-Projektstruktur erstellen:**  
```
backend/
├── app.py        # Hauptdatei  
├── config.py     # Konfiguration (z. B. DB-Verbindung)  
├── models.py     # Datenbankmodelle  
├── routes.py     # API-Routen  
├── db.py         # Datenbank-Verbindung  
├── requirements.txt  # Paketliste  
```

✅ **Flask starten & testen:**  
```bash  
python app.py  
```
Öffne `http://127.0.0.1:5000/ping` im Browser → Sollte `{ "message": "pong!" }` anzeigen.  

---  

## 3. React-Frontend einrichten  
✅ **In den `frontend/` Ordner wechseln & React-Projekt erstellen:**  
```bash  
cd ../frontend  
npx create-react-app .   
```

✅ **React-Abhängigkeiten installieren:**  
```bash  
npm install axios react-router-dom  
```

✅ **Backend-Anfrage testen (`App.js` ändern):**  
```jsx  
import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/ping").then((response) => {
      setMessage(response.data.message);
    });
  }, []);

  return <h1>{message}</h1>;
}

export default App;
```

✅ **Frontend starten:**  
```bash  
npm start  
```
Sollte `pong!` auf der Webseite anzeigen.  

---  

## 4. PostgreSQL-Datenbank einrichten  
✅ **PostgreSQL installieren & starten**  
Falls noch nicht installiert: [Download PostgreSQL](https://www.postgresql.org/download/)  

✅ **Datenbank erstellen:**  
```sql  
CREATE DATABASE spotify_clone;  
```

✅ **Datenbank-Verbindung in `config.py` setzen:**  
```python  
DATABASE_URL = "postgresql://user:passwort@localhost/spotify_clone"  
```

✅ **SQLAlchemy & Migrations-Setup:**  
```bash  
pip install flask-migrate  
```

✅ **Datenbank-Migration erstellen & ausführen:**  
```bash  
flask db init  
flask db migrate -m "Initial migration"  
flask db upgrade  
```

---  

## 5. Authentifizierung mit JWT einbauen  
✅ **JWT in `config.py` aktivieren:**  
```python  
JWT_SECRET_KEY = "supergeheimes-passwort"  
```

✅ **User-Modell (`models.py` erstellen):**  
```python  
from flask_sqlalchemy import SQLAlchemy  

db = SQLAlchemy()  

class User(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    username = db.Column(db.String(80), unique=True, nullable=False)  
    password = db.Column(db.String(200), nullable=False)  
```

✅ **Login & Registrierung (`auth.py` erstellen):**  
```python  
from flask import Blueprint, request, jsonify  
from werkzeug.security import generate_password_hash, check_password_hash  
from flask_jwt_extended import create_access_token  

auth = Blueprint("auth", __name__)  

@auth.route("/register", methods=["POST"])  
def register():  
    data = request.get_json()  
    hashed_pw = generate_password_hash(data["password"])  
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
```

✅ **Login von React aus testen:**  
```jsx  
axios.post("http://127.0.0.1:5000/login", { username: "test", password: "pass" })  
  .then(res => console.log(res.data.access_token));  
```

---  

## 6. Audio-Streaming einbauen  
✅ **Streaming-Route in `routes.py` hinzufügen:**  
```python  
import os  
from flask import send_file  

@api.route("/stream/<filename>")  
def stream_audio(filename):  
    file_path = f"static/audio/{filename}"  
    if os.path.exists(file_path):  
        return send_file(file_path, mimetype="audio/mpeg")  
    return jsonify({"error": "File not found"}), 404  
```

✅ **React-Audio-Player einbauen (`Player.js` erstellen):**  
```jsx  
import React from "react";  

const Player = ({ file }) => {  
  return (  
    <audio controls>  
      <source src={`http://127.0.0.1:5000/stream/${file}`} type="audio/mpeg" />  
      Dein Browser unterstützt kein Audio-Tag.  
    </audio>  
  );  
};  

export default Player;  
```

✅ **Beispiel im `App.js` anzeigen:**  
```jsx  
<Player file="song.mp3" />  
```

---  

## 7. Deployment (optional, wenn fertig)  
✅ **Backend mit Gunicorn & Nginx hosten**  
✅ **Frontend mit Netlify/Vercel deployen**  
✅ **Datenbank in der Cloud hosten (z. B. Heroku, Supabase)**  

---  

Das wäre das Grundgerüst für deinen Spotify-Klon!

