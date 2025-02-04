# **Spotify Clone** - Flask & React Symphony

## Overview
Flask & React Symphony is a full-stack web application inspired by Spotify. It is built using Flask for the backend and React for the frontend. The project aims to demonstrate authentication, database management, and audio streaming functionalities.

## Features
- User authentication (JWT-based login & registration)
- Audio streaming using Flask API
- MySQL database for user and media storage
- RESTful API for handling requests
- React frontend with a music player
- Secure token-based authentication

## Tech Stack
- **Backend:** Flask, Flask-RESTful, Flask-JWT-Extended, SQLAlchemy
- **Frontend:** React, Axios, React Router
- **Database:** MySQL
- **Deployment:** Gunicorn, Nginx, Netlify/Vercel

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/theoffclkaze/spotify_clone.git
cd spotify_clone
```

### 2. Setup Backend (Flask)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

### 3. Setup MySQL Database
```sql
CREATE DATABASE spotify_clone;
```
Set the database URL in `config.py`:
```python
DATABASE_URL = "mysql+pymysql://username:password@127.0.0.1/spotify_clone"
```
Run migrations:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4. Start Backend Server
```bash
python app.py
```
API should be available at `http://127.0.0.1:5000/`

### 5. Setup Frontend (React)
```bash
cd ../frontend
npm install
npm start
```
Frontend should be running at `http://localhost:3000/`

## Usage
- **Register/Login:** Create an account and log in
- **Upload & Stream Music:** API supports MP3 file uploads and streaming
- **Play Music:** Use the React audio player to listen to tracks

## API Endpoints
- `POST /register` - Register a new user
- `POST /login` - Login and receive a JWT token
- `GET /stream/<filename>` - Stream an audio file

## Deployment
- Deploy backend using Gunicorn & Nginx
- Deploy frontend on Netlify/Vercel
- Host database on a cloud provider (e.g., Heroku, Supabase)

## License
MIT License

