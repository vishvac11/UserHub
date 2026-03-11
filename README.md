# UserHub

A small **User Management System** built with **Flask** and **SQLite** that supports full **CRUD**:
create users, view users, edit users, and delete users — with a clean Vanilla CSS and Bootstrap UI.

---

# Live Demo

The application is deployed on **Render** and can be accessed online.

Live URL:

```
https://userhub-5dt0.onrender.com/
```

---

# Features

- **Modern UI**: Bootstrap 5 layout + custom styling (`static/style.css`)
- **3-page flow**

  - **Home** (landing page)
  - **Add/Edit User** (better form + validation)
  - **View Users** (table with search + actions)

- **CRUD operations**

  - Create a new user
  - Read (list) all users
  - Update a user
  - Delete a user (with confirmation)

- **SQLite database**: auto-creates `database.db` and the `users` table on first run
- **Validation**

  - Name required
  - Email must look valid
  - Age must be a number between 0 and 150

---

# Pages

- **Home page**: `/`
- **Form input page** (create): `/users/new`
- **User viewing page** (list): `/users`

Editing and deleting are available from the **View Users** page.

---

# Tech Stack

- **Python**
- **Flask**
- **SQLite** (`sqlite3` from the Python standard library)
- **Bootstrap 5** (via CDN)
- **Render** (for cloud deployment)

---

# Project Structure

```
UserHub/
  app.py
  database.db              # created automatically after first run
  requirements.txt
  README.md

  static/
    style.css

  templates/
    base.html
    home.html
    user_form.html
    users.html
```

---

# Setup (Local Development)

## 1) Clone the Repository

```
git clone https://github.com/vishvac11/UserHub
cd userhub
```

---

## 2) Install Dependencies

```
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, install Flask manually:

```
pip install flask
```

---

## 3) Run the Application

```
python app.py
```

Open the browser and visit:

```
http://127.0.0.1:5000
```

---

# CRUD Operations & Routes

## Read

- **Home page**
  `GET /`

- **List users**
  `GET /users`

---

## Create

- **Show create form**
  `GET /users/new`

- **Create user**
  `POST /users/new`

---

## Update

- **Show edit form**
  `GET /users/<user_id>/edit`

- **Save edits**
  `POST /users/<user_id>/edit`

---

## Delete

- **Delete user**
  `POST /users/<user_id>/delete`

Note: Delete uses a **POST request** to prevent accidental deletions from simple link clicks.

---

# Database

The application uses a local SQLite database file:

```
database.db
```

Table schema:

```
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  email TEXT,
  age INTEGER
);
```

The database and table are **automatically created on first run**.

---

# Deployment on Render

This project is deployed using **Render**, a cloud platform for hosting web services.

## Deployment Steps

1. Push the project to **GitHub**.

2. Go to **Render Dashboard**

3. Click **New → Web Service**

4. Connect your GitHub repository.

5. Configure the service:

**Environment**

```
Python 3
```

**Build Command**

```
pip install -r requirements.txt
```

**Start Command**

```
gunicorn app:app
```

6. Click **Create Web Service**

Render will automatically:

- Install dependencies
- Build the application
- Start the Flask server
- Provide a public URL

---

# Notes About SQLite on Render

SQLite works for small applications and demos.

However, on the **Render free tier**, the filesystem is **ephemeral**, which means:

- The `database.db` file may reset when the service restarts.

For production applications, a cloud database such as **PostgreSQL** is recommended.

---

# Learning Outcomes

This project demonstrates:

- Full Stack Web Development basics
- Flask backend development
- CRUD operations
- HTML form handling
- SQLite database integration
- Cloud deployment using Render

---

# Author

Built with passion 👍 by **Vishva Chauhan**
