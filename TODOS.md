# Spotify Clone To-Do List (For Dummies)

## 1️⃣ Start the Project
- [x] Create a new project on GitHub (Public, so people can see it)
- [x] Download and install **Python** if you don’t have it
- [x] Download and install **Node.js** if you don’t have it
- [x] Open **WebStorm**

## 2️⃣ Backend (The Brain of the App)
- [ ] Open **Terminal** in WebStorm
- [ ] Type this to create the backend folder: `mkdir backend && cd backend`
- [ ] Set up a virtual environment: `python -m venv venv`
- [ ] Activate it: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
- [ ] Install Django and some helpers: `pip install django djangorestframework mysqlclient`
- [ ] Create a new Django project: `django-admin startproject spotify_clone`
- [ ] Go into the project folder: `cd spotify_clone`
- [ ] Create a new Django app for the API: `python manage.py startapp music`
- [ ] Configure MySQL in `settings.py` to store music data
- [ ] Create models for songs, playlists, and user profiles in the `music` app
- [ ] Run migrations: `python manage.py makemigrations` and `python manage.py migrate`
- [ ] Create a basic API with Django REST Framework:
    - [ ] Login & Signup
    - [ ] Get songs from the database
    - [ ] Create and manage playlists
    - [ ] Add favorite songs to profiles
- [ ] Test your API using Postman or the browser (Django admin)

## 3️⃣ Frontend (The Look of the App)
- [ ] Open **Terminal** and go to the main folder
- [ ] Create the frontend: `npm create vite@latest frontend --template react`
- [ ] Go into the frontend folder: `cd frontend`
- [ ] Install everything: `npm install`
- [ ] Run it: `npm run dev` (Check if a page shows up in your browser)
- [ ] Build login and signup pages
- [ ] Build the music player UI (where songs play)
- [ ] Connect frontend to the backend API (fetch data from Django)
- [ ] Add search functionality for songs
- [ ] Add playlist features (create and manage playlists)

## 4️⃣ Extra Cool Stuff
- [ ] Let users edit their profile (change name, picture, etc.)
- [ ] Add **recommended songs** feature (optional but cool)
- [ ] Put the app **online** so others can see it (use Vercel, Heroku, or a server)

## 5️⃣ Finishing Up
- [ ] Write a **README.md** (explain what the project is)
- [ ] Make sure `.gitignore` is correct (so private stuff stays private)
- [ ] Push your code to GitHub
- [ ] Share your project in your portfolio 🚀
